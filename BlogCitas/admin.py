from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Post)
admin.site.register(Promociones)
admin.site.register(Citas)