from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Proyecto(models.Model):

    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    link = models.URLField(max_length=256)
    pdf = models.FileField()
    foto = models.ImageField()
    email = models.EmailField()
    fecha_maxima = models.DateField(blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.titulo}'

class Trabajador(models.Model):

    PUESTO_CHOICES = [
    ('1', 'Obrero'),
    ('2', 'Maestro mayor'),
    ('3', 'Arquitecto'),
    ('4', 'Ingeniero'),
    ('5', 'Renderista'),
    ('6', 'Maquetista'),
    ('7', 'Otro'),
    ]

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.CharField(max_length=30)
    email = models.EmailField()
    cv = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg'])])
    puesto = models.IntegerField(choices=PUESTO_CHOICES)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Material(models.Model):

    nombre = models.CharField(max_length=40)
    numero = models.CharField(max_length=30)
    email = models.EmailField()
