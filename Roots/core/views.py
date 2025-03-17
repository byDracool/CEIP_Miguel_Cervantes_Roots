from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Alumn
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AlumnsList(ListView):
    model = Alumn
    context_object_name = "alumns_list"


@login_required
def home(request):
    return render(request, "core/home.html")

@login_required
def alumns(request):
    alumns_list = Alumn.objects.all()
    return render(request, "core/alumns.html", {"alumns": alumns_list})

@login_required
def external_tests(request):
    return render(request, "core/external_tests.html")

@login_required
def califications(request):
    return render(request, "core/califications.html")

@login_required
def economy(request):
    return render(request, "core/economy.html")

@login_required
def parents_contact(request):
    return render(request, "core/parents_contact.html")

@login_required
def accede(request):
    return render(request, "core/accede.html")

@login_required
def incidences(request):
    return render(request, "core/incidences.html")




