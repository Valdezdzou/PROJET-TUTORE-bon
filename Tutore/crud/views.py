from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from crud.models import Fichier
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import Fichierform
from .models import Fichier
import mimetypes
from wsgiref.util  import FileWrapper
from django.http import StreamingHttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os


def bas(request):
    fich = Fichier.objects.all()

    context = {
        'fich':fich,
    }
    return render(request,'crud/base.html',context)

def Accueil(request):
    fich= Fichier.objects.all()
    count=Fichier.objects.count()
    countU=User.objects.count()
    context = {

          'fich':fich,
          'count':count,
          'countU':countU

     }
    return render(request, 'crud/accueil.html',context)

def mesfichiers(request):
    fich= Fichier.objects.all()
    count=Fichier.objects.count()
    countU=User.objects.count()
    context = {
        'fich':fich,
        'count':count,
        'countU':countU
    }

    return render(request, 'crud/mesfichiers.html',context)

def listefichiers(request):
    toutfich= Fichier.objects.all()
    count=Fichier.objects.count()
    countU=User.objects.count()
    context = {

          'toutfich':toutfich,
          'count':count,
          'countU':countU

     }
    return render(request, 'crud/listefichier.html',context)


def modifier(request):
    fich = Fichier.objects.all()

    context = {
        'fich':fich,
    }
    return redirect(request, 'crud/mesfichiers.html',context)


def update(request,id):
    if request.method == "POST":
        Titre = request.POST.get('Titre')
        Auteur = request.POST.get('Auteur')
        nom = request.POST.get('nom_du_fichier')
        contributeur = request.POST.get('dernier_contributeur')
        datemodification = request.POST.get('date_de_modification')
        sujet = request.POST.get('sujet')
        description = request.POST.get('description')
        

        fich = Fichier(
            id = id,
            Titre = Titre,
            Auteur = Auteur,
            nom_du_fichier = nom,
            dernier_contributeur = contributeur,
            date_de_modification = datemodification,
            sujet = sujet,
            description = description,
        )
        fich.save()    
        return redirect('mesfichiers')
    

    return render(request, 'crud/mesfichiers.html')




def supprimer(request,id):
    fich = Fichier.objects.filter(id = id)
    fich.delete()
    context = {
        'fich':fich,
    }

    return redirect('mesfichiers')



#inscription
def Sign_Up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('connexion')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
  
    return render(request,'crud/inscription.html', context)


#connexion avec email
def connecter(request):
   if request.method == "POST": 
           username = request.POST.get("username")
           password = request.POST.get("password")

           user = authenticate(username=username, password=password)
           if user:
               login(request, user)
               return redirect('Accueil')
   return render(request,'crud/connexion.html')



#deconnexion de l'admin
def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')



def inscription(request):
    return render(request, 'crud/inscription.html')


def connexion(request):
    if request.method == "POST": 
           username = request.POST.get("username")
           password = request.POST.get("password")

           user = authenticate(username=username, password=password)
           if user:
               login(request, user)
               return redirect('Accueil')
    return render(request,'crud/connexion.html')


def recherche(request):
    return render(request,'crud/rechercheA.html')





def ADD(request):
  if request.method == "POST":
        Titre = request.POST.get('Titre')
        Auteur = request.POST.get('Auteur')
        nom = request.POST.get('nom_du_fichier')
        contributeur = request.POST.get('dernier_contributeur')
        datecreation = request.POST.get('date_de_creation')
        sujet = request.POST.get('sujet')
        description = request.POST.get('description')
        document = request.FILES['document']
 
        fich = Fichier(
            Titre = Titre,
            Auteur = Auteur,
            nom_du_fichier = nom,
            dernier_contributeur = contributeur,
            date_de_creation = datecreation,
            sujet = sujet,
            description = description,
            document = document
        )
        fich.save()    
        return redirect('mesfichiers')
  
    
  return render(request, 'crud/Accueil.html', )


def rechercheAvancee(request):
  toutfich = Fichier.objects.all()
  if request.method == "POST":
        Titre = request.POST.get('Titre')
        Auteur = request.POST.get('Auteur')
        nom = request.POST.get('nom_du_fichier')
        contributeur = request.POST.get('dernier_contributeur')
        sujet = request.POST.get('sujet')
        description = request.POST.get('description')
        toutfich = Fichier.objects.filter(
            Titre=Titre,
            Auteur=Auteur,
            nom_du_fichier=nom,
            dernier_contributeur=contributeur,
            sujet=sujet,
            description=description,
        )

        context = {
                'toutfich':toutfich,
          }
  
    
  return render(request, 'crud/listefichier.html',context )



def deconnecter(request):
    logout(request)
    return redirect('connecter')


