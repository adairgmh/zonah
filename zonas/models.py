from django.db import models

# Create your models here.
from django.db import models

class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    zona_horaria = models.CharField(max_length=50)  # Campo para la zona horaria

    def __str__(self):
        return self.nombre
