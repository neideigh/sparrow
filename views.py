from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})


def ship(request):
	return render(request, 'ship.html', {})