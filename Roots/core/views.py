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
from django.contrib.auth.models import User


class AlumnList(LoginRequiredMixin, ListView):
    model = Alumn
    context_object_name = "alumn_list"
    template_name = 'core/alumn_list.html'

    def get_queryset(self):
        """Filter the list of students by name if a value has been entered in the search bar."""
        queryset = super().get_queryset()
        searched_value = self.request.GET.get('find_area', '').strip()

        if searched_value:
            queryset = queryset.filter(Nombre__icontains=searched_value)

        return queryset

    def get_context_data(self, **kwargs):
        """Add the total number of results and the searched value to the context"""
        context = super().get_context_data(**kwargs)
        context['count'] = context['alumn_list'].count()
        context['searched_value'] = self.request.GET.get('find_area', '').strip()
        return context


class AlumnDetail(LoginRequiredMixin, DetailView):
    model = Alumn
    context_object_name = "alumn"
    template_name = "core/alumn.html"


class AlumnFullViewDetail(LoginRequiredMixin, DetailView):
    model = Alumn
    context_object_name = "alumn_full_view"
    template_name = "core/alumn_full_view.html"


class AddAlumn(LoginRequiredMixin, CreateView):
    model = Alumn
    fields = '__all__'
    success_url = reverse_lazy("alumns_administration")

class EditAlumn(LoginRequiredMixin, UpdateView):
    model = Alumn
    fields = '__all__'
    template_name = "core/alumn_form.html"
    success_url = reverse_lazy("alumns_administration")


class DeleteAlumn(LoginRequiredMixin, DeleteView):
    model = Alumn
    context_object_name = "alumn"
    template_name = "core/alumn_confirm_delete.html"
    success_url = reverse_lazy("alumns_administration")


class TeachersList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "teachers_list"
    template_name = 'core/teachers_list.html'

    def get_queryset(self):
        """Filter the list of teachers by username if a value has been entered in the search bar."""
        queryset = super().get_queryset()
        searched_value = self.request.GET.get('find_area', '').strip()

        if searched_value:
            queryset = queryset.filter(username__icontains=searched_value)

        return queryset

    # def get_context_data(self, **kwargs):
    #     """Añade el número total de resultados y el valor buscado al contexto."""
    #     context = super().get_context_data(**kwargs)
    #     context['count'] = context['alumn_list'].count()
    #     context['searched_value'] = self.request.GET.get('find_area', '').strip()
    #     return context


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = "user"
    template_name = "core/teacher.html"


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


class EditUser(LoginRequiredMixin, UpdateView):
    model = User
    fields = '__all__'
    template_name = "core/user_form.html"
    success_url = reverse_lazy("teacher_management")


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = "user"
    template_name = "core/user_confirm_delete.html"
    success_url = reverse_lazy("teacher_management")


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
def alumns_administration(request):
    return render(request, "core/alumns_administration.html")

@login_required
def teacher_management(request):
    return render(request, "core/teacher_management.html")

@login_required
def register(request):
    return render(request, "registration/register.html")

@login_required
def edit_delete_user(request):
    teachers = User.objects.exclude(username="admin")
    return render(request, "core/edit_delete_user.html", {"teachers_list": teachers})

@login_required
def edit_delete_alumn(request):
    alumns = Alumn.objects.all()
    return render(request, "core/edit_delete_alumn.html", {"alumns_list": alumns})




