from django.shortcuts import redirect, render
from .models import *
from .forms import *

def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request , 'products.html' , context)

def new(request):
    if request.method == "post":
        form = ProductForm()
        if form.is_valid():
            form.save()
            return redirect('products:products')
    else:
        form = ProductForm()
    context = {
        'form':form,

    }
    return render(request , 'new.html' , context)



