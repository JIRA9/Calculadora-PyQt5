#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Creado: Sábado 24 de Febrero del 2018, 00:17:39
Calculadora simple con PyQt5

@author: josue
Última modificación: Febrero 2018
"""

import sys
from calculadora_gui import Ventana
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ventana()
    app.exec_()
