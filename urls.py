from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('ship.html', views.ship, name="ship"),


]
