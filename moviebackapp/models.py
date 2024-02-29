from django.db import models
from django.db import models
from django.contrib.auth.models import User as UserAuth
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError


class usuario(models.Model):
    user = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    avatar = models.CharField(max_length= 250)


class pelicula(models.Model):
    nombre =  models.CharField(max_length=45)
    anio = models.DateField()
    url_img =  models.ImageField(null=True, blank=True)
    descripcion = models.TextField(max_length=500)
  

# Create your models here.
