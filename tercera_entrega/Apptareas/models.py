from django.db import models


class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    miembros = models.ManyToManyField(Miembro, related_name='proyectos')


class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
