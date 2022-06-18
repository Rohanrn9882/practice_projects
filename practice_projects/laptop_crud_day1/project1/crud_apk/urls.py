from django.urls import path
from . import views

urlpatterns = [
    path('laptop/', views.laptopformView, name='laptopform_url'),
    path('showdata/', views.showlaptopView, name='showdata_url'),
    path('update/<int:id>/', views.updateView, name='update_url'),
    path('delete/<int:id>/', views.deleteView, name='delete_url'),
]