from django.shortcuts import render,redirect
from .forms import CityNameForm 
from geopy.geocoders import Nominatim
from user.models import Profil,LinkCommande
import unicodedata
from django.core import serializers
import json

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
            print(i)
            return i

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = CityNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect('map',code = name)
    else:
        form = CityNameForm()
    return render(request,'cityAdmin/home.html',locals())

def map(request,code):
    geolocator = Nominatim(user_agent = "C19Help")
    coord = []
    commandes = []
    for c in LinkCommande.objects.all():
        location = geolocator.geocode(c.profil.adress)
        postale_code = getCode(location.raw['display_name']) 
        lat = location.latitude
        lgt = location.longitude
        if code == postale_code and (lat,lgt) not in coord:
            coord.append((lat,lgt))
            commandes.append(c.__str__().split(','))
    coordJson = json.dumps(dict(coord))
    return render(request,'cityAdmin/map.html',{"coord":coordJson,"commandes":commandes})

def listCommande(request,code):
    geolocator = Nominatim(user_agent = "C19Help")
    commandes = []
    for c in  LinkCommande.objects.all():
        location = geolocator.geocode(str(c.profil.adress))
        postale_code  = getCode(location.raw['display_name'])
        if code == postale_code: 
            commandes.append(c.__str__())
    return render(request,'cityAdmin/listCommande.html',locals())




    


