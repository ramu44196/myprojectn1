from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()

    return render(request, 'customers/customer_list.html', {
        'customers': customers
    })
def add_customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        company = request.POST['company']
        address = request.POST['address']

        Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            address=address
        )

        return redirect('customer_list')

    return render(request, 'customers/add_customer.html')

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.company = request.POST['company']
        customer.address = request.POST['address']

        customer.save()

        return redirect('customer_list')

    return render(request, 'customers/edit_customer.html', {
        'customer': customer
    })

    def delete_customer(request, id):
        customer = Customer.objects.get(id=id)
        customer.delete()

    return redirect('customer_list')