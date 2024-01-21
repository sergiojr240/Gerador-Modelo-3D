from abc import ABC, abstractmethod

class Modelo3DBuilder(ABC):
    @abstractmethod
    def build_pontos_referencia(self):
        pass
    
    @abstractmethod
    def build_mascara_contorno(self):
        pass
    
    @abstractmethod
    def build_dimensoes_gerais(self):
        pass
    
    @abstractmethod
    def build_tipo_ortese(self):
        pass
    
    @abstractmethod
    def build_pontos_tratamento(self):
        pass

