class CajaFuerte():
    def __init__(self, combinacion, cantidad_acumulada):
        self.combinacion = combinacion
        self.cantidad_acumulada = cantidad_acumulada
        self.abierta = False

    def cerrarCajaFuerte(self):
        self.abierta = False
        
    def abrirCajaFuerte(self, combinacion):
        if self.combinacion == combinacion:
            self.abierta = True
        else:
            print("La combinacion no es la correcta")

    def meterDinero(self, cantidad, combinacion):
        self.abrirCajaFuerte(combinacion)
        if self.abierta == True:
            self.cantidad_acumulada = self.cantidad_acumulada + cantidad
            self.cerrarCajaFuerte()
            print("Se metieron " + str(cantidad) + " pesos")

    def sacarDinero(self, cantidad, combinacion):
        self.abrirCajaFuerte(combinacion)
        if self.abierta == True:
            self.cantidad_acumulada = self.cantidad_acumulada - cantidad
            self.cerrarCajaFuerte()

            print("Se retiraron " + str(cantidad) + " pesos")
    def saldoCaja(self, combinacion):
        self.abrirCajaFuerte(combinacion)
        if self.abierta == True:
            print("El saldo de mi caja fuerte es: " + str(self.cantidad_acumulada))


CajaFuerte_Mario = CajaFuerte(123456, 100)
CajaFuerte_Jose = CajaFuerte(0000, 200) 

CajaFuerte_Jose.meterDinero(50, 0000)
CajaFuerte_Jose.sacarDinero(80, 0000)
CajaFuerte_Jose.saldoCaja(0000)