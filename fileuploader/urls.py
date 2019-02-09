from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('blackandwhite/', views.blackAndWhite, name='blackandwhite'),
    path('resize/', views.resize, name='resize'),
    path('crop/', views.crop, name='crop'),
    path('rotate/', views.rotate, name='rotate'),
    path('share/', views.share, name='share'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
