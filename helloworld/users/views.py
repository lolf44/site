from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post


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
            return HttpResponseRedirect('../')
        else:
            print("it didnt work")

    renderForm = {'form': form, 'activationRegister': 'active'}
    return render(request, urlChanger, renderForm)

def login(request):
    login_page = 'users/login.html'
    return  render(request, login_page)


