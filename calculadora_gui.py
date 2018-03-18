#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado con Python 3.X y PyQt5
Calculadora simple con PyQt5

@author: josue
Última modificación: Febrero 2018
"""

from sistema import Calculadora
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QDesktopWidget, QLabel, QLineEdit

class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.sistema = Calculadora()
        self.operacion = ''
        self.operar = {
            '+':self.sistema.suma,
            '-':self.sistema.resta,
            '*':self.sistema.multiplicacion,
            '/':self.sistema.division
        }

        self.iniciar_basico()
        self.iniciar_controles()
        self.show()

    def iniciar_basico(self):
        self.setWindowTitle('Calculadora PyQt5')
        self.setWindowIcon(QIcon('img/icon.png'))
        self.resize(300, 230)
        self.setMaximumSize(300, 230)
        self.setMinimumSize(300, 230)

        self.centro()
        self.setFont(QFont('/font/HelveticaNeue.otf'))
        self.setStyleSheet("""
            * {
                background-color: #f8fcfb;
                border: none;
                color: #6892d5;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: #6892d5;
                color: #c9fdd7;
            }

            #anterior {
                background-color: #e5e5e5;
                color: #a1a1a1;
                font-size: 14px;
            }

            #historial {
                background-color: #e5e5e5;
            }

            #historial:hover {
                background-color: #f8fcfb;
            }

            #display {
                font-size: 22px;
            }""")

    def centro(self):
        posicion = self.frameGeometry()
        centrar = QDesktopWidget().availableGeometry().center()
        posicion.moveCenter(centrar)
        self.move(posicion.topLeft())

    def iniciar_controles(self):
        self.anterior_operacion = QLabel('  0', self)
        self.anterior_operacion.setObjectName('anterior')
        self.anterior_operacion.resize(270, 30)
        self.anterior_operacion.move(0, 0)

        historial = QPushButton('', self)
        historial.setIcon(QIcon('img/historial.png'))
        historial.setObjectName('historial')
        historial.resize(30, 30)
        historial.move(270, 0)
        historial.setToolTip('Historial de operaciones')

        self.display = QLineEdit('', self)
        self.display.setObjectName('display')
        self.display.resize(300, 40)
        self.display.move(0, 30)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setEnabled(False)

        btn1 = QPushButton('1', self)
        btn1.resize(75, 30)
        btn1.move(0, 80)
        btn1.clicked.connect(lambda:self.escribir('1'))

        btn2 = QPushButton('2', self)
        btn2.resize(75, 30)
        btn2.move(75, 80)
        btn2.clicked.connect(lambda:self.escribir('2'))

        btn3 = QPushButton('3', self)
        btn3.resize(75, 30)
        btn3.move(150, 80)
        btn3.clicked.connect(lambda:self.escribir('3'))

        btn_suma = QPushButton('+', self)
        btn_suma.setToolTip('Suma')
        btn_suma.resize(75, 30)
        btn_suma.move(225, 80)
        btn_suma.clicked.connect(self.sumar)

        btn4 = QPushButton('4', self)
        btn4.resize(75, 30)
        btn4.move(0, 110)
        btn4.clicked.connect(lambda:self.escribir('4'))

        btn5 = QPushButton('5', self)
        btn5.resize(75, 30)
        btn5.move(75, 110)
        btn5.clicked.connect(lambda:self.escribir('5'))

        btn6 = QPushButton('6', self)
        btn6.resize(75, 30)
        btn6.move(150, 110)
        btn6.clicked.connect(lambda:self.escribir('6'))

        btn_resta = QPushButton('-', self)
        btn_resta.setToolTip('Resta')
        btn_resta.resize(75, 30)
        btn_resta.move(225, 110)
        btn_resta.clicked.connect(self.restar)

        btn7 = QPushButton('7', self)
        btn7.resize(75, 30)
        btn7.move(0, 140)
        btn7.clicked.connect(lambda:self.escribir('7'))

        btn8 = QPushButton('8', self)
        btn8.resize(75, 30)
        btn8.move(75, 140)
        btn8.clicked.connect(lambda:self.escribir('8'))

        btn9 = QPushButton('9', self)
        btn9.resize(75, 30)
        btn9.move(150, 140)
        btn9.clicked.connect(lambda:self.escribir('9'))

        btn_multiplicacion = QPushButton('*', self)
        btn_multiplicacion.setToolTip('Multiplicación')
        btn_multiplicacion.resize(75, 30)
        btn_multiplicacion.move(225, 140)
        btn_multiplicacion.clicked.connect(self.multiplicar)

        btn_punto = QPushButton('.', self)
        btn_punto.setToolTip('Punto decimal')
        btn_punto.resize(75, 30)
        btn_punto.move(0, 170)
        btn_punto.clicked.connect(lambda:self.escribir('.'))

        btn0 = QPushButton('0', self)
        btn0.resize(75, 30)
        btn0.move(75, 170)
        btn0.clicked.connect(lambda:self.escribir('0'))

        btn_c = QPushButton('C', self)
        btn_c.setToolTip('Limpiar')
        btn_c.resize(75, 30)
        btn_c.move(150, 170)
        btn_c.clicked.connect(self.limpiar)

        btn_division = QPushButton('/', self)
        btn_division.setToolTip('División')
        btn_division.resize(75, 30)
        btn_division.move(225, 170)
        btn_division.clicked.connect(self.dividir)

        btn_resultado = QPushButton('=', self)
        btn_resultado.setToolTip('Resultado')
        btn_resultado.resize(300, 30)
        btn_resultado.move(0, 200)

    def escribir(self, cadena):
        aux = self.display.text()
        self.display.setText(aux + cadena)

    def limpiar(self):
        self.sistema.borrar()
        self.operacion = ''
        self.display.setText('')
        self.anterior_operacion.setText('  0')

    def conseguir_numero(self):
        if self.display.text() != '':
            if not self.sistema.num1.lleno:
                self.sistema.num1.valor = float(self.display.text())
            else:
                self.sistema.num2.valor = float(self.display.text())

    def sumar(self):
        if self.operacion == '':
            self.conseguir_numero()
            self.operacion = '+'
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '+')
            self.display.setText('')
        else:
            self.conseguir_numero()
            self.operar[self.operacion]()
            self.anterior_operacion.setText('  ' + self.sistema.resultado.valor + '+')
            self.display.setText('')
            self.sistema.num2.vaciar()
            self.operacion = '+'

    def restar(self):
        if self.operacion == '':
            self.conseguir_numero()
            self.operacion = '-'
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '-')
            self.display.setText('')
        else:
            self.conseguir_numero()
            self.operar[self.operacion]()
            self.anterior_operacion.setText('  ' + self.sistema.resultado.valor + '-')
            self.display.setText('')
            self.sistema.num2.vaciar()
            self.operacion = '-'

    def multiplicar(self):
        if self.operacion == '':
            self.conseguir_numero()
            self.operacion = '*'
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '*')
            self.display.setText('')
        else:
            self.conseguir_numero()
            self.operar[self.operacion]()
            self.anterior_operacion.setText('  ' + self.sistema.resultado.valor + '*')
            self.display.setText('')
            self.sistema.num2.vaciar()
            self.operacion = '*'

    def dividir(self):
        if self.operacion == '':
            self.conseguir_numero()
            self.operacion = '/'
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '/')
            self.display.setText('')
        else:
            self.conseguir_numero()
            self.operar[self.operacion]()
            self.anterior_operacion.setText('  ' + self.sistema.resultado.valor + '/')
            self.display.setText('')
            self.sistema.num2.vaciar()
            self.operacion = '/'
