from django.shortcuts import render

def index(request):

    product = product_name.objects.all()
    
    return render(request, 'base/base.html', {'products': product})
