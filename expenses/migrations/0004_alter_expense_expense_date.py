# Generated by Django 5.0.6 on 2024-06-14 09:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_user_alter_expense_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
