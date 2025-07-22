from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')


from book.models import BookInfo
BookInfo.objects.filter(pub_date__year=1980)

BookInfo.objects.filter(id__gt=3)