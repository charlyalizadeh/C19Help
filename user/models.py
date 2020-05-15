from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone, formats
from django.utils.translation import gettext_lazy as _



class Profil(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    adress = models.CharField(max_length = 1000,verbose_name = "Adresse postale")
    postale_code = models.CharField(max_length = 6,verbose_name = "Code postale",null = True)

class Product(models.Model):
    name = models.CharField(max_length = 100,verbose_name = "Produit")
    def __str__(self):
        return self.name

class Commande(models.Model):
    profil = models.ForeignKey(Profil,on_delete = models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    class Status(models.TextChoices):
        CREATION = 'ICT',_('in creation')
        PREPARATION = 'IPP',_('in preparation')
        PROGRESS = 'IPG',_('in progress')
        DELIVERED = 'DEL',_('delivered')
    status = models.CharField(max_length=3,choices = Status.choices,default=Status.CREATION)
    def __str__(self):
        date = formats.date_format(self.date,"SHORT_DATETIME_FORMAT")
        description = "{0} \n {1}\n".format(self.profil.user.username,date)
        for c in LinkCommande.objects.filter(commande__pk = self.pk):
            description += c.__str__() + '\n'
        description = description[:-1]
        return description

class LinkCommande(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,null = True)
    quantity = models.PositiveIntegerField(verbose_name = "Quantité")
    commande = models.ForeignKey(Commande,on_delete = models.CASCADE,null = True)
    def __str__(self):
        return "{0} : {1}".format(self.product,self.quantity)


