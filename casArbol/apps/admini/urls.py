
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name= 'apps.admini'

urlpatterns = [
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)