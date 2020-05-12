from django import forms

class CityNameForm(forms.Form):
    name = forms.CharField(max_length=200)

