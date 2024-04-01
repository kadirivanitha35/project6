from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rings(request):
    return HttpResponse('Gold rings are expensive')
