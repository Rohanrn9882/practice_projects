from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_url')
def laptopformView(request):
    form = LaptopForm()
    template_name = 'crud_apk/laptopform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showdata_url')
    return render(request, template_name, context)

@login_required(login_url='login_url')
def showlaptopView(request):
    data = Laptop.objects.all()
    template_name = 'crud_apk/showlaptop.html'
    context = {'data': data}
    return render(request, template_name, context)

def updateView(request, id):
    obj = Laptop.objects.get(laptop_id=id)
    form = LaptopForm(instance = obj)
    template_name = 'crud_apk/laptopform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showdata_url')
    return render(request, template_name, context)

def deleteView(request, id):
    obj = Laptop.objects.get(laptop_id = id)
    template_name = 'crud_apk/deleteConfirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showdata_url')
    return render(request, template_name, context)
