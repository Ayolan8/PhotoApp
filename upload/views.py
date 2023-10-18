from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddForm, EditForm
from core.models import Photos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Add photos
@login_required
def addform(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "You've added a photo successfully!!!")
            return redirect('my_photos')
        
    else:
        form = AddForm()

    return render(request, 'upload/addform.html', {'form': form, 'title': addform})

# Edit photo and its detail
@login_required
def editform(request, slug):
    upload = get_object_or_404(Photos, slug=slug, created_by=request.user)
    if request.method == "POST":
        form = EditForm(request, request.POST, request.FILES, instance=upload)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "Image Updated Successfully!!!")
            return redirect('my_photos')
        
    else:
        form = EditForm(instance=upload)

    return render(request, 'upload/editform.html', {'form': form, 'title': editform})

# Pre - delete page
@login_required
def delete_warning(request, slug):
    item = Photos.objects.get(slug=slug, created_by=request.user)

    return render(request, 'upload/delete.html', {'item': item})

# Delete photo
@login_required
def delete_photo(request, slug):
    item = Photos.objects.get(slug=slug, created_by=request.user)
    item.delete()
    return redirect('/myphotos/')
