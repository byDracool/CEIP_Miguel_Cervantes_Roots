from django.contrib import admin
from .models import Alumn
import data_wizard

# Register your models here.
admin.site.register(Alumn)
data_wizard.register(Alumn)