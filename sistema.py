class Numero:

    def __init__(self):
        self.valor = 0
        self.lleno = False

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, v):
        self.__valor = round(v, 4)
        self.lleno = True

    def vaciar(self):
        self.valor = 0
        self.lleno = False


class Calculadora:

    def __init__(self):
        self.num1 = Numero()
        self.num2 = Numero()
        self.resultado = 0.0

    def suma(self):
        res = self.num1.valor + self.num2.valor
        res = round(res, 4)
        self.resultado.valor = str(res)
        self.num1.valor = float(self.resultado.valor)

    def resta(self):
        res = self.num1.valor - self.num2.valor
        res = round(res, 4)
        self.resultado.valor = str(res)
        self.num1.valor = float(self.resultado.valor)

    def multiplicacion(self):
        res = self.num1.valor * self.num2.valor
        res = round(res, 4)
        self.resultado.valor = str(res)
        self.num1.valor = float(self.resultado.valor)

    def division(self):
        if self.num2 != 0:
            res = self.num1.valor / self.num2.valor
            res = round(res, 4)
            self.resultado.valor = str(res)
            self.num1.valor = float(self.resultado.valor)
        else:
            self.resultado.valor = 'INFINITO'
            self.borrar()

    def igual(self, anterior_operacion):
        pass

    def borrar(self):
        self.num1.vaciar()
        self.num2.vaciar()
        self.resultado.vaciar()
