from django.shortcuts import render, get_object_or_404

from myapp.models import Product_Name

def index(request):

    product = Product_Name.objects.all()
    
    return render(request, 'myapp/form.html', {'products': product})

def detail(request, slug=None):

    product = get_object_or_404(Product_Name, slug=slug)

    return render(request, 'myapp/form.html', {'products': product})
