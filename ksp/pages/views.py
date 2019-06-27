from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path, include
from .forms import *
from pages.criminal_script.CriminalRecognition import *
import face_recognition
import time
from django.template import loader, Context


def base(request):
    form = CriminalForm()
    return render(request, 'index.html', {'form': form})


def import_iter(img):
    np_im = face_recognition.load_image_file(img)
    criminal_instance = CriminalRecognition()

    t = loader.get_template('result.html')
    c = Context()
    yield t.render()

    yield "<div class='container'><br><h1>Matched Images</h1><br><div style='width:1100px;display:flex; flex-wrap: wrap;'>"
    if criminal_instance.validator(np_im):
        print("check iter")
        import os
        filenames = (os.listdir("static/images/Test Images/"))
        for i in filenames:
            #print("static/images/Test Images/"+str(i))
            img2 = face_recognition.load_image_file(
                "static/images/Test Images/"+str(i))
            # print(img2)
            if criminal_instance.face_compare(np_im, img2):
                print("Matched image:  ", i)
                yield "<div class='img-uploader' style='height:300px; padding:20px;overflow-y:hidden'><img style='width:300px;float:left;' src='static/images/Test Images/"+i+"' alt="+i+" /></div>"
        yield "</div></div>"
    else:
        return HttpResponse('no face detected')


def criminal_view(request):

    if request.method == 'POST':
        form = CriminalForm(request.POST, request.FILES)

        if form.is_valid():
            img = (request.FILES.get('criminal_Img'))
            return HttpResponse(import_iter(img))
            #from PIL import Image
            #import numpy
            #im = Image.open(img)
            #np_im = numpy.array(im)
            # print(np_im)
            # np_im=face_recognition.load_image_file(img)
            # print(np_im)
            #criminal_instance = CriminalRecognition()
            # if criminal_instance.validator(np_im):
            #    print("in")
            #    import os
            #    filenames=(os.listdir("static/images/Test Images/"))
            #    for i in filenames:
            #        print("static/images/Test Images/"+str(i))
            #        img2=face_recognition.load_image_file("static/images/Test Images/"+str(i))
            #        #print(img2)
            #        if criminal_instance.face_compare(np_im,img2):
            #            print(i)

    else:
        form = CriminalForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')

# def gen():
#    frame = [1,2,3]
#    for i in frame:
#        yield { 'value' : i}


def result(request):
    if request.method == "POST":
        return HttpResponse(import_iter())
    else:
        return render(request, 'result.html', {'value': 10})
