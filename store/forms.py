from django import forms
from .models import Customer


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['User Name', 'First Name', 'Last Name', 'Email']
