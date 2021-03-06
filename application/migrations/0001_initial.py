# Generated by Django 4.0.1 on 2022-01-31 20:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона необходимо ввести в формате: '+999999999'. Допускается до 15 цифр.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
