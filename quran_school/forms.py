# quran_school/forms.py
from django import forms
from .models import MonthlyPayment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = MonthlyPayment
        fields = ['amount', 'month', 'year']
        widgets = {
            
            'month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'year': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
        }
