from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import path
import requests
import sys
from subprocess import run,PIPE

# Create your views here.

class CertificadoView(TemplateView):
    template_name='certificado.html'



