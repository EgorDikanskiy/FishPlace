# Generated by Django 4.2.5 on 2024-03-27 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_alter_spot_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name='пользователь',
            ),
        ),
    ]
