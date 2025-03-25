import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy
from .managers import UserManager
from django.db import models
from django.conf import settings


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


class User(AbstractBaseUser, PermissionsMixin):
    """Data model for custom user in system"""

    name = models.CharField(
        gettext_lazy("first_name"), max_length=30, blank=False, null=False
    )
    lastname = models.CharField(
        gettext_lazy("last_name"), max_length=30, blank=False, null=False
    )
    alumns_group = models.CharField(
        gettext_lazy("alumns_group"), choices=GROUP_CHOICES, max_length=10, blank=True, null=True
    )
    email = models.EmailField(gettext_lazy("email_address"), unique=True)
    date_joined = models.DateTimeField(gettext_lazy("date_joined"), auto_now_add=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text=gettext_lazy(
            "Designates wheter the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(gettext_lazy("active"), default=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "lastname"]

    class Meta:
        """Meta definitions for model"""

        verbose_name = gettext_lazy("user")
        verbose_name_plural = gettext_lazy("users")

    @property
    def full_name(self):
        """
        Returns the full name.
        """
        full_name = f"{self.name} {self.lastname}"
        return full_name.strip()

    def get_short_name(self):
        """
        Returns a short name for the user.
        """
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.full_name



class Alumn(models.Model):

    Grupo = models.CharField(choices=GROUP_CHOICES, max_length=3, blank=False)
    Nombre = models.CharField(max_length=200, blank=False, null=False)
    Fotografia = models.URLField(max_length=200, blank=True, null = True)
    gender_choices = [
        ("H", "Hombre"),
        ("M", "Mujer"),
        ("NA", "Sin especificar"),
    ]
    Sexo = models.CharField(choices=gender_choices, max_length=2, blank=False)
    Tutor_a = models.ForeignKey(settings.AUTH_USER_MODEL, null = False, blank=False, on_delete=models.DO_NOTHING)
    Observaciones = models.TextField(max_length=300, blank=True, null=True)
    external_tests_choices = [
        ("PET", "PET"),
        ("KET", "KET"),
        ("None", "None"),
    ]
    PET_KET = models.CharField(choices=external_tests_choices, max_length=4, blank=True, default="")
    Calificaciones = models.JSONField(default=dict, blank=True, null=True)
    Telefono_contacto_padre = models.PositiveIntegerField(blank=True, null=True)
    Nombre_padre = models.CharField(max_length=30, blank=True, null=True)
    Email_padre = models.EmailField(blank=True, null=True)
    Telefono_contacto_madre = models.PositiveIntegerField(blank=True, null=True)
    Nombre_madre = models.CharField(max_length=30, blank=True, null=True)
    Email_madre = models.EmailField(blank=True, null=True)
    Personas_autorizadas_recogida = models.TextField(max_length=300, blank=True, null=True)
    comedor_choices = [
        ("SI", "SI"),
        ("NO", "NO"),
    ]
    Comedor = models.CharField(choices=comedor_choices, max_length=2, blank=False)
    Alergias = models.TextField(max_length=300, blank=True, null=True)
    IBAN = models.CharField(max_length=24, blank=True, null=True)
    Titular_cuenta = models.CharField(max_length=30, blank=True, null=True)
    Beca_comedor = models.CharField(choices=comedor_choices, max_length=2, blank=False)
    Pagos_pendientes = models.CharField(max_length=200, blank=True, null=True)
    accede_choices = [
        ("SI", "SI"),
        ("NO", "NO"),
    ]
    Adhesion_Accede = models.CharField(choices=accede_choices, max_length=2, blank=False)
    Senal_Accede = models.CharField(choices=accede_choices, max_length=2, blank=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ["Grupo", "Nombre"]


