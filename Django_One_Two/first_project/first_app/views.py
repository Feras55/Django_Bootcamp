from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord, User

# Create your views here.


def index(request):
    my_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': my_list}
    return render(request, 'first_app/index.html', context=date_dict)


def my_help(request):
    my_dict = {'para1': "jinja2.constants.LOREM_IPSUM_WORDS",
               'para2': "This is paragraph two of the help page"
               }

    return render(request, 'first_app/help.html', context=my_dict)


def my_users(request):
    my_users_list = User.objects.order_by('first_name')
    users_dict = {'user_list': my_users_list}
    return render(request, 'first_app/users.html', context=users_dict)
