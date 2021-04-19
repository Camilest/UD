from productos import *

def montura_decorator(raza):
    def super_Fabricas(cls):
        class SuperFabricas(cls):
            def crear_montura(self):
                if raza == "elfos":
                    return MonturaElfos()
        
        return SuperFabricas

    return super_Fabricas

def cuerpo_decorator(raza):
    def super_Fabricas(cls):
        class SuperFabricas(cls):
            def crear_cuerpo(self):
                if raza == "elfos":
                    return CuerpoElfos()
        return SuperFabricas

    return super_Fabricas

class Fabricas:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaHumanos(Fabricas):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabricas):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

@cuerpo_decorator("elfos")
@montura_decorator("elfos")
class FabricaElfos(Fabricas):
    def crear_arma(self):
        return ArmaElfos()

    def crear_escudo(self):
        return EscudoElfos()


    


