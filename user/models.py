from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Profil(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    adress = models.CharField(max_length = 1000)

class Product(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class LinkCommande(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,null = True)
    profil = models.ForeignKey(Profil,on_delete = models.CASCADE,null = True)
    date = models.DateTimeField(default = timezone.now)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.quantity,self.product,self.profil.user.username,self.date)


