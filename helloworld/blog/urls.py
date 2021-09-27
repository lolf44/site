from django.urls import path
from users import views as user_views
from . import views as blog_views

urlpatterns = [
    path('', blog_views.Home, name="blog-Home"),
    path('about/', blog_views.About, name="blog-About"),
    path('Post/', blog_views.Post, name="blog-Post"),
    path('register/', user_views.Register, name='blog-Register'),
    path('login/', user_views.Login, name='blog-Login'),
    path('error_register/', user_views.Error_register, name='blog-Error_register'),  
]