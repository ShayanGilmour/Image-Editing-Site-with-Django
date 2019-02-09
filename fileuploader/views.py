from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import Req
from PIL import Image
import os


def index(request):
#    return render(request, 'fileuploader/index.html', {
#        'lst': [1, 2, 3, 4, 5, 'salam'], 'lst2':[10, 11, 12, 13],
#    })
    return render(request, 'fileuploader/index.html');


def upload(request):
#    fileName = default_storage.save('file', request.FILES['fileToUpload'])
#    path = "media/" + path;
    req = Req(image = request.FILES['fileToUpload']);
#    req.session;  #MAY be useless
    req.save();
    request.session['photoId'] = req.id;

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })
#    return render(request, 'fileuploader/edit.html', {
#        'path': paths, })

def blackandwhite(request):
    req = Req.objects.filter(pk=request.session['photoId']);
    req = req[0];

#    return render(request, 'fileuploader/debug.html', {
#        'req': req, 'request': request,
#    })

#    Req.objects.filter(pk=request.session['photoId']).delete();          # should be removed from the database?
    imageTmp = Image.open(req.image); #The image that should be edited
    imageTmp = imageTmp.convert('L');
#    imageTmp.save(req.image.url);
#    req.image = imageTmp;
#    Req.objects.filter(pk=request.session['photoId']).delete();
    os.remove(req.image.path);
    imageTmp.save(req.image.path);
#    imageTmp.save('/media/bullshit');
#    req.save();

    return render(request, 'fileuploader/edit.html', {
        'req': req, 'request': request,
    })
