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
        self.desc = 10
        self.logo.setPixmap(QPixmap('./logo_audioplus.jpeg'))
        self.reiniciar()
        self.labelDescuento.setText('Descuento por el mes de {}'.format(
            datetime.now().strftime('%B')))
        self.boxGama.currentIndexChanged.connect(self.change_gama)
        self.boxFamilia.currentIndexChanged.connect(self.change_familia)
        self.boxPotencia.currentIndexChanged.connect(self.change_potencia)
        self.boxModelo.currentIndexChanged.connect(self.change_modelo)
        self.boxAudifono.currentIndexChanged.connect(self.change_audifono)
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

    def reiniciar(self):
        self.bloquear_senhal(True)
        self.boxCantidad.blockSignals(True)
        self.delete()
        self.clear_line()
        self.crear_caja()
        self.boxCantidad.blockSignals(False)
        self.bloquear_senhal(False)

    def crear_caja(self, cotizacion=ctz.seleccion_audifono()):
        gama = cotizacion[0]
        familia = cotizacion[1]
        potencia = cotizacion[2]
        modelo = cotizacion[3]
        audifono = cotizacion[4]
        box = ['boxGama', 'boxFamilia', 'boxPotencia', 'boxModelo', 'boxAudifono']

        for i in range(0, 5):
            for j in cotizacion[i]:
                aux = getattr(self, '{}'.format(box[i]))
                aux.addItem(j)

        #
        # for i in gama:
        #     aux = getattr(self, 'boxGama')
        #     print(aux)
        #     aux.addItem(i)
        #     # self.boxGama.addItem(i)
        # for i in familia:
        #     self.boxFamilia.addItem(i)
        # for i in potencia:
        #     self.boxPotencia.addItem(i)
        # for i in modelo:
        #     self.boxModelo.addItem(i)
        # for i in audifono:
        #     self.boxAudifono.addItem(i)

    def change_gama(self):
        self.boxCantidad.setValue(0)
        gama = self.boxGama.currentText()
        datos = [
            gama, 'Mostrar Todos', 'Mostrar Todos', 'Mostrar Todos',
            'Seleccione Uno'
        ]
        print(datos)

        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.boxFamilia.clear()
        self.boxPotencia.clear()
        self.boxModelo.clear()
        self.boxAudifono.clear()
        familia = cotizacion[1]
        potencia = cotizacion[2]
        modelo = cotizacion[3]
        audifono = cotizacion[4]
        for i in familia:
            self.boxFamilia.addItem(i)
        for i in potencia:
            self.boxPotencia.addItem(i)
        for i in modelo:
            self.boxModelo.addItem(i)
        for i in audifono:
            self.boxAudifono.addItem(i)
        self.bloquear_senhal(False)

    def change_familia(self):
        """Llena la caja familia con los items correspondientes"""
        self.boxCantidad.setValue(0)
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        datos = [
            gama, familia, 'Mostrar Todos', 'Mostrar Todos', 'Seleccione Uno'
        ]
        print(datos)

        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.boxPotencia.clear()
        self.boxModelo.clear()
        self.boxAudifono.clear()
        potencia = cotizacion[2]
        modelo = cotizacion[3]
        audifono = cotizacion[4]
        for i in potencia:
            self.boxPotencia.addItem(i)
        for i in modelo:
            self.boxModelo.addItem(i)
        for i in audifono:
            self.boxAudifono.addItem(i)
        self.bloquear_senhal(False)

    def change_potencia(self):
        self.boxCantidad.setValue(0)
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        potencia = self.boxPotencia.currentText()
        datos = [gama, familia, potencia, 'Mostrar Todos', 'Seleccione Uno']
        print(datos)

        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.boxCantidad.blockSignals(True)
        self.boxModelo.clear()
        self.boxAudifono.clear()
        modelo = cotizacion[3]
        audifono = cotizacion[4]
        for i in modelo:
            self.boxModelo.addItem(i)
        for i in audifono:
            self.boxAudifono.addItem(i)
        self.boxCantidad.blockSignals(False)
        self.bloquear_senhal(False)

    def change_modelo(self):
        self.boxCantidad.setValue(0)
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        potencia = self.boxPotencia.currentText()
        modelo = self.boxModelo.currentText()
        datos = [gama, familia, potencia, modelo, 'Seleccione Uno']
        print(datos)

        cotizacion = ctz.seleccion_audifono(datos)
        self.bloquear_senhal(True)
        self.boxAudifono.clear()
        audifono = cotizacion[4]
        for i in audifono:
            self.boxAudifono.addItem(i)
        self.bloquear_senhal(False)

    def change_audifono(self):
        gama = self.boxGama.currentText()
        familia = self.boxFamilia.currentText()
        potencia = self.boxPotencia.currentText()
        modelo = self.boxModelo.currentText()
        audifono = self.boxAudifono.currentIndex()
        datos = [gama, familia, potencia, modelo, audifono]
        print(datos)
        if self.boxCantidad.value() == 0:
            self.clear_line()
        if audifono != 0 or self.cant != 0:
            self.bloquear_senhal(True)
            self.cant = self.boxCantidad.value()
            # return es class_audifonos
            try:
                cotizacion = ctz.seleccion_audifono(datos)
                print(cotizacion)
                ganancia = cotizacion.ganancia(cantidad=self.cant,
                                               utilidad=self.utility)
                self.linePrecio.setText(str(ganancia))
                descuento = cotizacion.descuento(precio_final=ganancia, descuento=self.desc)
                self.lineDescuento.setText(str(self.desc))
                self.linePrecioFinal.setText(str(descuento))
            finally:
                self.bloquear_senhal(False)

    def delete(self):
        self.boxGama.clear()
        self.boxFamilia.clear()
        self.boxPotencia.clear()
        self.boxModelo.clear()
        self.boxAudifono.clear()
        self.boxCantidad.setRange(0, 6)
        self.boxCantidad.setValue(0)

    def clear_line(self):
        self.linePrecio.setText('')
        self.lineDescuento.setText('')
        self.linePrecioFinal.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyWindow()
    sys.exit(app.exec_())
