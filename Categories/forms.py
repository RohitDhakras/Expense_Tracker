from django.core import validators
from django import forms
from .models import categories

class manageCategoriesForm(forms.ModelForm):
    class Meta:
        model = categories
        fields = ["category"]
        labels = {
            "category": "Category",
        }
        widgets = {
            "category": forms.TextInput(
                attrs= {
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Enter Category",
                }
            ),
        }