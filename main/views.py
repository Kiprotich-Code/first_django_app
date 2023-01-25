from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'home.html')


def header(request):
    title = 'Main Page'

    return render(request, 
        'main/header.html',
        {'title':title})

def user_info(request):
    userinfo = {
        'username': 'Kiprotich',
        'country': 'Kenya',
    }

    context = {
        'userinfo': userinfo,
        'title': 'User Info Page'
    }

    return render(request, 
        'main/user_info.html',
        context)