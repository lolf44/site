from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from blog.models import Post
from django.contrib.auth import login

post_p = Post.objects.all()

context = {
    'activationHome': "active",
    'posts': post_p
}


#TODO: add if user already exist
def register(request):
    urlChanger = 'users/register.html'
    form = UserCreationForm()

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

    renderForm = {'form': form, 'activationRegister': 'active'}
    return render(request, urlChanger, renderForm)

def Login(request):
    login_page = 'users/login.html'
    if request.method  == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(user)
    else:
        form = AuthenticationForm(data=request.POST)

        #redirecet to blog post
        # TODO: stay logged in
        #return HttpResponseRedirect('../')
    return render(request, 'templates/login.html', {'form': form})
