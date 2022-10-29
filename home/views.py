from base64 import encode
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError, JsonResponse
from django.conf import settings
from home.models import dataModel
from home import *
import cv2 as cv
import os,hashlib,time

def index(request):
    context = {"a": ""}
    return render(request, 'index.html', context)

def defaultMsg(request):
    context = {"a": ""}
    return render(request, 'message.html', context)

def saveDetails(request):
    print(request)
    if request.method == 'POST':
        data = dataModel()
        data.fname = request.POST.get('firstName')
        data.lname = request.POST.get('lastName')
        data.phone = request.POST.get('phoneNumber')
        print(data)
        data.save()
    context = {"a": "Data submitted"}
    return render(request, 'index.html', context)


def addBorder(frame):
    frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('./home/haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(frame_grey, 1.1, 3)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    print(len(faces_rect))
    output_frame = {'frame': frame, 'faces': faces_rect}
    return output_frame


def displayVideo():
    camera = cv.VideoCapture(0)
    while True:
        result, frame = camera.read()

        flag, encodedFrame = cv.imencode('.jpg', frame)

        encodedFrame = encodedFrame.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + encodedFrame + b'\r\n\r\n')


def index2(request):
    return StreamingHttpResponse(displayVideo(),content_type='multipart/x-mixed-replace;boundary=frame')
    

def captureImage(request):
    camera = cv.VideoCapture(0)
    result, frame = camera.read()

    file_path = os.path.join(settings.MEDIA_ROOT,hashlib.sha1(frame).hexdigest()[:10] + '.jpg')
    cv.imwrite(file_path, frame)


def detectFace(request):
    context = {"msg": "Face Detected!", "img": ""}
    camera = cv.VideoCapture(0)
    result, frame = camera.read()
    if result:
        output_frame = addBorder(frame)

    if len(output_frame['faces']) == 0:
        camera.release()
        cv.destroyAllWindows()
        context['msg'] = "No faces found"
        return render(request, 'message.html', context)

    (flag,encodedImage) = cv.imencode('.jpg', output_frame['frame'])

    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


    file_path = os.path.join(settings.MEDIA_ROOT,hashlib.sha1(frame).hexdigest()[:10] + '.jpg')
    context['img'] = file_path
    print(file_path)
    cv.imwrite(file_path, frame)

    data = dataModel()
    data.img = file_path
    data.save()

    camera.release()
    cv.destroyAllWindows()
    return render(request, 'message.html', context)

# Create your views here.
