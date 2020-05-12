from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
        path('suscribe/',views.suscribe,name= 'suscribe'),
        path('connexion/',views.connexion,name= 'connexion'),
        path('deconnexion/',views.deconnexion,name = 'deconnexion'),
        path('commande/',views.commande,name = 'commande'),
        path('home/',views.home,name='home'),
        path('admin/',views.go_admin,name='go_admin')

        ]
