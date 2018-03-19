#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado con Python3 y PyQt5.
Clase para crear la GUI del proyecto.

Autor: Rodríguez Hernández Josué Iván
Última modificación: Marzo 2018
"""

from PyQt5.QtCore import Qt # Configuraciones y valores generales del sistema
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QPushButton, QToolTip, QWidget
from sistema import Calculadora # Importamos los archivos locales necesarios para la GUI

class Ventana(QWidget): # Hereda la clase QWidget
    """
    Clase: Ventana
    Crea la GUI de la calculadora, además agrega las métodos para ser completamente funcional.

    Parámetros:
    QWidget -- Clase necesaria para crear la GUI

    Atributos:
    sistema -- Instancia de "Calculadora"
    operacion -- Indica la operación a realizar por la calculadora
    operar -- Switch entre las diferentes operaciones
    """

    def __init__(self):
        """Constructor Clase: Ventana"""

        super().__init__() # Llama al constructor de la clase heredada (QWidget)

        self.sistema = Calculadora()
        self.operacion = ''
        self.operar = {
            '+':self.sistema.suma,
            '-':self.sistema.resta,
            '*':self.sistema.multiplicacion,
            '/':self.sistema.division
        }

        self.iniciar_gui()
        self.iniciar_controles()
        self.show()

    # --- Métodos utilizados en la GUI ---
    def centrar_gui(self):
        """Centrar la GUI de acuerdo a la pantalla"""

        centro = QDesktopWidget().availableGeometry().center()
        posicion = self.frameGeometry()
        posicion.moveCenter(centro)
        self.move(posicion.topLeft())

    def escribir_display(self, cadena):
        """
        Escribe el argumento dado en el control "display".

        Parámetros:
        cadena -- Valor a escribir en el control
        """

        aux = self.display.text() # Creamos un auxiliar para no perder datos
        self.display.setText(aux + cadena)

    def limpiar(self):
        """Restablece todo en un valor 0 excepto el historial"""

        self.anterior_operacion.setText('  0')
        self.display.setText('')
        self.operacion = ''
        self.sistema.borrar()

    # --- Crear GUI y configurarla ---
    def iniciar_gui(self):
        """Configurar los valores de la ventana (GUI)"""

        # Cambiar las dimensiones de la GUI
        self.setMaximumSize(300, 230)
        self.setMinimumSize(300, 230)
        self.resize(300, 230)
        self.centrar_gui()

        self.setFont(QFont('/font/HelveticaNeue.otf'))
        self.setWindowIcon(QIcon('img/icon.png'))
        self.setWindowTitle('Calculadora PyQt5')
        self.setStyleSheet("""
            * {
                background-color: #f8fcfb;
                border: none;
            }

            QPushButton {
                color: #6892d5;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: #6892d5;
                color: #c9fdd7;
            }

            #anterior, #historial {
                background-color: #e5e5e5;
            }

            #anterior {
                color: #a1a1a1;
                font-size: 14px;
            }

            #historial:hover {
                background-color: #f8fcfb;
            }

            #display {
                color: black;
                font-size: 22px;
            }""")

    def iniciar_controles(self):
        """Crea los controles que apareceran en la GUI, al igual los asocia con sus métodos"""

        self.anterior_operacion = QLabel(self)
        self.anterior_operacion.setObjectName('anterior')
        self.anterior_operacion.resize(270, 30)
        self.anterior_operacion.move(0, 0)

        btn_historial = QPushButton(self)
        btn_historial.setObjectName('historial')
        btn_historial.setToolTip('Historial de operaciones')
        btn_historial.setIcon(QIcon('img/icon.png'))
        btn_historial.resize(30, 30)
        btn_historial.move(270, 0)
        btn_historial.clicked.connect(self.leer_historial) # Enlazamos el evento cuando hace clic en el botón con un método que hemos creado

        self.display = QLineEdit(self)
        self.display.setObjectName('display')
        self.display.setEnabled(False)
        self.display.resize(300, 40)
        self.display.move(0, 30)
        self.display.setAlignment(Qt.AlignRight) # Todo el texto del control será alineado a la derecha

        btn1 = QPushButton('1', self)
        btn1.resize(75, 30)
        btn1.move(0, 80)
        btn1.clicked.connect(lambda:self.escribir_display('1')) # Como el método a conectar necesita un argumento creamos una función anónima sino dará error

        btn2 = QPushButton('2', self)
        btn2.resize(75, 30)
        btn2.move(75, 80)
        btn2.clicked.connect(lambda:self.escribir_display('2'))

        btn3 = QPushButton('3', self)
        btn3.resize(75, 30)
        btn3.move(150, 80)
        btn3.clicked.connect(lambda:self.escribir_display('3'))

        btn_suma = QPushButton('+', self)
        btn_suma.setToolTip('Suma')
        btn_suma.resize(75, 30)
        btn_suma.move(225, 80)
        btn_suma.clicked.connect(self.sumar)

        btn4 = QPushButton('4', self)
        btn4.resize(75, 30)
        btn4.move(0, 110)
        btn4.clicked.connect(lambda:self.escribir_display('4'))

        btn5 = QPushButton('5', self)
        btn5.resize(75, 30)
        btn5.move(75, 110)
        btn5.clicked.connect(lambda:self.escribir_display('5'))

        btn6 = QPushButton('6', self)
        btn6.resize(75, 30)
        btn6.move(150, 110)
        btn6.clicked.connect(lambda:self.escribir_display('6'))

        btn_resta = QPushButton('-', self)
        btn_resta.setToolTip('Resta')
        btn_resta.resize(75, 30)
        btn_resta.move(225, 110)
        btn_resta.clicked.connect(self.restar)

        btn7 = QPushButton('7', self)
        btn7.resize(75, 30)
        btn7.move(0, 140)
        btn7.clicked.connect(lambda:self.escribir_display('7'))

        btn8 = QPushButton('8', self)
        btn8.resize(75, 30)
        btn8.move(75, 140)
        btn8.clicked.connect(lambda:self.escribir_display('8'))

        btn9 = QPushButton('9', self)
        btn9.resize(75, 30)
        btn9.move(150, 140)
        btn9.clicked.connect(lambda:self.escribir_display('9'))

        btn_multiplicacion = QPushButton('*', self)
        btn_multiplicacion.setToolTip('Multiplicación')
        btn_multiplicacion.resize(75, 30)
        btn_multiplicacion.move(225, 140)
        btn_multiplicacion.clicked.connect(self.multiplicar)

        btn_punto = QPushButton('.', self)
        btn_punto.setToolTip('Punto decimal')
        btn_punto.resize(75, 30)
        btn_punto.move(0, 170)
        btn_punto.clicked.connect(lambda:self.escribir_display('.'))

        btn0 = QPushButton('0', self)
        btn0.resize(75, 30)
        btn0.move(75, 170)
        btn0.clicked.connect(lambda:self.escribir_display('0'))

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
        btn_resultado.clicked.connect(self.igual)

    def keyPressEvent(self, e):
        """
        Evento sobreescrito: keyPressEvent

        Parámetros:
        e -- Evento de presionar una tecla
        """

        aux = self.display.text()
        if e.key() == Qt.Key_N:
            if aux != '':
                aux = float(aux)
            else:
                aux = 0
            aux *= -1
            self.display.setText(str(aux))
        elif e.key() == Qt.Key_Plus:
            self.sumar()
        elif e.key() == Qt.Key_Minus:
            self.restar()
        elif e.key() == Qt.Key_Asterisk:
            self.multiplicar()
        elif e.key() == Qt.Key_Slash:
            self.dividir()
        elif e.key() == Qt.Key_Equal:
            self.igual()
        else:
            if e.key() == Qt.Key_0:
                aux += '0'
            elif e.key() == Qt.Key_1:
                aux += '1'
            elif e.key() == Qt.Key_2:
                aux += '2'
            elif e.key() == Qt.Key_3:
                aux += '3'
            elif e.key() == Qt.Key_4:
                aux += '4'
            elif e.key() == Qt.Key_5:
                aux += '5'
            elif e.key() == Qt.Key_6:
                aux += '6'
            elif e.key() == Qt.Key_7:
                aux += '7'
            elif e.key() == Qt.Key_8:
                aux += '8'
            elif e.key() == Qt.Key_9:
                aux += '9'
            elif e.key() == Qt.Key_Backspace:
                if aux != '':
                    aux = aux[:-1]
            elif e.key() == Qt.Key_Period:
                if ('.' in aux) < 1:
                    aux += '.'
            self.display.setText(aux)

    # --- Métodos del historial de operaciones ---
    def borrar_historial(self, componente):
        """
        Borra todo el historial de operaciones.

        Parámetros:
        componente -- Cierra el componente dado
        """

        op = QMessageBox.question(self, "Borrar el historial", "¿Desea borrar el historial de operaciones?", QMessageBox.Yes | QMessageBox.No)
        if op == QMessageBox.Yes:
            with open('historial.hist', 'w') as f: # Permisos de escritura
                f.write('')
                componente.close()

    def escribir_operacion(self, num1, operador):
        """
        Escribe en un archivo "historial.hist" todas las operaciones que se hagan en la calculdora.

        Parámetros:
        num1 -- Primer número de la operación
        operador -- Símbolo de la operación que se realizó
        """

        cadena = str(num1) + operador + str(self.sistema.num2.valor) + '=' + self.sistema.resultado + '\n'
        with open("historial.hist", "a") as f: # Abre con permisos de escritura pero el cursor lo pone al final del fichero
            f.write(cadena)

    def leer_historial(self):
        """Crea un QDialog que mostrará el historial de operaciones de la calculadora"""

        try:
            with open('historial.hist', 'r') as f: # Intentamos abrir un fichero externo llamado "historial.hist" con permisos de lectura (r)
                cadena = f.read() # Leemos todo el contenido del fichero

                if cadena != '':
                    ventana_historial = QDialog()
                    ventana_historial.setMaximumSize(300, 600)
                    ventana_historial.setMinimumSize(300, 600)
                    ventana_historial.resize(300, 600)

                    ventana_historial.setFont(QFont('/font/HelveticaNeue.otf'))
                    ventana_historial.setWindowIcon(QIcon('img/icon.png'))
                    ventana_historial.setWindowModality(Qt.ApplicationModal)
                    ventana_historial.setWindowTitle('Historial')
                    ventana_historial.setStyleSheet("""
                        * {
                            background-color: #f8fcfb;
                            border: none;
                            font-size: 12px;
                        }

                        QPlainTextEdit {
                            font-size: 15px;
                        }
                        QPushButton:hover {
                            background-color: #6892d5;
                            color: #c9fdd7;
                        }""")

                    historial = QPlainTextEdit(cadena, ventana_historial)
                    historial.resize(300, 550)
                    historial.move(0,0)

                    btn_volver = QPushButton(ventana_historial)
                    btn_volver.setIcon(QIcon('img/atras.png'))
                    btn_volver.resize(50, 50)
                    btn_volver.move(0, 550)
                    btn_volver.clicked.connect(lambda: ventana_historial.close()) # Cerrar ventana

                    btn_borrar_historial = QPushButton('Borrar historial', ventana_historial)
                    btn_borrar_historial.resize(250, 50)
                    btn_borrar_historial.move(50, 550)
                    btn_borrar_historial.clicked.connect(lambda:self.borrar_historial(ventana_historial))
                    ventana_historial.exec_() # Lanzamos el QDialog
                else:
                    QMessageBox.information(self, "Información", "No hay operaciones en el historial.") # Damos un mensaje en dado caso que no hay nada en el fichero

        except FileNotFoundError:
            QMessageBox.information(self, "Información", "No hay operaciones en el historial.")

    # --- Métodos sobre los números y operaciones de la calculadora ---
    def conseguir_numero(self):
        """Obtiene el número en flotante (float) del control "display"""

        if self.display.text() != '':
            if not self.sistema.num1.editado or self.operacion == '':
                self.sistema.num1.valor = float(self.display.text())
            else:
                self.sistema.num2.valor = float(self.display.text())

    def sumar(self):
        """Suma los 2 números guardados"""

        if self.operacion == '':
            self.conseguir_numero()
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '+')
            self.operacion = '+'
            self.display.setText('')
        else:
            self.conseguir_numero()
            aux = self.sistema.num1.valor
            self.operar[self.operacion]() # Si hay una operación anterior la realiza

            self.escribir_operacion(aux, self.operacion)
            self.anterior_operacion.setText('  ' + self.sistema.resultado + '+')

            self.operacion = '+'
            self.display.setText('')
            self.sistema.num2.vaciar()

    def restar(self):
        """Resta los 2 números guardados"""

        if self.operacion == '':
            self.conseguir_numero()
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '-')
            self.operacion = '-'
            self.display.setText('')
        else:
            self.conseguir_numero()
            aux = self.sistema.num1.valor
            self.operar[self.operacion]()

            self.escribir_operacion(aux, self.operacion)
            self.anterior_operacion.setText('  ' + self.sistema.resultado + '-')

            self.operacion = '-'
            self.display.setText('')
            self.sistema.num2.vaciar()

    def multiplicar(self):
        """Multiplica los 2 números guardados"""

        if self.operacion == '':
            self.conseguir_numero()
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '*')
            self.operacion = '*'
            self.display.setText('')
        else:
            self.conseguir_numero()
            aux = self.sistema.num1.valor
            self.operar[self.operacion]()

            self.escribir_operacion(aux, self.operacion)
            self.anterior_operacion.setText('  ' + self.sistema.resultado + '*')

            self.operacion = '*'
            self.display.setText('')
            self.sistema.num2.vaciar()

    def dividir(self):
        """Divide los 2 números guardados"""

        if self.operacion == '':
            self.conseguir_numero()
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor) + '/')
            self.operacion = '/'
            self.display.setText('')
        else:
            self.conseguir_numero()
            aux = self.sistema.num1.valor
            self.operar[self.operacion]()

            self.escribir_operacion(aux, self.operacion)
            self.anterior_operacion.setText('  ' + self.sistema.resultado + '/')

            self.operacion = '/'
            self.display.setText('')
            self.sistema.num2.vaciar()

    def igual(self):
        """Resuelve todas las operaciones pendientes por realizar, sino hay nínguna solo guarda el número"""

        if self.operacion == '':
            self.conseguir_numero()
            self.anterior_operacion.setText('  ' + str(self.sistema.num1.valor))
            self.display.setText('')
        else:
            self.conseguir_numero()
            aux = self.sistema.num1.valor
            self.operar[self.operacion]()

            self.escribir_operacion(aux, self.operacion)
            self.anterior_operacion.setText('  ' + self.sistema.resultado)

            self.operacion = ''
            self.display.setText('')
            self.sistema.num2.vaciar()
