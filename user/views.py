from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profil,LinkCommande,Commande
from .forms import UserForm,ProfilForm,LinkCommandeForm,ConnexionForm
from django.contrib.auth import authenticate, login,logout
from django.forms import modelformset_factory
from geopy.geocoders import Nominatim
from django.views import View





def suscribe(request):
    isConnected = request.user.is_authenticated
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
        postale_code = formProfil.cleaned_data['postale_code']
        Profil(user = user,adress = adress,postale_code = postale_code).save()
        login(request,user)
        return redirect(home)
    return render(request,'user/suscribe.html',locals())

def connexion(request):
    isConnected = request.user.is_authenticated
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
    isConnected = request.user.is_authenticated
    logout(request)
    return redirect(home)

def home(request):
    isConnected = request.user.is_authenticated
    return render(request,'user/home.html',locals())

def commande(request):
    isConnected = request.user.is_authenticated
    commande = ''
    username = request.user.username
    if request.method == "POST":
        commande = Commande.objects.filter(profil__user__username = username).filter(status = Commande.Status.CREATION)[0]
        form = LinkCommandeForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            product = form.cleaned_data['product']
            link_commandes = LinkCommande.objects.filter(commande__pk = commande.pk)
            product_in_commande = False
            for l in link_commandes:
                if l.product.name == product.name:
                    product_in_commande = True
                    break
            if not product_in_commande:
                LinkCommande(quantity = quantity,product = product,commande = commande).save()
    else:
        commande = Commande.objects.filter(profil__user__username = username).filter(status = Commande.Status.CREATION)
        if len(commande)==0:
            commande = Commande(profil = request.user.profil)
            commande.save()
        else:
            commande = commande[0]
        form = LinkCommandeForm()
    link_commandes = LinkCommande.objects.filter(commande__pk = commande.pk)
    return render(request, 'user/commande.html', locals())

def delete_linkcommande(request,pk_link_commande):
    link_commande = LinkCommande.objects.filter(pk = pk_link_commande)
    link_commande.delete()
    return redirect(commande)

def end_commande(request,username):
    commande =  Commande.objects.filter(profil__user__username = username).filter(status = Commande.Status.CREATION)[0]
    linkCommande = LinkCommande.objects.filter(commande__pk = commande.pk)
    if len(linkCommande)==0:
        commande.delete()
    else:
        commande.status = Commande.Status.PREPARATION
        commande.save()
    print(commande.status)
    return redirect(home)

def account_infos(request):
    profil = request.user.profil
    return render(request,'user/account_infos.html',locals()) 
    

