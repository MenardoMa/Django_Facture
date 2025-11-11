from django import forms 
from .models import Customer, Invoice
from django.contrib.auth.models import User

class FormCustomer(forms.ModelForm):

    SEX_TYPE = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]

    name   = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre nom'}))
    email  = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre email'}))
    phone  = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre phone'}))
    address = forms.CharField(label='', max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre addres'}))
    sex    = forms.ChoiceField(label='', choices=SEX_TYPE , widget=forms.Select(attrs={'class': 'form-control'}))
    age    = forms.CharField(label='', required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'votre age'}))
    city   = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ville'}))
    zip_code = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip code'}))

    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code')


class FormInvoice(forms.ModelForm):

    INVOICE_TYPE = [
        ('R', 'RECU'),
        ('P', 'PROFORMA FACTURE'),
        ('F', 'FACTURE'),
    ]

    customer = forms.ChoiceField(label='', widget=forms.Select(attrs={'class': 'form-control'}))    
    total    = forms.CharField(label='', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total'}))
    qte      = forms.CharField(label='', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantité'}))
    paid     = forms.BooleanField(label='', widget=forms.BooleanField())
    comments = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control'}))
    invoice_type = forms.ChoiceField(label='',choices= INVOICE_TYPE, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Invoice
        fields = ('customer', 'total', 'qte', 'paid', 'comments', 'invoice_type')
