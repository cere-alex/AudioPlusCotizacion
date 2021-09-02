#! /usr/bin/env python3

import sys
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPixmap
import class_cotizacion as ctz
from datetime import datetime
import locale
from darktheme.widget_template import DarkPalette


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setPalette(DarkPalette())
        uic.loadUi('windows.ui', self)
        print(locale.getlocale())
        self.cant = 0
        self.utility = 20
        self.desc = 5
        self.logo.setPixmap(QPixmap('./logo_audioplus.jpg'))
        self.reiniciar()
        self.labelDescuento.setText('Descuento por el mes de {}'.format(
            datetime.now().strftime('%B')))
        self.boxGama.currentIndexChanged.connect(self.change_gama)
        self.boxFamilia.currentIndexChanged.connect(self.change_familia)
        self.boxPotencia.currentIndexChanged.connect(self.change_potencia)
        self.boxModelo.currentIndexChanged.connect(self.change_modelo)
        self.boxAudifono.currentIndexChanged.connect(self.change_audifono)
        self.boxCantidad.setRange(0, 6)
        self.boxCantidad.valueChanged.connect(self.change_audifono)
        self.buttonBorrar.pressed.connect(self.reiniciar)

        self.show()

    def bloquear_senhal(self, boolean):
        print(boolean)
        self.boxGama.blockSignals(boolean)
        self.boxFamilia.blockSignals(boolean)
        self.boxPotencia.blockSignals(boolean)
        self.boxModelo.blockSignals(boolean)
        self.boxAudifono.blockSignals(boolean)
        self.boxCantidad.blockSignals(boolean)

    def reiniciar(self):
        self.bloquear_senhal(True)
        self.boxCantidad.blockSignals(True)
        self.delete()
        self.clear_line()
        self.crear_caja()
        self.boxCantidad.blockSignals(False)
        self.bloquear_senhal(False)

    def crear_caja(self, a=0, b=5, cotizacion=ctz.seleccion_audifono()):
        box = [
            'boxGama', 'boxFamilia', 'boxPotencia', 'boxModelo', 'boxAudifono'
        ]
        for i in range(a, b):
            for j in cotizacion[i]:
                aux = getattr(self, '{}'.format(box[i]))
                aux.addItem(j)

    def change_gama(self):
        gama = self.boxGama.currentText()
        datos = [
            gama, 'Mostrar Todos', 'Mostrar Todos', 'Mostrar Todos',
            'Seleccione Uno'
        ]
        print(datos)
        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.delete(a=1)
        self.crear_caja(a=1, cotizacion=cotizacion)
        self.bloquear_senhal(False)

    def change_familia(self):
        """Llena la caja familia con los items correspondientes"""
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        datos = [
            gama, familia, 'Mostrar Todos', 'Mostrar Todos', 'Seleccione Uno'
        ]
        print(datos)
        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.delete(a=2)
        self.crear_caja(a=2, cotizacion=cotizacion)
        self.bloquear_senhal(False)

    def change_potencia(self):
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        potencia = self.boxPotencia.currentText()
        datos = [gama, familia, potencia, 'Mostrar Todos', 'Seleccione Uno']
        print(datos)
        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.delete(a=3)
        self.crear_caja(a=3, cotizacion=cotizacion)
        self.bloquear_senhal(False)

    def change_modelo(self):
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        potencia = self.boxPotencia.currentText()
        modelo = self.boxModelo.currentText()
        datos = [gama, familia, potencia, modelo, 'Seleccione Uno']
        print(datos)
        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.delete(a=4)
        self.crear_caja(a=4, cotizacion=cotizacion)
        self.bloquear_senhal(False)

    def change_audifono(self):

        box = [
            'boxGama', 'boxFamilia', 'boxPotencia', 'boxModelo', 'boxAudifono'
        ]
        datos = []
        for i in range(0, 4):
            # no se toma encuenta boxAudifono por ser otro tipo de dato
            aux = getattr(self, box[i])
            aux2 = aux.currentText()
            datos.append(aux2)
        audifono = self.boxAudifono.currentIndex()
        datos.append(audifono)
        print(datos)
        if self.boxCantidad.value() == 0:
            self.clear_line()
        if audifono != 0:
            self.bloquear_senhal(True)
            self.cant = self.boxCantidad.value()
            # return es class_audifonos
            try:
                cotizacion = ctz.seleccion_audifono(datos)
                print(cotizacion)
                ganancia = cotizacion.ganancia(cantidad=self.cant,
                                               utilidad=self.utility)
                self.linePrecio.setText(str(ganancia))
                descuento = cotizacion.descuento(precio_final=ganancia,
                                                 descuento=self.desc)
                self.lineDescuento.setText(str(self.desc))
                self.linePrecioFinal.setText(str(descuento))
            finally:
                self.bloquear_senhal(False)
        else:
            self.clear_line()

    def delete(self, a=0, b=5):
        self.boxCantidad.setValue(0)
        box = [
            'boxGama', 'boxFamilia', 'boxPotencia', 'boxModelo', 'boxAudifono'
        ]
        for i in range(a, b):
            aux = getattr(self, box[i])
            aux.clear()
        self.clear_line()

    def clear_line(self):
        self.linePrecio.setText('')
        self.lineDescuento.setText('')
        self.linePrecioFinal.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow()
    sys.exit(app.exec_())
