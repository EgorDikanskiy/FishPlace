# Generated by Django 4.2.5 on 2024-03-26 21:44

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0009_alter_user_avatar_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(
                default='/avatars/base.jpg',
                upload_to=users.models.User.path_to_save,
                verbose_name='аватарка',
            ),
        ),
    ]
