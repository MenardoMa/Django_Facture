from django.shortcuts import render, redirect

from django.views import View

from .models import *
from .forms import FormCustomer
from django.contrib.auth.models import User

from django.contrib import messages

class HomeView(View):

    template_name = 'home.html'
    invoices = Invoice.objects.select_related('customer', 'save_by').all()

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
                form.save()
                messages.success(request, 'Customer ajouter avec success')
                return redirect('home')
            else:
                messages.success(request, 'Une erreur est survenie')
                return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)