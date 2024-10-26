"""
URL configuration for projet project.

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
from django.urls import path
from blog.views import home, topics, topic, new_topic, new_entry, edit_entry, loginpage, logoutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    # la page d'acceuil
    path('', home, name="home"),
    # les éléments de ma page
    path('topics/', topics, name="topics"),
    # detail pour chaque sujet 
    path('topics/<int:topic_id>/', topic, name="topic"),
    # ajouter un nouveau sujet
    path('new_topic/', new_topic, name="new_topic"),
    # ajouter un nouveau élément pour chaque sujet
    path('new_entry/<int:topic_id>/', new_entry, name="new_entry"),
    # une page pour editer une entrée(entry)
    path('edit_entry/<int:entry_id>/', edit_entry, name="edit_entry"),
    # login page
    path('loginpage/', loginpage, name="loginpage"),
    #logout page 
    path("logoutpage/", logoutpage, name="logoutpage"),
]
