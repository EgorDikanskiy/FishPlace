# Generated by Django 4.2.5 on 2024-01-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0004_rename_slug_fishtag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='tags',
            field=models.ManyToManyField(
                help_text='Выберите или добавьте тег',
                to='catalog.fishtag',
                verbose_name='Tags',
            ),
        ),
    ]