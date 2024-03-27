from django.contrib import admin
from django.contrib.auth import get_user_model

__all__ = []

User = get_user_model()


class UserAdministrator(admin.ModelAdmin):
    model = User

    readonly_fields = (
        "id",
        User.token.field.name,
        User.date_joined.field.name,
    )
    fields = (
        "id",
        User.username.field.name,
        User.first_name.field.name,
        User.last_name.field.name,
        User.email.field.name,
        User.avatar.field.name,
        User.last_login.field.name,
        User.is_active.field.name,
        User.is_superuser.field.name,
        User.is_staff.field.name,
        User.token_active.field.name,
        User.token.field.name,
        User.date_joined.field.name,
    )
    exclude = (User.password.field.name,)


admin.site.register(User, UserAdministrator)
