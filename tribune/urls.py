"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path(r'',include('news.urls')),
    re_path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    # path('accounts/login/', views.LoginView.as_view()),
    re_path(r'^login$', views.LoginView.as_view(template_name='django_registration/login.html')),
    re_path(r'^logout/$', views.LogoutView.as_view(next_page='/')), 
]
