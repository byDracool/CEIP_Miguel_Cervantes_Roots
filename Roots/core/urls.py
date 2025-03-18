from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from .views import AlumnList, AlumnDetail, AddAlumn, EditAlumn, DeleteAlumn

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('alumn_list/', AlumnList.as_view(), name = "alumn_list"),
    path('alumn/<int:pk>/', AlumnDetail.as_view(), name = "alumn"),
    path('add_alumn/', AddAlumn.as_view(), name = "add_alumn"),
    path('edit_alumn/<int:pk>/', EditAlumn.as_view(), name = "edit_alumn"),
    path('delete_alumn/<int:pk>/', DeleteAlumn.as_view(), name = "delete_alumn"),
    # path('alumns/', views.alumns, name = "alumns"),
    path('external_tests/', views.external_tests, name = "external_tests"),
    path('califications/', views.califications, name = "califications"),
    path('economy/', views.economy, name = "economy"),
    path('parents_contact/', views.parents_contact, name = "parents_contact"),
    path('accede/', views.accede, name = "accede"),
    path('incidences/', views.incidences, name = "incidences"),
    path('administration/', views.administration, name = "administration"),
]