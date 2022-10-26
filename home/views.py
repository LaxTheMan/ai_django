from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from home.models import samplemodel
from home import *
import cv2 as cv
import os

def index(request):
    context = {"a": ""}
    return render(request, 'index.html', context)

def defaultMsg(request):
    context = {"a": ""}
    return render(request, 'message.html', context)

def saveDetails(request):
    print(request)
    if request.method == 'POST':
        data = {}
        data['firstName'] = request.POST.get('firstName')
        data['lastName'] = request.POST.get('lastName')
        data['phone'] = request.POST.get('phoneNumber')
        print(data)
    context = {"a": "Data submitted"}
    return render(request, 'index.html', context)

def webcam(request):
    context = {"msg": "Camera was opened"}
    camera = cv.VideoCapture(0)
    result, frame = camera.read()

    if result:
        frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('./home/haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(frame_grey, 1.1, 3)
    print(len(faces_rect))
    if len(faces_rect) == 0:
        camera.release()
        cv.destroyAllWindows()
        return render(request, 'message.html', {"msg": "No faces found"})

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', frame)
    cv.moveWindow('Detected Faces', 0, 0)

    camera.release()
    cv.destroyAllWindows()
    return render(request, 'message.html', context)

def detectFace(request):
    context = {"msg": "Camera was opened"}
    camera = cv.VideoCapture(0)
    
    if not camera.isOpened():
        exit()
        return render(request, 'message.html', {"msg": "Cannot open camera"})

    while True:
        result, frame = camera.read()

        if not result:
            print('Cannot capture through camera')
            break
            
        frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('image', frame_grey)
        cv.moveWindow('image', 0, 0)

        if cv.waitKey(1) == ord('s'):
            break

    camera.release()
    cv.destroyAllWindows()
    return render(request, 'message.html', context)

# Create your views here.
