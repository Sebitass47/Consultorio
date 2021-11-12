from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from tinymce import models as tinymce_models

# Create your models here.
class Doctor(AbstractUser):
    pass


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    historial = tinymce_models.HTMLField(blank=True)

    def __str__(self):
        return f"Nombre del paciente: {self.nombre} Correo: {self.correo}"


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = tinymce_models.HTMLField()
    imagen = models.ImageField(upload_to="imagenes")
    creador = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="posts_doctor")
    fecha = models.DateField()

    def __str__(self):
        return f"El titulo del post es: {self.titulo} creado por: {self.creador}"


class Promociones(models.Model):
    promocion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="promociones")

    def __str__(self):
        return f"Promocion {self.promocion}"


class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="paciente_cita")
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"El paciente {self.paciente} tiene cita el día {self.fecha} a las {self.hora}"


class HorariosTrabajo(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return f"Horario de cita: {self.hora}"