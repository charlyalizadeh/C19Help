from django import forms
from .models import Profil, LinkCommande
from django.contrib.auth.models import User
from django.forms import formset_factory


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['adress']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class LinkCommandeForm(forms.ModelForm):
    class Meta:
        model = LinkCommande
        fields = ['quantity','product']




