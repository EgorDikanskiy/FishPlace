# Generated by Django 4.2.5 on 2024-03-26 20:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0007_user_uuid_activate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uuid_activate',
            new_name='token_activate',
        ),
    ]