from django.shortcuts import render, redirect

from django.views import View
from .models import *
from .forms import FormCustomer, FormInvoice
from django.contrib.auth.models import User

from django.contrib import messages

class HomeView(View):

    template_name = 'home.html'
    invoices = Invoice.objects.select_related('customer', 'save_by').all() 
    #select_related('customer', '') selection les elements et leurs relation associer 

    context = {
        'invoices' : invoices
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        pass

class AddCustorm(View):

    template_name = 'forms.html'

    context = {
        'form' : FormCustomer
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            form = FormCustomer(request.POST)
            
            if form.is_valid():
                customer = form.save(commit=False) # ne sauvegarde pas encore dans la table
                customer.save_by = request.user    # depuis la request on recupere l'utilisateur connecter
                customer.save()                    # on sauvegarde dans la table customer
                messages.success(request, 'Customer ajouter avec success')
                return redirect('home')
            else:

                context = {
                    'form' : form
                }

                messages.success(request, 'Une erreur est survenie')
                return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)
    

class AddInvoice(View):

    template_name = 'forms.html'

    context = {
        'etat' : 'addinvoive',
        'form' : FormInvoice
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)