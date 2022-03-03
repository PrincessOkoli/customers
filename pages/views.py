from django.shortcuts import render, redirect
from pages.models import customers
from pages.form import AddForm

# Create your views here.
def home(reguest):
    customerlist = customers.objects.all()
    return render(reguest, 'page/home.html', {'customerlist': customerlist})

def about(reguest):
    return render(reguest, 'page/about.html')

def contact(reguest):
    return render(reguest, 'page/contact.html')

def create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        phone = request.POST['phone']

        form = customers(first_name=firstname, Last_name=lastname, age=age, phone=phone)
        form.save()
        return redirect('/')

    return render(request, 'page/create.html')

def add(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AddForm()


    return render(request, 'page/add.html', {'form': form})

def detail(request, id):
    customer = customers.objects.get(id=id)
    return render(request, 'page/detail.html', {'customer': customer})


def delete(request, id):
    customer = customers.objects.get(id=id)
    customer.delete()
    return redirect('/')

def edit(request, id):
    customer = customers.objects.get(id=id)
    form = AddForm(instance=customer)

    if request.method == 'POST':
        form = AddForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AddForm()
    return render(request, 'page/edit.html', {'form': form, 'customer': customer})

