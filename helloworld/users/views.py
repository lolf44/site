from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from blog.models import Post
from django.contrib.auth import login
from .models import User

error_message=False

user_objects = User.objects.all()

User_context = {
    'user_info': user_objects,
    'activationProfile': 'active'
}

def Register(request):
    view_html = 'users/register.html'
    form = UserCreationForm()
    error_message=False
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        print(request.POST)
        if f.is_valid():
            f.save()
            login(request, user)
            print(user)
            return HttpResponseRedirect('../')
        else:
            print("it didnt work")
            error_message=True
            return HttpResponseRedirect('../error_register/')
    renderForm = {'form': form, 'activationRegister': 'active'}
    return render(request, view_html ,renderForm)

def Login(request):
    redirect = False
    login_page = 'users/login.html'
    if request.method  == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(user)
            redirect = True
            return HttpResponseRedirect('../')
    else:
        form = AuthenticationForm(data=request.POST)
    #while request is False:
    error_message=True
    return render(request, login_page, {'form': form, 'activationLogin': 'active'}) 

def Error_register(request):
    error_page = 'users/error_register.html'
    return render(request, error_page)    

def UserProfile(request):
    page_template = 'users/profile.html'
    return render(request, page_template, User_context)