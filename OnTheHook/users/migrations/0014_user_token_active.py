# Generated by Django 4.2.5 on 2024-03-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0013_alter_user_experience_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token_active',
            field=models.BooleanField(
                default=True, verbose_name='Токен активен'
            ),
        ),
    ]
