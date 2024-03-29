# Generated by Django 4.2.5 on 2024-03-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0005_alter_spot_tags'),
        ('users', '0004_user_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.IntegerField(
                blank=True, null=True, verbose_name='Стаж в годах'
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='catalog.region',
                verbose_name='Место жительства',
            ),
        ),
    ]
