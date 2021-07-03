from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('Post_blog/', views.Post_blog, name="blog-Post_blog"),
]