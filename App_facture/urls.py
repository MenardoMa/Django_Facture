from django.urls import path

from . import views

app_name = 'facture'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('addCustomer/', views.AddCustorm.as_view(), name='addCustomer'),
    path('addInvoice/', views.AddInvoice.as_view(), name='addInvoice'),
]