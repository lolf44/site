from django.shortcuts import render
from .models import Post

post_p = Post.objects.all()

context = {
    'activationHome': "active",
    'posts': post_p
}

def Home(request):
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html', {'title': 'about', 'activationAbout': "active"})

def Post(request):
    return render(request, 'blog/Post.html', context)
