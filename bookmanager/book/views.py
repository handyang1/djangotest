from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest


def index(request):

    return HttpResponse('OK')