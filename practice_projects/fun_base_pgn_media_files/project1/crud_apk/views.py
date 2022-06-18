from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator
from fpdf import FPDF

# Create your views here.
def customerformView(request):
    form = CustomerForm
    template_name = 'crud_apk/customerform.html'
    context = {'form' : form}

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showcustomer_url')
    return render(request, template_name, context)

def showcustomerView(request):
    data = Customer.objects.all().order_by('cid')
    template_name = 'crud_apk/showcustomer.html'
    paginator = Paginator(data,2)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    return render(request, template_name, context={'page_obj': page_obj})

def updateView(request, id):
    obj = Customer.objects.get(cid=id)
    form = CustomerForm(instance = obj)
    template_name = 'crud_apk/customerform.html'
    context = {'form':form}
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('showcustomer_url')
    return render(request, template_name, context)

def deleteView(request, id):
    obj = Customer.objects.get(cid=id)
    template_name = 'crud_apk/delete.html'
    context = {'obj':obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showcustomer_url')
    return render(request, template_name, context)

def reportView(request, id):
    obj = Customer.objects.get(cid = id)
    pdf = FPDF('p', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'CUSTOMER_REPORT',0 ,1)
    pdf.cell(40, 10, '', 0, 1)

    print(obj.cid)

    pdf.cell(200, 8, f'CUSTOMER_ID : {obj.cid}', 0, 1)
    pdf.cell(200, 8, f'FIRST NAME : {obj.fname}', 0, 1)
    pdf.cell(200, 8, f'LAST NAME : {obj.lname}', 0, 1)
    pdf.cell(200, 8, f'EMAIL ID : {obj.mail}', 0, 1)
    pdf.cell(200, 8, f'CITY : {obj.city}', 0, 1)
    pdf.cell(200, 8, f'MOBILE NUMBER : {obj.mob_no}', 0, 1)
    pdf.cell(200, 8, f'PRODUCT : {obj.product}', 0, 1)
    pdf.cell(200, 8, f'PRICE : {obj.price}', 0, 1)

    pdf.cell(200, 8, f'http://127.0.0.1:8000{obj.image.url}', 0, 1)

    pdf.output('Customer_report.pdf', 'F')
    return FileResponse(open('Customer_report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')