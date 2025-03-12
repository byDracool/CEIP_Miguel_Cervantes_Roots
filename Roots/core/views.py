from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Alumn
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


class Login(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

#@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html', {})

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

