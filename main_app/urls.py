from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('index/', views.about ,name ='index'),
    path('finchs/', views.finchs_index, name='index')

]