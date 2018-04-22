from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'football/index.html')


def login(request):
	return render(request, 'football/login.html')