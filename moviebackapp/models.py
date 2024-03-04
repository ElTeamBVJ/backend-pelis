from django.db import models
from django.db import models
from django.contrib.auth.models import User as UserAuth
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError
class genero(models.Model):
    nombre = models.CharField(max_length=45)  

class pelicula(models.Model):
    nombre =  models.CharField(max_length=45)
    #le puse IntegerField porque el año es un numero.
    anio = models.IntegerField()
    url_img =  models.ImageField(null=True, blank=True)
    descripcion = models.TextField(max_length=500)
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, related_name='peliculas')
    

class usuario(models.Model):
    user = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    email = models.EmailField()
    avatar = models.CharField(max_length= 250)
    peliculas_vistas = models.ManyToManyField(pelicula)

    
class plataforma(models.Model):
    nombre =  models.CharField(max_length=45)
    peliculas = models.ManyToManyField(pelicula)
    
class detalle_pelicula(models.Model):
     clasificacion =  models.CharField(max_length=45)
     esVieja=  models.BooleanField()
     esPopular =  models.BooleanField()
     recibioPremios =  models.BooleanField()
     #En detalle pelicula hay un campo que indica a que pelicula pertenecen los detalles
     pelicula = models.OneToOneField(pelicula, on_delete=models.CASCADE)



  

# Create your models here.
