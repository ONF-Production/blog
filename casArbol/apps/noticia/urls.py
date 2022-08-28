from django.contrib import admin
from django.urls import include,path
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('noticias/<int:id>/', views.noticiasdetalle, name='noticiasdetalle')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
