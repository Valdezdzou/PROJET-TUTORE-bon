"""
URL configuration for projtuto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path 
from crud.views import mesfichiers, recherche, listefichiers, bas, ADD, modifier, update, supprimer, inscription, connexion, connecter, Sign_Up, login, Logout_admin, logout, Accueil, rechercheAvancee, deconnecter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mesfichiers', mesfichiers, name='mesfichiers'),
    path('base', bas, name='bas'),
    path('recherche', recherche, name='recherche'),
    path('listefichiers', listefichiers, name='listefichiers'),
    path('add',ADD, name='ADD'),
    path('',connecter, name='connecter'),
    path('Accueil/',Accueil, name='Accueil'),
    path('modifier',modifier, name='modifier'),
    path('update/<str:id>',update, name='update'),
    path('supprimer/<str:id>',supprimer, name='supprimer'),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('connecter/', connecter, name='connecter'),
    path('Sign_Up/', Sign_Up, name='Sign_Up'),
    path('login/', login, name='login'),
    path('Logout_admin/', Logout_admin, name='Logout_admin'),
    path('logout/', logout, name='logout'),
    path('Avancée/', rechercheAvancee, name='rechercheAvancee'),
    path('decon/', deconnecter, name='deconnecter'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)