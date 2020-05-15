from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
         path('home/',views.home,name= 'city_home'),
         path('search_commandes',views.search_commande,name = 'search_commande'),
         path('map/<code>',views.map,name = 'map'),
         path('commande_summary/<postale_code>',views.commande_summary,name = 'commande_summary'),
         path('menu_city/<code>',views.menu_city,name='menu_city')
        ]
