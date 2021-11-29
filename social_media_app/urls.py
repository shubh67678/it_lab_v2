"""social_media_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from user_auth.views import *
from posts_and_like.views import *
from comments_and_follow.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout',LogoutView.as_view(),name='logout'),
    path('accounts/',include('allauth.urls')),
    path('',homePage,name='homePage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('user/<str:pk>',profilePage,name='profilePage'),
    path('user/friend_list/<str:pk>/',friend_list,name='friend_list'),
    path('updateProfileImage/',updateProfileImage,name='updateProfileImage'),
    path('makepost/',makepost,name='makepost'),
    path('make_a_comment/<int:pk>',make_a_comment,name='make_a_comment'),
    path('make_a_friend/<int:pk>',make_a_friend,name='make_a_friend'),
    path('comment/<int:pk>',makecomment,name='makecomment'),
    path('likeclicked/',likeclicked,name='likeclicked'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

