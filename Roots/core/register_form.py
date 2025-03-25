from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


GROUP_CHOICES = [
        ("1AI", "1_A_infantil"),
        ("1BI", "1_B_infantil"),
        ("1CI", "1_C_infantil"),
        ("1DI", "1_D_infantil"),
        ("1EI", "1_E_infantil"),
        ("2AI", "2_A_infantil"),
        ("2BI", "2_B_infantil"),
        ("2CI", "2_C_infantil"),
        ("2DI", "2_D_infantil"),
        ("3AI", "3_A_infantil"),
        ("3BI", "3_B_infantil"),
        ("3CI", "3_C_infantil"),
        ("3DI", "3_D_infantil"),
        ("1AP", "1_A_primaria"),
        ("1BP", "1_B_primaria"),
        ("1CP", "1_C_primaria"),
        ("1DP", "1_D_primaria"),
        ("2AP", "2_A_primaria"),
        ("2BP", "2_B_primaria"),
        ("2CP", "2_C_primaria"),
        ("3AP", "3_A_primaria"),
        ("3BP", "3_B_primaria"),
        ("3CP", "3_C_primaria"),
        ("4AP", "4_A_primaria"),
        ("4BP", "4_B_primaria"),
        ("5AP", "5_A_primaria"),
        ("5BP", "5_B_primaria"),
        ("6AP", "6_A_primaria"),
        ("6BP", "6_B_primaria"),
    ]


class RegisterForm(UserCreationForm):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        min_length=3,
        max_length=100
    )
    last_name = forms.CharField(  # CORREGIDO: antes era last_name
        label="Apellidos",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
        min_length=3,
        max_length=100
    )
    alumns_group = forms.ChoiceField(
        choices=GROUP_CHOICES,
        label="Grupo de alumnos",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu email'}),
        min_length=3,
        max_length=100
    )

    class Meta:
        model = User
        fields = ["name", "last_name", "email", "alumns_group", "password1", "password2"]