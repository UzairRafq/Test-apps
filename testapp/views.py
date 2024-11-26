from django.shortcuts import render
from testapp.models import TestModel
from django.contrib import messages


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        sold_currency = request.POST.get('sold_currency')
        get_currency = request.POST.get('get_currency')
        ph_number = request.POST.get('ph_number')
        location = request.POST.get('location')
    
        TestModel.objects.create(
            name = name,
            sold_currency = sold_currency,
            get_currency = get_currency,
            phone_number = ph_number,
            location = location
        )
        messages.success(request,'Data Added !!')
        
    data = TestModel.objects.all()
    return render(request, 'index.html', {'data':data})
