from random import randint
from django.shortcuts import redirect, render

from .models import Student
from .forms import StudentForm 
from faker import Faker
# import sqlite3


# Create your views here.
def studentcreateView(request):
    form = StudentForm
    template_name = 'crud_apk/studentform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context)

def showstudentView(request):
    data = Student.objects.all()
    template_name = 'crud_apk/showstudent.html'
    context = {'data': data}
    return render(request, template_name, context)

def updatestudentView(request, id):
    obj = Student.objects.get(rn = id)
    form = StudentForm(instance = obj)
    template_name = 'crud_apk/studentform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context)

def deletestudentView(request, id):
    obj = Student.objects.get(rn = id)
    template_name = 'crud_apk/deleteconfirm.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)


# fake_data = Faker()

# connection = sqlite3

# connection = sqlite3.connect('database_faker.db')

# cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS fakedata_table (rn integer, name text, mark float, mail text, city text)''')

# cursor.execute('INSERT INTO fakedata_table VALUES(:rn, :name, :mark, :mail, :city)',
#                 {'rn': fake_data.rn(), 'name': fake_data.name(), 'mark': fake_data.mark(), 'mail': fake_data.mail(), 'city': fake_data.city()}
# )

# cursor.execute('SELECT * FROM fakedata_table')
# connection.commit()
# connection.close()

def fakedataView(request):
    fake = Faker()

    fake_rn = randint(15,50)
    
    fake_name = fake.name()
    fake_mark = randint(50,95)
    
    fake_mail = fake.email()
    fake_city = fake.city()

    obj = Student(rn = fake_rn, name = fake_name, mark = fake_mark, mail = fake_mail, city = fake_city)
    obj.save()

    return redirect('show_url')



