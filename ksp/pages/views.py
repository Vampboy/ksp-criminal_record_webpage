from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path, include
from .forms import *
from pages.criminal_script.CriminalRecognition import *
import face_recognition
import time
from django.template import loader, Context
from .models import criminal


def base(request):
    form = CriminalForm()
    return render(request, 'index.html', {'form': form})


def import_iter(img):
    res=[]

    np_im = face_recognition.load_image_file(img)
    criminal_instance = CriminalRecognition()
    
    if criminal_instance.validator(np_im):
        
        import os
        filenames_from_db = criminal.objects.all()
        count=0

        for i in range(len(filenames_from_db)):

            img2 = face_recognition.load_image_file(filenames_from_db[i].criminal_Img)

            if criminal_instance.face_compare(np_im, img2):
                res.append(filenames_from_db[i])
                count+=1
                if count>=5:
                    break
    return res


def criminal_view(request):

    if request.method == 'POST':
        form = CriminalForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            img = (request.FILES.get('criminal_Img'))
            images= import_iter(img)
            
            return render(request,'result.html',{"images":images})

    else:
        form = CriminalForm()
        
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


def result(request):
    return render(request, 'result.html', {})
