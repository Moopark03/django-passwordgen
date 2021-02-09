from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
     return render(request, 'generator/home.html')

def password(request):

     createdpassword = ''

     characters = list('abcdefghjklmnopqrstuvwxyz')
     if request.GET.get('uppercase'):
          characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('special'):
          characters.extend(list('!@#$%^&*()_+'))
     if request.GET.get('numbers'):
          characters.extend(list('0123456789'))

     length = int(request.GET.get('length', 12)) #request.GET.get('name of variable from the HTML page', default value if needed)

     for x in range(length):
          createdpassword += random.choice(characters)

     return render(request, 'generator/password.html', {'password':createdpassword})

def about(request):
     return render(request, 'generator/about.html')
