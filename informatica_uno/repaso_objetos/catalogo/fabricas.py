from productos import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

class FabricaCompleta(Fabrica):
    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass

class FabricaElfos(FabricaCompleta):
    def crear_cuerpo(self):
        return Cuerpo()

    def crear_montura(self):
        return Montura()

    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()