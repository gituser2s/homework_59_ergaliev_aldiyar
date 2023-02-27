# Generated by Django 3.2 on 2023-02-24 14:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('OTHER', 'Разное'), ('FOOD', 'Еда'), ('CAR', 'Автомобиль')], default='OTHER', max_length=20, verbose_name='Категория')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('photo', models.TextField(max_length=3000, verbose_name='Фото')),
                ('count', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Время и дата удаления')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
            },
        ),
    ]