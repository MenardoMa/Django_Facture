from django.shortcuts import render

from django.views import View

from .models import *

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