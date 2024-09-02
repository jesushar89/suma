class OperacionesAritmeticas():
    def calcularSuma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def leerSumando(self):
        sumando1 = int(input('Primer sumando: '))
        sumando2 = int(input('Segundo sumando: '))
        return sumando1, sumando2

if __name__ == '__main__':
    operacion = OperacionesAritmeticas()
    sumando1, sumando2 = operacion.leerSumando()
    print(f"{sumando1} + {sumando2} = {operacion.calcularSuma(sumando1, sumando2)}")