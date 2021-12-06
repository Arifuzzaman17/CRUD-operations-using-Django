from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=16)
    email = models.EmailField( max_length=254)
    id_no = models.IntegerField(max_length=8)