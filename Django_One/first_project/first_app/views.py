from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello, i am from first_app/index.html views.py !"}
    return render(request, 'first_app/index.html', context=my_dict)


def my_help(request):
    my_dict = {'para1': "jinja2.constants.LOREM_IPSUM_WORDS",
               'para2': "This is paragraph two of the help page"
               }

    return render(request, 'first_app/help.html', context=my_dict)
