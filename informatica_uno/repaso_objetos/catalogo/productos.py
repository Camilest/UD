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
        self.imagen = "imagenes/humanos/arma.jpg"
        self.descripcion = "Arma de los humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "Arma de los orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "Escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/Orcos/escudo.png"
        self.descripcion = "Escudo de los Orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumano(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/Humanos/escudo.png"
        self.descripcion = "Montura de los Humanos"

class MonturaOrco(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/Orcos/escudo.png"
        self.descripcion = "Montura de los Orcos"

class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)

class CuerpoHumano(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/Humanos/escudo.png"
        self.descripcion = "cuerpo de los humanos"

class CuerpoOrco(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/Orcos/escudo.png"
        self.descripcion = "Cuerpo de los Orcos"