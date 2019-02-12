from random import randint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.utils import timezone
from .models import Req
from PIL import Image
import os


def index(request):
    return render(request, 'fileuploader/index.html');


def getReq(request):
    req = Req.objects.filter(pk=request.session['photoId']); req = req[0]; #Finds the uploaded image
    return req;


def upload(request):
    req = Req(image = request.FILES['fileToUpload']);
    req.save();
    request.session['photoId'] = req.id;        #Sets an id for the client

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def blackAndWhite(request):
    req = getReq(request);

    imageTmp = Image.open(req.image); #The image that should be edited
    imageTmp = imageTmp.convert('L'); #Black and White

    os.remove(req.image.path);
    imageTmp.save(req.image.path);

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def resize(request):
    req = getReq(request);

    imageTmp = Image.open(req.image);
    height = request.POST.get('height'); width =  request.POST.get('width');
    imageTmp = imageTmp.resize((int(width), int(height)));

    os.remove(req.image.path);
    imageTmp.save(req.image.path);
    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def crop(request):
    req = getReq(request);

    imageTmp = Image.open(req.image);
    left = int (request.POST.get('left'));
    upper = int (request.POST.get('upper'));
    right = int (request.POST.get('right'));
    lower = int (request.POST.get('lower'));
    imageTmp = imageTmp.crop ((left, upper, right, lower));

    os.remove(req.image.path);
    imageTmp.save(req.image.path);
    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def rotate(request):
    req = getReq(request);

    imageTmp = Image.open(req.image);
    degree = request.POST.get('degree');
    imageTmp = imageTmp.rotate((int(degree)));

    os.remove(req.image.path);
    imageTmp.save(req.image.path);
    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })


def share(request):
    if request.method == "POST":
        req = getReq(request);
        req.share = True;
        req.pubDate = timezone.now(); #Sets the publishing date and time
        req.save();

    shared = Req.objects.filter(share=True).order_by('-pubDate'); #Sort
    return render(request, 'fileuploader/shared.html', {
        'shared': shared, 'request': request,
    })
