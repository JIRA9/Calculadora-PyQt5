#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado con Python3 y PyQt5.
Calculadora simple con PyQt5.

Autor: Rodríguez Hernández Josué Iván
Última modificación: Marzo 2018
"""

import sys # Necesario para correr la GUI
from PyQt5.QtWidgets import QApplication # Crear la aplicación
from calculadora_gui import Ventana # GUI de la calculadora

if __name__ == '__main__': # Sí este es el fichero que se está ejecutando
    app = QApplication(sys.argv)
    w = Ventana()
    app.exec_()
