from django.urls import path
from . import views

urlpatterns = [
    path('addcustomer/', views.customerformView, name='customerform_url'),
    path('showcustomer/', views.showcustomerView, name ='showcustomer_url'),
    path('update/<int:id>/', views.updateView, name='update_url'),
    path('delete/<int:id>/', views.deleteView, name='delete_url'),
    path('pdfreport/<int:id>/', views.reportView, name='pdf_url')
]