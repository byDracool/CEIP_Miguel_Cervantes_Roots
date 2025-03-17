from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from .views import AlumnsList

urlpatterns = [
    path('', views.home, name = "home"),
    # path('logout/', views.user_logout, name='user_logout'),
    # path('logout/', views.logout, name="logout"),
    # path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('alumns_list/', AlumnsList.as_view(), name = "alumns_list"),
    path('alumns/', views.alumns, name = "alumns"),
    path('external_tests/', views.external_tests, name = "external_tests"),
    path('califications/', views.califications, name = "califications"),
    path('economy/', views.economy, name = "economy"),
    path('parents_contact/', views.parents_contact, name = "parents_contact"),
    path('accede/', views.accede, name = "accede"),
    path('incidences/', views.incidences, name = "incidences"),
]