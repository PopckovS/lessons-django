from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('777');
    print(request);
    print('777');
    return HttpResponse("Hello, world. You're at the polls index.")
