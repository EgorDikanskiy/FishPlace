from django.conf import settings
from django.contrib.auth import login
from django.core.mail import EmailMultiAlternatives
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import generic, View

from users.forms import CustomUserCreateForm, EditProfile
from users.models import User
from users.utils import email_confirmation_token


__all__ = []

PATH = "users/"


class ProfileView(View):
    template = PATH + "profile.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["model"] = request.user
        self.context["form"] = EditProfile(instance=request.user)

        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            file = request.FILES.get("avatar")
            if file:
                request.user.avatar = file
                request.user.save()
        self.context["form"] = form
        return render(request, self.template, self.context)


class RegisterView(generic.FormView):
    template_name = PATH + "auth/register.html"
    form_class = CustomUserCreateForm
    success_url = "/auth/profile/"

    def form_valid(self, form):
        normalize_email = User.objects.normalize_email(
            form.cleaned_data["email"],
        )
        form.is_active = settings.DEFAULT_USER_IS_ACTIVE
        form.email = normalize_email

        user = form.save(commit=False)
        user.token_activate = email_confirmation_token.make_token(user)
        user.save()

        subject = "Подтверждение аккаунта"
        link = "http://localhost:8000" + reverse(  # URL
            "users:activate",
            args=[user.id, user.token_activate],
        )
        html_message = render_to_string(
            "auth_email.html",
            {
                "confirmation_link": link,
                "username": user.username,
            },
        )
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = [user.email]
        msg = EmailMultiAlternatives(subject, plain_message, from_email, to)
        msg.attach_alternative(html_message, "text/html")
        msg.send()

        return super().form_valid(form)


class ActivateView(generic.View):
    context = {}

    def get(self, request, **kwargs):
        try:
            user = User.objects.get(**kwargs)
        except User.DoesNotExist:
            user = None
        if isinstance(user, User) and not user.is_active:
            user.is_active = True
            user.save()
            login(
                request,
                user,
                "OnTheHook.backends.ModifyLogin",
            )
            return redirect(reverse("users:profile"))

        return Http404("Ошибка")
