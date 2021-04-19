class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "Arma de los Humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "Arma de los Orcos"

class ArmaElfos(Arma):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/arma.png"
        self.descripcion = "Arma de los Elfos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "Escudo  de los Humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "Escudo de los Orcos"

class EscudoElfos(Escudo):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/escudo.png"
        self.descripcion = "Escudo de los Elfos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaElfos(Montura):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/montura.jpg"
        self.descripcion = "Montura de los Elfos"

class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

class CuerpoElfos(Montura):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/cuerpo.png"
        self.descripcion = "Cuerpo de los Elfos"


    