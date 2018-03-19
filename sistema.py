#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado con Python3.
Clases necesarias para realizar las operaciones de la calculadora.

Autor: Rodríguez Hernández Josué Iván
Última modificación: Marzo 2018
"""

class Numero:
    """
    Clase Numero
    Contiene todos los elementos necesarios para operar con los números fácilmente.

    Atributos:
    valor -- Valor actual del número
    editado -- Indica sí el número ya fue editado o no
    """

    def __init__(self):
        """Constructor Clase: Numero"""

        self.valor = 0
        self.editado = False

    # --- GET y SET de los atributos ---
    # Sí unos de los métodos "get" o "set" se debe definir también el otro método sino dará error
    @property # Método "get" de un atributo
    def valor(self): # Mismo nombre del atributo
        return self.__valor # Para hacer referencia a él se utiliza el "__"
    @valor.setter # Método "set" de un atributo
    def valor(self, v):
        self.__valor = round(v, 4) # Redondea un número de acuerdo a la longitud dada
        self.editado = True

    # --- Operaciones con el número ---
    def vaciar(self):
        """Vacia el número (lo deja sin valor)"""

        self.valor = 0
        self.editado = False

class Calculadora:
    """
    Clase Calculadora
    Contiene los métodos necesarios para realizar las operaciones básicas sin problemas.

    Atributos:
    num1 -- Instancia de "Numero"
    num2 -- Instancia de "Numero"
    resultado -- Resultado de las operaciones
    """

    def __init__(self):
        """Constructor Clase: Calculadora"""

        self.num1 = Numero()
        self.num2 = Numero()
        self.resultado = "0"

    # --- Operaciones y métodos de la calculadora ---
    def suma(self):
        """Suma los 2 números que se han guardado en el sistema"""

        res = self.num1.valor + self.num2.valor
        res = round(res, 4) # Redondeamos el resultado para que no salga de mucha longitud
        self.resultado = str(res)
        self.num1.valor = float(self.resultado) # Cómo solo tenemos un control para ingresar números necesarios respaldar la información

    def resta(self):
        """Resta los 2 números que se han guardado en el sistema"""

        res = self.num1.valor - self.num2.valor
        res = round(res, 4)
        self.resultado = str(res)
        self.num1.valor = float(self.resultado)

    def multiplicacion(self):
        """Multiplica los 2 números que se han guardado en el sistema"""

        res = self.num1.valor * self.num2.valor
        res = round(res, 4)
        self.resultado = str(res)
        self.num1.valor = float(self.resultado)

    def division(self):
        """Divide los 2 números que se han guardado en el sistema"""

        try:
            res = self.num1.valor / self.num2.valor
            res = round(res, 4)
            self.resultado = str(res)
            self.num1.valor = float(self.resultado)

        except ZeroDivisionError: # Sí divide el número entre 0
            self.num1.vaciar()
            self.num2.vaciar()
            self.resultado = 'INFINITO'

    def borrar(self):
        """Borra todos los datos actuales de la calculadora"""

        self.num1.vaciar()
        self.num2.vaciar()
        self.resultado = "0"
