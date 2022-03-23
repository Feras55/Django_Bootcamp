from django.shortcuts import render, redirect
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app import forms


# Create your views here.


def index(request):
    # my_list = AccessRecord.objects.order_by('date')
    # date_dict = {'access_record': my_list}
    return render(request, 'first_app/index.html')


def my_help(request):
    my_dict = {'para1': "jinja2.constants.LOREM_IPSUM_WORDS",
               'para2': "This is paragraph two of the help page"
               }

    return render(request, 'first_app/help.html', context=my_dict)


def my_users(request):
    my_users_list = User.objects.order_by('first_name')
    users_dict = {'user_list': my_users_list}
    return render(request, 'first_app/users2.html', context=users_dict)


def sign_up(request):
    form = forms.NewUserForm()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)  # Save the info taken from the form
            return index(request)

        else:
            print("ERROR FORM INVALID")

    return render(request, "first_app/users.html", {'form': form})
