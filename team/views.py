from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def manageplayer(request):
    return render(request,'manageplayer.html')

def addplayers(request):
    if request.method=='POST':
        name = request.POST.get('name')
        sports = request.POST.get('sports')
        position = request.POST.get('position')
        nationalteam = request.POST.get('nationalteam')
        club = request.POST.get('club')
        gameplayed = request.POST.get('gameplayed')
        newpoint = request.POST.get('newpoint')
        total = request.POST.get('newpoint')
        dreamteam = request.POST.get('dreamteam')
        captiancy = request.POST.get('captiancy')
        vicecaptiancy = request.POST.get('vicecaptiancy')
        if players.objects.filter(name=name,nationalteam=nationalteam,club=club).exists():
            messages.error(request,'The player already registered ')
            return redirect(reverse('addplayers'))
        players.objects.create(name=name,sports=sports,position=position,nationalteam=nationalteam,club=club,gameplayed=gameplayed,newpoint=newpoint,total=total,dreamteam=dreamteam,captiancy=captiancy,vicecaptiancy=vicecaptiancy)
        return redirect(reverse('manageplayer'))
    return render(request,'addplayers.html')