# Generated by Django 4.2.5 on 2024-01-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FishTag',
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
                ('slug', models.TextField(unique=True, verbose_name='тег')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.AddField(
            model_name='spot',
            name='tags',
            field=models.ManyToManyField(
                help_text='Выберите или добавьте тег',
                to='catalog.fishtag',
                verbose_name='Теги',
            ),
        ),
    ]
