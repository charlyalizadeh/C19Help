from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profil,LinkCommande
from .forms import UserForm,ProfilForm,LinkCommandeForm,ConnexionForm
from django.contrib.auth import authenticate, login,logout
from django.forms import modelformset_factory
from geopy.geocoders import Nominatim
from django.views import View





def suscribe(request):
    formUser = UserForm(request.POST or None)
    formProfil = ProfilForm(request.POST or None)

    if formUser.is_valid() and formProfil.is_valid():
        #FORM USER
        username = formUser.cleaned_data['username']
        firstname = formUser.cleaned_data['first_name']
        lastname = formUser.cleaned_data['last_name']
        password = formUser.cleaned_data['password']
        email = formUser.cleaned_data['email']
        user = User.objects.create_user(username = username,first_name = firstname,last_name = lastname,password = password,email = email)
        adress = formProfil.cleaned_data['adress']
        Profil(user = user,adress = adress).save()
        login(request,user)
        return redirect(home)
    return render(request,'user/suscribe.html',locals())

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  
            if user:  
                login(request, user)  
                return redirect(home)
            else: 
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'user/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(home)

def home(request):
    isConnected = request.user.is_authenticated
    return render(request,'user/home.html',locals())

def go_admin(request):
    return redirect('cityAdmin:homeCity')

def commande(request):
    if request.method == "POST":
        form = LinkCommandeForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            product = form.cleaned_data['product']
            LinkCommande(quantity = quantity,product = product,profil = request.user.profil).save()
    else:
        form = LinkCommandeForm()
    return render(request, 'user/commande.html', locals())


