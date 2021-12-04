from django.shortcuts import render, redirect 
from .models import Wizard

def index(request):
    context = {
        'all_wizards': Wizard.objects.all()
    }
    return render(request, 'index.html', context)