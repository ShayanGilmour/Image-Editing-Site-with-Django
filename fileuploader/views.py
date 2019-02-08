from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import Req


def index(request):
#    return render(request, 'fileuploader/index.html', {
#        'lst': [1, 2, 3, 4, 5, 'salam'], 'lst2':[10, 11, 12, 13],
#    })
    return render(request, 'fileuploader/index.html');


def upload(request):
#    fileName = default_storage.save('file', request.FILES['fileToUpload'])
#    path = "media/" + path;
    req = Req(image = request.FILES['fileToUpload']);
    req.save();

    return render(request, 'fileuploader/edit.html', {
        'req': req,
    })
#    return render(request, 'fileuploader/edit.html', {
#        'path': paths, })
