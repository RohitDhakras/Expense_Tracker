# Generated by Django 5.0.6 on 2024-06-14 14:37

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_expense_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.TextField(unique=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
