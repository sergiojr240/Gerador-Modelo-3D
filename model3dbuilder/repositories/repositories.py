from .models import Modelo3D, Ortese

class Repository:
    def save_modelo_3d(self, nome):
        return Modelo3D.objects.create(nome=nome)

    def save_ortese(self, modelo_3d, nome):
        return Ortese.objects.create(modelo_3d=modelo_3d, nome=nome)

