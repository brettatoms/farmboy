from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django import forms
from django.contrib import messages
from django.urls import reverse

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
            messages.success(request, f'{ form["name"].data } saved')
            return redirect('crops_add')
    else:
        form = CropForm()

    context = {
        'form': form,
        'form_action': reverse('crops_add'),
        'save_button_text': 'Create',
        'header_text': 'Add crop'
    }
    return render(request, 'crops/crop_form.html', context)


def update(request, crop_id):
    instance = get_object_or_404(Crop, pk=crop_id)
    form = CropForm(request.POST or None, instance=instance)
    print(form)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        messages.success(request, f'{ form["name"].data } saved')
        return redirect('crops_edit', crop_id)

    context = {
        'form': form,
        'form_action': reverse('crops_edit', kwargs={
            'crop_id': instance.id
        }),
        'save_button_text': 'Save',
        'header_text': instance.name
    }
    return render(request, 'crops/crop_form.html', context)
