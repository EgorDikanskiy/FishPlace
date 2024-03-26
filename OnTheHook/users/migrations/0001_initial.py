# Generated by Django 4.1 on 2023-12-19 22:04

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.managers
import users.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'password',
                    models.CharField(max_length=128, verbose_name='password'),
                ),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        help_text='имя отображаемое для всех пользователей (nickname).\nДопустимые символы: латиница, цифры, @|.|+|-|_',
                        max_length=25,
                        unique=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(25),
                            django.core.validators.MinLengthValidator(4),
                            django.contrib.auth.validators.UnicodeUsernameValidator(),
                        ],
                        verbose_name='пользовательское имя',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        help_text='почтовый ящик',
                        max_length=254,
                        unique=True,
                        verbose_name='почта',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True,
                        help_text='как вас родители назвали',
                        max_length=150,
                        null=True,
                        verbose_name='имя',
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name='Фамилия. Как у отца или псевдоним',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text='деньи время, когда пользователь зарегистрировался',
                        null=True,
                        verbose_name='дата присоединения',
                    ),
                ),
                (
                    'avatar',
                    models.ImageField(
                        upload_to=users.models.User.path_to_save,
                        verbose_name='аватарка',
                    ),
                ),
                (
                    'birthday',
                    models.DateField(
                        blank=True,
                        help_text='ДД.ММ.ГГГГ',
                        null=True,
                        verbose_name='День рождения',
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='тебе дозволенно всё',
                        verbose_name='владыка',
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False, verbose_name='персонал'
                    ),
                ),
                (
                    'is_moderator',
                    models.BooleanField(
                        default=False, verbose_name='модератор'
                    ),
                ),
                (
                    'is_redactor',
                    models.BooleanField(
                        default=False, verbose_name='редактор'
                    ),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'location',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='catalog.region',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]
