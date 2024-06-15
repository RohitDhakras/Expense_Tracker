from django.core import validators
from django import forms
from .models import expense
from categories.models import categories

class DateInput(forms.DateInput):
    input_type = 'date'

class manageExpenseForm(forms.ModelForm):
    class Meta:
        model = expense
        fields = ["expense_date", "expense_category", "expense_amount"]
        labels = {
            "expense_date": "Expense Date",
            "expense_category": "Expense Category",
            "expense_amount": "Expense Amount",
        }
        widgets = {
            "expense_date": DateInput(
                attrs= {
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Expense Date",
                },
                format='%d%m%Y',
            ),
            "expense_category": forms.Select(
                attrs= {
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Expense Date",
                },
            ),
            "expense_amount": forms.NumberInput(
                attrs= {
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Expense Amount",
                },
            ),
        }

