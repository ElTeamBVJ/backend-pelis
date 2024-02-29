from multiprocessing import AuthenticationError
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import Template,Context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as UserAuthfrom
from  django.views.generic import TemplateView

def inicio(request):
    peliculas = pelicula.objects.all()
    print(peliculas)
    return render(request, 'index.html',{'peliculas':peliculas})

def test (request):
    return render(request,'test.html')

def plataform(request):
    return render(request,'plataform.html')

def random(request):
    return render (request,'random.html')

def results(request):
    return render(request, 'results.html')


def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            form.save()
            return render(req, "success.html", {"message": "Usuario creado"})

    else:
        form = UserCreationForm()

    return render(req, "register.html", {"form": form})


def login_request(req):
    form = UserCreationForm()

    if req.method == "POST":
        form = AuthenticationError(req, data=req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            passw = form.cleaned_data["password"]

            user = authenticate(username=username, password=passw)
            print(username, passw, user)
            if user is not None:
                login(req, user)
                return render(req, "login-suc.html", {"message": f"Welcome, {user}!"})

            else:
                return render(
                    req,
                    "login.html",
                    {"message": f"Error: el usaurio no existe", "form": form},
                )
        else:
            return render(
                req,
                "login.html",
                {"message": f"Error, datos incorrectos", "form": form},
            )
    form = AuthenticationForm()
    return render(req, "login.html", {"form": form})