from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Alumn
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TeachersList(LoginRequiredMixin, ListView):
    model = Alumn #ESTO HAY QUE CAMBIARLO POR EL USUARIO PERSONALIZADO
    context_object_name = "teachers_list"
    template_name = 'core/teachers_list.html'


class AlumnList(LoginRequiredMixin, ListView):
    model = Alumn
    context_object_name = "alumn_list"
    template_name = 'core/alumn_list.html'

    def get_queryset(self):
        """Filtra la lista de alumnos por nombre si se ha introducido un valor en el buscador."""
        queryset = super().get_queryset()
        searched_value = self.request.GET.get('find_area', '').strip()

        if searched_value:
            queryset = queryset.filter(Nombre__icontains=searched_value)

        return queryset

    def get_context_data(self, **kwargs):
        """Añade el número total de resultados y el valor buscado al contexto."""
        context = super().get_context_data(**kwargs)
        context['count'] = context['alumn_list'].count()
        context['searched_value'] = self.request.GET.get('find_area', '').strip()
        return context


# class AlumnList(LoginRequiredMixin, ListView):
#     model = Alumn
#     context_object_name = "alumn_list"
#     template_name = 'core/alumn_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#     #     context['alumn_list'] = context['alumn_list'].filter(Grupo=self.request.user)
#         context['count'] = context['alumn_list'].count()
#
#         finded_value = self.request.GET.get('find_area') or ''
#         if finded_value:
#             context['alumn_list'] = context['alumn_list'].filter(Nombre__icontains = finded_value)
#             context['finded_value'] = finded_value
#         return context


class AlumnDetail(LoginRequiredMixin, DetailView):
    model = Alumn
    context_object_name = "alumn"
    template_name = "core/alumn.html"


class AddAlumn(LoginRequiredMixin, CreateView):
    model = Alumn
    fields = '__all__'
    success_url = reverse_lazy("administration")

class EditAlumn(LoginRequiredMixin, UpdateView):
    model = Alumn
    fields = '__all__'
    success_url = reverse_lazy("administration")


class DeleteAlumn(LoginRequiredMixin, DeleteView):
    model = Alumn
    context_object_name = "alumn"
    success_url = reverse_lazy("administration")


class UserRegister(LoginRequiredMixin, FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = False
    success_url = reverse_lazy('teacher_management')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super().form_valid(form)


@login_required
def home(request):
    return render(request, "core/home.html")

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

@login_required
def administration(request):
    return render(request, "core/administration.html")

@login_required
def teacher_management(request):
    return render(request, "core/teacher_management.html")

@login_required
def register(request):
    return render(request, "registration/register.html")




