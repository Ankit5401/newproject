from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,  HttpResponse

# Create your views here.
def index (request):
    return HttpResponse ("this is home page")