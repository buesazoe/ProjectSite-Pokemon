"""
URL configuration for ProjectSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from AppCardQuest import views
from AppCardQuest.views import HomePageView, TrainerList, PokemonList, CollectionList



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='base'),
    path('trainers/', TrainerList.as_view(), name='trainer'),
    path('pokemon/', PokemonList.as_view(), name='pokemon'),  # Add this line
    path('collections/', CollectionList.as_view(), name='collection'),  # Assuming you want a list of collections
]