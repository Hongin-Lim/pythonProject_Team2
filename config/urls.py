"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import hplace.views
import comment.views
import post_list.views
import post.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', hplace.views.register),
    path('posts/', hplace.views.posts),
    path('update/<int:bid>', hplace.views.update),
    path('read/<int:bid>', hplace.views.read),
    path('delete/<int:bid>', hplace.views.delete),
    path('home/', hplace.views.home),
    path('like/', hplace.views.like),

    path('hplace/', post.views.main_post),
    path('test/', hplace.views.test),


    path('comment/register/<int:bid>', comment.views.register),

    path('user/login', user.views.userlogin),
    path('user/signup', user.views.signup),
    path('user/logout', user.views.userlogout),
    path('main_post', post.views.main_post),
    path('post_list/', post_list.views.post_list),
]
