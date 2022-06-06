from django.contrib import admin

# Register your models here.
from .models import Libro
from .models import Prestamo
from .models import Usuario

admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Usuario)


