from flask import Flask , render_template
from fabricas import *
from random import choice

app = Flask(__name__)

@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos(), FabricaElfos()]
    fabricas = [1,2,3]
    opcion = choice(fabricas)

    productos = []
    if opcion != 3:
        if opcion == 1:
            fabrica = FabricaHumanos()
        else:
            fabrica = FabricaOrcos()   
    else:
        fabrica = FabricaElfos()
        montura = fabrica.crear_montura()
        cuerpo = fabrica.crear_cuerpo()
        productos.append(montura)
        productos.append(cuerpo)

    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    
    productos.append(arma)
    productos.append(escudo)
    

    return render_template("productos.html", productos = productos)


if __name__ == '__main__':
    app.run(debug= True)