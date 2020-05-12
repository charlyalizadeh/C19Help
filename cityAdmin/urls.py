from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
         path('home/',views.home,name= 'homeCity'),
         path('map/<code>',views.map,name = 'map'),
         path('listCommande/<code>',views.listCommande,name='listCommande')
        ]
