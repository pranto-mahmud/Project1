from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is 1st app/courses page.")
def about(request):
    return HttpResponse("This is 1st app/about page.")
def home(request):
    return HttpResponse("This is 1st app/home page.")