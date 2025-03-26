from django.contrib import admin
from .models import Alumn, User
import data_wizard

# Register your models here.
admin.site.register(Alumn)
data_wizard.register(Alumn)
admin.site.register(User)
data_wizard.register(User)