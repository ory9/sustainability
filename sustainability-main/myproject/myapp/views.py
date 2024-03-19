from django.shortcuts import render
from .models import Manufacturer, Product
from django.http import HttpResponse
from django.http import HttpResponse
from .forms import NameForm
from django.shortcuts import render, get_object_or_404
from myapp.models import Product

# Create your views here.
def ft_try(request):
    return HttpResponse("Hello, world. You're at the ft_try index.")


def get_name(request):
    if reques.method == "POST":
        form = NameForm(request.Form)
        if form.isvalid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    
    return render(request, "name.html", {"form": form})

def index(request):

    products = Product.objects.all()
    
    return render(request, 'base/base.html', {'product': products})

def detail(request, slug=None):

    products = get_object_or_404(Product, slug=slug)

    return render(request, 'base/base.html', {'product': products})

def about(request):

    products = Product.objects.all()
    
    return render(request, '/myapp/about.html', {'product': products})