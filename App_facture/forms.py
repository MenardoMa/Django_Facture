from django import forms 
from .models import Customer
from django.contrib.auth.models import User

class FormCustomer(forms.ModelForm):

    SEX_TYPE = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]

    name   = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre nom'}))
    email  = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre email'}))
    phone  = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre phone'}))
    address = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre addres'}))
    sex    = forms.ChoiceField(label='', choices=SEX_TYPE , widget=forms.Select(attrs={'class': 'form-control'}))
    age    = forms.CharField(label='', required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'votre age'}))
    city   = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ville'}))
    zip_code = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip code'}))
    user = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user'}))

    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code', 'user')
