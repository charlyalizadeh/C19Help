from django import forms
from .models import Profil, LinkCommande
from django.contrib.auth.models import User
from django.forms import formset_factory


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'type' : 'password','placeholder' : 'Mot de passe'}))
    username = forms.CharField(widget = forms.TextInput(attrs={'type':'text','placeholder' : 'Pseudo'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'type':'text','placeholder' : 'Prénom'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'type':'text','placeholder' : 'Nom'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'type' : 'text','placeholder' : 'Email'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class ProfilForm(forms.ModelForm):
    adress = forms.CharField(widget = forms.TextInput(attrs = {'type' : 'text','placeholder' : 'Adresse'}))
    postale_code = forms.CharField(widget = forms.TextInput(attrs = {'type' : 'text', 'placeholder' : 'Code Postale'}))
    class Meta:
        model = Profil
        fields = ['postale_code','adress']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget = forms.TextInput(attrs = {'type' : 'text','placeholder' : 'Pseudo'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs = {'placeholder' : 'Mot de passe'}))

class LinkCommandeForm(forms.ModelForm):
    class Meta:
        model = LinkCommande
        fields = ['quantity','product']





