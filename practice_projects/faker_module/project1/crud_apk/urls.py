from django.urls import path
from . import views

urlpatterns = [
    path('addstudent/', views.studentcreateView, name='studentform_url'),
    path('showdata/', views.showstudentView, name='show_url'),
    path('update/<int:id>/', views.updatestudentView, name='update_url'),
    path('delete/<int:id>/', views.deletestudentView, name='delete_url'),
    path('fakedata/', views.fakedataView, name='fakedata_url'),

]