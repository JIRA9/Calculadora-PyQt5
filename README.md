# Calculadora en PyQt5

## Descripción:
Es una aplicación *GUI* creada con **PyQt5** y **Python3**, en está *GUI* se manejan todos los aspectos básicos de **PyQt5** para la creación de interfaces. En este proyectos se implementa lo siguiente:

* Uso de **PyQt5**
* Creación de *GUI's* con **PyQt5**
* Modificación de aspectos básicos en **PyQt5** (fuentes, colores, tamaños, posiciones)
* Uso de estilos en *GUI*
* Creación de mensajes y dialogos

## Características:
* Guarda en un archivo *"historial.hist"* todas las operaciones que se han realizado
* Puede utilizar las teclas para manejar más rápido la calculadora:
    * **[0-9.]:** Escribe le caracter presionado
    * **[+ - * / (SHIFT+0)]:** Teclas para operar con los número
    * **[BACKSPACE]:** Borra un caracter del número actual
    * **[N]:** Pone el número actual en negativo

## Versión actual: *1.1*
---

### Requisitos para correr el proyecto:
1. Tener instalado el módulo **PyQt5** en el *entorno virtual (virtualenv)* a utilizar o en *Python* en general.

### Notas:
1. La *GUI* está creada por medio de código, no existe ningún archivo *XML* para modificarlo en el diseñador gráfico.
2. Para instalar **PyQt5** es recomendable que sea con el módulo **pip** de *Python*.

En caso de *Linux* debemos instalar **pip** para *Python3*:
>```sudo apt-get install python3-pip```

Después instalar **PyQt5**:
>```sudo pip3 install pyqt5```

En caso de *Windows*, cuando se instala *Python* trae instalado por defecto el módulo **pip**, solo queda instalar **PyQt5**:
>```pip install pyqt5```
