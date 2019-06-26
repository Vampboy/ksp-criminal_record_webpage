from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import path, include
from .forms import *


def base(request):
   form = CriminalForm()
   return render(request, 'index.html', {'form': form})


def criminal_view(request): 
  
    if request.method == 'POST': 
        form = CriminalForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            return redirect('success') 
    else: 
        form = CriminalForm() 
    return render(request, 'upload.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 