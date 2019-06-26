from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import path, include
from .forms import *
from pages.criminal_script.CriminalRecognition import *
import face_recognition

def base(request):
   form = CriminalForm()
   return render(request, 'index.html', {'form': form})


def criminal_view(request): 
  
    if request.method == 'POST': 
        form = CriminalForm(request.POST, request.FILES) 
  
        if form.is_valid():
            img=(request.FILES.get('criminal_Img'))
            
            #from PIL import Image
            #import numpy
            #im = Image.open(img)
            #np_im = numpy.array(im)
            #print(np_im)
            np_im=face_recognition.load_image_file(img)
            #print(np_im)
            criminal_instance = CriminalRecognition()
            if criminal_instance.validator(np_im):
                print("in")
                import os
                filenames=(os.listdir("Test Images/"))
                for i in filenames:
                    print("Test Images/"+str(i))
                    img2=face_recognition.load_image_file("Test Images/"+str(i))
                    #print(img2)
                    if criminal_instance.face_compare(np_im,img2):
                        print(i)

            else:
                return HttpResponse('no face detected')

            return redirect('success') 
    else: 
        form = CriminalForm() 
    return render(request, 'upload.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 