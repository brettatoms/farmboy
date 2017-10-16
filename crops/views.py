from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django import forms
from django.contrib import messages

from .models import Crop


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description']


def index(request):
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crops/crops.html', context)


def detail(request, crop_id):
    crop = get_object_or_404(Crop, pk=crop_id)
    context = {'crop': crop}
    return render(request, 'crops/crop_detail.html', context)


def create(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{ form["name"].data} saved')
            return redirect('crops_add')
    else:
        form = CropForm()

    context = {'form': form}
    return render(request, 'crops/crop_add.html', context)
