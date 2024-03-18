from django.shortcuts import render, get_object_or_404

from landinapp.models import Flower

def index(request):

    flowers = Flower.objects.all()
    
    return render(request, 'index.html', {'flowers': flowers })
