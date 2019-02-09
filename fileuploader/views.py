from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import Req
from PIL import Image
import os


def index(request):
    return render(request, 'fileuploader/index.html');


def upload(request):
    req = Req(image = request.FILES['fileToUpload']);
    req.save();
    request.session['photoId'] = req.id;        #Sets an id for the client

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def blackAndWhite(request):
    req = Req.objects.filter(pk=request.session['photoId']); req = req[0]; #Finds the uploaded image

    imageTmp = Image.open(req.image); #The image that should be edited
    imageTmp = imageTmp.convert('L'); #Black and White

    os.remove(req.image.path);
    imageTmp.save(req.image.path);

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })

def resize(request):
    req = Req.objects.filter(pk=request.session['photoId']); req = req[0]; #Finds the uploaded image
    imageTmp = Image.open(req.image); #The image that should be edited
    height = request.POST.get('height', '');
    width =  request.POST.get('width',  '');
    imageTmp = imageTmp.resize(( int(width), int(height) ));
    os.remove(req.image.path);
    imageTmp.save(req.image.path);
    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })
