# Generated by Django 4.1 on 2023-12-19 22:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import rating.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingImages',
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
                    'image',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=rating.models.RatingImages.upload_to,
                        verbose_name='изображение',
                    ),
                ),
            ],
            options={
                'verbose_name': 'изображения',
                'verbose_name_plural': 'изображения',
            },
        ),
        migrations.CreateModel(
            name='SpotRating',
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
                    'mark',
                    models.SmallIntegerField(
                        choices=[
                            (5, 'Любовь'),
                            (4, 'Обожание'),
                            (3, 'Нейтрально'),
                            (2, 'Неприязнь'),
                            (1, 'Ненависть'),
                            (0, 'Удалить'),
                        ],
                        verbose_name='оценка',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(
                        auto_now=True, verbose_name='дата отзыва'
                    ),
                ),
                (
                    'comment',
                    ckeditor.fields.RichTextField(
                        help_text='Оставьте комментарий',
                        verbose_name='Комментарий',
                    ),
                ),
                (
                    'spot',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='catalog.spot',
                        verbose_name='товар',
                    ),
                ),
            ],
            options={
                'verbose_name': 'рэйтинг',
                'verbose_name_plural': 'рэйтинги',
            },
        ),
    ]
