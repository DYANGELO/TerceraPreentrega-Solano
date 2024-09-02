"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from servicios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('juegos/list', views.juegos_list, name='juegos_list'),
    path('sorteos/list', views.sorteos_list, name='sorteos_list'),
    path('promociones/list', views.promociones_list, name='promociones_list'),
    path("", views.index, name='index'),
    path('juegos/create', views.juegos_create, name='juegos_create'),
    path('promociones/create', views.promociones_create, name='promociones_create'),
    path('sorteos/create', views.sorteos_create, name='sorteos_create'),
]
