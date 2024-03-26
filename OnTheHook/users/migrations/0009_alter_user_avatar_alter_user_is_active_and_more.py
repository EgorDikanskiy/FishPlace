# Generated by Django 4.2.5 on 2024-03-26 21:40

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0008_rename_uuid_activate_user_token_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(
                default='/media/avatars/base.jpg',
                upload_to=users.models.User.path_to_save,
                verbose_name='аватарка',
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(
                default=False, verbose_name='Пользователь активен'
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='token_activate',
            field=models.CharField(
                blank=True,
                help_text='уникальная штука для активации',
                max_length=50,
                null=True,
                verbose_name='Токен',
            ),
        ),
    ]