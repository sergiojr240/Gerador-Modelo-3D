from django.db import models

class Modelo3D(models.Model):
    nome = models.CharField(max_length=255)

class Ortese(models.Model):
    modelo_3d = models.ForeignKey(Modelo3D, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
