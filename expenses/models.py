from datetime import date
from django.db import models
from categories.models import categories
import django.utils.timezone as date
from django.contrib.auth.models import User

# Create your models here.

class expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    expense_date = models.DateField(default=date.now)
    expense_category = models.ForeignKey(categories, on_delete=models.SET_NULL, null=True)
    expense_amount = models.FloatField()
    
    def __str__(self):
        return str(self.expense_date)