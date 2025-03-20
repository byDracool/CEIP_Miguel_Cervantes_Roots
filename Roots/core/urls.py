from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
from .views import AlumnList, AlumnDetail, AddAlumn, EditAlumn, DeleteAlumn, TeachersList, UserRegister, EditUser, DeleteUser, UserDetail

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('alumn_list/', AlumnList.as_view(), name = "alumn_list"),
    path('alumn/<int:pk>/', AlumnDetail.as_view(), name = "alumn"),
    path('add_alumn/', AddAlumn.as_view(), name = "add_alumn"),
    path('edit_alumn/<int:pk>/', EditAlumn.as_view(), name = "edit_alumn"),
    path('delete_alumn/<int:pk>/', DeleteAlumn.as_view(), name = "delete_alumn"),
    path('external_tests/', views.external_tests, name = "external_tests"),
    path('califications/', views.califications, name = "califications"),
    path('economy/', views.economy, name = "economy"),
    path('parents_contact/', views.parents_contact, name = "parents_contact"),
    path('accede/', views.accede, name = "accede"),
    path('incidences/', views.incidences, name = "incidences"),
    path('alumns_administration/', views.alumns_administration, name = "alumns_administration"),
    path('teacher_management/', views.teacher_management, name = "teacher_management"),
    path('teachers_list/', TeachersList.as_view(), name = "teachers_list"),
    path('register/', UserRegister.as_view(), name = "register"),
    path('user/<int:pk>/', UserDetail.as_view(), name="user"),
    path('edit_delete_user/', views.edit_delete_user, name = "edit_delete_user"),
    path('edit_user/<int:pk>/', EditUser.as_view(), name = "edit_user"),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name = "delete_user"),
]