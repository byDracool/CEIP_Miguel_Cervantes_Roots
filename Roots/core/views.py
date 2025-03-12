from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Alumn
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "core/home.html")

def alumns(request):
    alumns_list = Alumn.objects.all()
    return render(request, "core/alumns.html", {"alumns": alumns_list})

def external_tests(request):
    return render(request, "core/external_tests.html")

def califications(request):
    return render(request, "core/califications.html")

def economy(request):
    return render(request, "core/economy.html")

def parents_contact(request):
    return render(request, "core/parents_contact.html")

def accede(request):
    return render(request, "core/accede.html")


# class AlumnsList(ListView):
#     model = Alumn
#     context_object_name = "alumns_list"

