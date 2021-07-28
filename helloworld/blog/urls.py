from django.urls import path
from users import views
from . import views as blog_views

urlpatterns = [
    path('', blog_views.Home, name="blog-Home"),
    path('about/', blog_views.About, name="blog-About"),
    path('Post/', blog_views.Post, name="blog-Post"),
    path('register/', views.Register, name='blog-Register'),
    path('login/', views.Login, name='blog-Login'),
    #path('error_auth/', views.Error_auth, name='blog-Error_auth'),  
]