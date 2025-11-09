from django.contrib import admin

# Register your models here.

from .models import * 

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'adress', 'sex', 'age', 'city', 'zip_code', 'created_data', 'save_by')


class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'invoice_date_time', 'total', 'last_update_date', 'paid', 'invoice_type', 'comments')


admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)