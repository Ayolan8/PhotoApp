from django.shortcuts import render, get_object_or_404
from .models import Photos
from django.contrib.auth.decorators import login_required

def home(request):
    item =  Photos.objects.all()

    return render(request, 'core/home.html', {'items': item})

def detail_list(request, slug):
    item = get_object_or_404(Photos, slug=slug)

    return render(request, 'core/detail.html', {'item': item})

@login_required
def my_photos(request):
    myphoto = Photos.objects.filter(created_by=request.user)

    return render(request, 'core/myphoto.html', {'myphotos': myphoto})