from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'home.html')


def header(request):
    return render(request, 'main/header.html')

def user_info(request):
    return render(request, 'main/user_info.html')