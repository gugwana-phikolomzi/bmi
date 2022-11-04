from django.shortcuts import render
from .forms import MatricForm, ImperialForm
import numpy as np



def home(request):
    args ={}
    return render(request, 'index/home.html', args)

def matric(request):
    form = MatricForm(request.POST)
    bmi=0
    if form.is_valid():
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height']

        bmi = np.round((weight / height**2),0)


    form = MatricForm()


    args ={'form':form,'bmi':bmi}

    return render(request, 'index/matric.html', args)

def imperial(request):
    form = ImperialForm(request.POST)
    bmi=0
    if form.is_valid():
        weight = form.cleaned_data['weight']
        height = form.cleaned_data['height']

        bmi = np.round(((703*weight) / height**2),0)
    
    form = ImperialForm()

    args ={'form':form,'bmi':bmi}

    return render(request, 'index/imperial.html', args)