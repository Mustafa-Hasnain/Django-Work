from django.shortcuts import redirect, render
from form.models import Player, Score
from .form import playerform
# Create your views here.

def home(request):
    return render(request, 'index.html')

def player(request):
    if request.method == 'POST':
        name = request.POST['name']
        team = request.POST['team']
        table = Player(Name=name, team=team)
        table.save()
        redirect('form/')
    else:
        return render(request, 'index.html')