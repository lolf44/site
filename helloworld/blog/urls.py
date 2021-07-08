from django.urls import path
from users import views
from . import views as blog_views
urlpatterns = [
    path('', blog_views.home, name="blog-home"),
    path('about/', blog_views.about, name="blog-about"),
    path('Post_blog/', blog_views.Post_blog, name="blog-Post_blog"),
    path('register/', views.register, name='blog-register'),
    path('login/', views.Login, name='blog-login'),
]