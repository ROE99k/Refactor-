from django.shortcuts import render
from .models import  Product 

def home(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items})
