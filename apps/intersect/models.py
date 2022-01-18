from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Intersect(models.Model):
    codigo_departamento = models.CharField("COD_DANE", max_length=2, validators=[MinLengthValidator(2)])
    nombre_departamento = models.CharField("Nombre Departamento", max_length=60)
    id_area = models.CharField("ID Area", max_length=10)
    nombre_area = models.CharField("Nombre Area", max_length=500)
    area_ha = models.FloatField("Area Ha")

    class Meta:
        ordering = ['id_area']

    def __str__(self):
        return f'{self.nombre_departamento} {self.nombre_area} {self.area_ha}'