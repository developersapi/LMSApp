from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import CertificadoView
from . import views

urlpatterns=[
    path('certificado/', CertificadoView.as_view(), name='certificado')]
    