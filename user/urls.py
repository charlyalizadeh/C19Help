from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
        path('suscribe/',views.suscribe,name= 'suscribe'),
        path('connexion/',views.connexion,name= 'connexion'),
        path('deconnexion/',views.deconnexion,name = 'deconnexion'),
        path('commande/',views.commande,name = 'commande'),
        path('home/',views.home,name='user_home'),
        path("end_commande/<str:username>",views.end_commande,name="end_commande"),
        path("account_infos",views.account_infos,name="account_infos"),
        path("delete_linkcommande/<int:pk_link_commande>",views.delete_linkcommande,name="delete_linkcommande")
        ]
