from django.shortcuts import render
from .models import Post

post_p = Post.objects.all()

context = {
    'activationHome': "active",
    'posts': post_p

}


def home(request):
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about', 'activationAbout': "active"})


def posting(request):
    return render(request, 'blog/register.html', context)


def Post_blog(request):
    return render(request, 'blog/Post_blog.html', context)
