#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado con Python 3.X y PyQt5
Calculadora simple con PyQt5

@author: josue
Última modificación: Febrero 2018
"""

from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QDesktopWidget, QLabel, QTextEdit

class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciar_basico()
        self.iniciar_controles()
        self.show()

    def iniciar_basico(self):
        self.setWindowTitle('Calculator')
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

    def iniciar_controles(self):
        anterior_operacion = QLabel('  0', self)
        anterior_operacion.setObjectName('anterior')
        anterior_operacion.resize(270, 30)
        anterior_operacion.move(0, 0)

        historial = QPushButton('', self)
        historial.setIcon(QIcon('img/historial.png'))
        historial.setObjectName('historial')
        historial.resize(30, 30)
        historial.move(270, 0)
        historial.setToolTip('Historial de operaciones')

        display = QTextEdit('', self)
        display.setObjectName('display')
        display.setPlaceholderText('0')
        display.alignment()
        display.resize(300, 40)
        display.move(0, 30)

        btn1 = QPushButton('1', self)
        btn1.resize(75, 30)
        btn1.move(0, 80)

        btn2 = QPushButton('2', self)
        btn2.resize(75, 30)
        btn2.move(75, 80)

        btn3 = QPushButton('3', self)
        btn3.resize(75, 30)
        btn3.move(150, 80)

        btn_suma = QPushButton('+', self)
        btn_suma.setToolTip('Suma')
        btn_suma.resize(75, 30)
        btn_suma.move(225, 80)

        btn4 = QPushButton('4', self)
        btn4.resize(75, 30)
        btn4.move(0, 110)

        btn5 = QPushButton('5', self)
        btn5.resize(75, 30)
        btn5.move(75, 110)

        btn6 = QPushButton('6', self)
        btn6.resize(75, 30)
        btn6.move(150, 110)

        btn_resta = QPushButton('-', self)
        btn_resta.setToolTip('Resta')
        btn_resta.resize(75, 30)
        btn_resta.move(225, 110)

        btn7 = QPushButton('7', self)
        btn7.resize(75, 30)
        btn7.move(0, 140)

        btn8 = QPushButton('8', self)
        btn8.resize(75, 30)
        btn8.move(75, 140)

        btn9 = QPushButton('9', self)
        btn9.resize(75, 30)
        btn9.move(150, 140)

        btn_multiplicacion = QPushButton('*', self)
        btn_multiplicacion.setToolTip('Multiplicación')
        btn_multiplicacion.resize(75, 30)
        btn_multiplicacion.move(225, 140)

        btn_punto = QPushButton('.', self)
        btn_punto.setToolTip('Punto decimal')
        btn_punto.resize(75, 30)
        btn_punto.move(0, 170)

        btn0 = QPushButton('0', self)
        btn0.resize(75, 30)
        btn0.move(75, 170)

        btn_c = QPushButton('C', self)
        btn_c.setToolTip('Limpiar')
        btn_c.resize(75, 30)
        btn_c.move(150, 170)

        btn_division = QPushButton('/', self)
        btn_division.setToolTip('División')
        btn_division.resize(75, 30)
        btn_division.move(225, 170)

        btn_resultado = QPushButton('=', self)
        btn_resultado.setToolTip('Resultado')
        btn_resultado.resize(300, 30)
        btn_resultado.move(0, 200)

    def centro(self):
        posicion = self.frameGeometry()
        centrar = QDesktopWidget().availableGeometry().center()
        posicion.moveCenter(centrar)
        self.move(posicion.topLeft())
