from django.urls import path
from . import views
from .views import Login
from django.contrib.auth.views import LogoutView
# from .views import AlumnsList

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', Login.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('alumns/', views.alumns, name = "alumns"),
    path('external_tests/', views.external_tests, name = "external_tests"),
    path('califications/', views.califications, name = "califications"),
    path('economy/', views.economy, name = "economy"),
    path('parents_contact/', views.parents_contact, name = "parents_contact"),
    path('accede/', views.accede, name = "accede"),
    # path('alumns_list/', AlumnsList.as_view(), name = "alumns_list"),
]