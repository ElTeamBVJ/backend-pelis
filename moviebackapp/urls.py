from moviebackapp import views
from moviebackapp.views import *
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio,name='inicio'),
    path('test/', views.test,name='test'),
    path('plataform/', views.plataform,name='plataform'),
    path('results/',views.results,name='results'),
    path('login/',views.login_request,name="login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',views.register, name="register"),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name="logout"),
]
