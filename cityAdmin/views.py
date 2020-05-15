from django.shortcuts import render,redirect
from .forms import CityNameForm, ChangeDurationForm
from geopy.geocoders import Nominatim
from user.models import Profil,LinkCommande,Commande,Product
import unicodedata
from django.core import serializers
from django.utils import timezone
import json
import plotly.graph_objects as go
import plotly

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def isNumber(string):
    for i in string:
        if not i.isdigit():
            return False
    return True

def getCode(geo_tuple):
    temp = geo_tuple.split(',')
    for i in temp:
        i = i.strip()
        if len(i) == 5 and isNumber(i):
            return i

def getCommande(postale_code,geolocator):
    commandes = []
    coord = []
    for c in Commande.objects.all():
        location = geolocator.geocode(c.profil.adress + ' ' + c.profil.postale_code)
        lat = location.latitude
        lgt = location.longitude
        if postale_code == c.profil.postale_code:
            coord.append((lat,lgt))
            commandes.append(c.__str__().split('\n'))
    return commandes,coord 

def get_nbVente(product_name,days):
    link_commandes = []
    for l in LinkCommande.objects.filter(product__name=product_name):
        if (timezone.now()-l.commande.date).total_seconds()/(60*60*24)<days:
            link_commandes.append(l)
    quantity_sold = 0
    for l in link_commandes:
        quantity_sold += l.quantity
    return quantity_sold

def get_allName_Product():
    names = []
    for p in Product.objects.all():
        names.append(p.name)
    return names

def home(request):
    return render(request,'cityAdmin/home.html',locals())

def search_commande(request):
    if request.method == 'POST':
        form = CityNameForm(request.POST)
        if form.is_valid():
            postale_code = form.cleaned_data['postale_code']
            return redirect('menu_city',code = postale_code)
    else:
        form = CityNameForm()
    return render(request,'cityAdmin/search_commande.html',locals())

def menu_city(request,code):
    return render(request,'cityAdmin/menu_city.html',locals())

def map(request,code):
    geolocator = Nominatim(user_agent = "C19Help")
    commandes,coord = getCommande(code,geolocator)
    coordJson = json.dumps(dict(coord))
    return render(request,'cityAdmin/map.html',{"coord":coordJson,"commandes":commandes})

def commande_summary(request,postale_code):
    if request.method == "POST":
        form = ChangeDurationForm(request.POST)
        if form.is_valid():
            duration_type = int(form.cleaned_data["duration_type"])
            quantity = form.cleaned_data["quantity"]
            nb_days = quantity * duration_type
            print(nb_days,type(nb_days))
            names = get_allName_Product()
            nbVentes = [get_nbVente(n,nb_days) for n in names]
            fig = go.FigureWidget(data=go.Bar(x=names,y=nbVentes)) 
            graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
    else :
        form = ChangeDurationForm()
    return render(request,'cityAdmin/commande_summary.html',locals())

