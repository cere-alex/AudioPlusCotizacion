#! /usr/bin/env python3
import precio_cantidad_audifono as pca
import math

class audifonos:
    def __init__(self, familia, tecnologia, modelo, fuente, potencia, precio,
                 gama):
        self._familia = familia
        self._fuente = fuente
        self._gama = gama
        self._modelo = modelo
        self._potencia = potencia
        self._precio = precio * 7
        self._tecnologia = tecnologia

    @property
    def familia(self):
        return self._familia

    @property
    def fuente(self):
        return self._fuente

    @property
    def gama(self):
        return self._gama

    @property
    def modelo(self):
        return self._modelo

    @property
    def potencia(self):
        return self._potencia

    @property
    def precio(self):
        return self._precio

    @property
    def tecnologia(self):
        return self._tecnologia

    @familia.setter
    def familia(self, new_familia):
        self._familia = new_familia

    @fuente.setter
    def fuente(self, new_fuente):
        self._fuente = new_fuente

    @gama.setter
    def gama(self, new_gama):
        self._gama = new_gama

    @modelo.setter
    def modelo(self, new_modelo):
        self._modelo = new_modelo

    @potencia.setter
    def potencia(self, new_potencia):
        self._potencia = new_potencia

    @precio.setter
    def precio(self, new_precio):
        self._precio = new_precio

    @tecnologia.setter
    def tecnologia(self, new_tecnologia):
        self._tecnologia = new_tecnologia

    def costos_dependiendo_gama(self, cantidad):
        try:

            if self._gama == 'alta':
                p = pca.precio_gama_alta
                c = pca.cantidad_gama_alta

            elif self._gama == 'media':
                p = pca.precio_gama_media
                c = pca.cantidad_gama_media

            elif self._gama == 'standard':
                p = pca.precio_gama_standard
                c = pca.cantidad_gama_standard

            suma = 0

            if cantidad == 1:
                for i, j in enumerate(p):
                    suma += round(c[i] * p[j])

            elif cantidad == 2:
                dos = pca.precio_dos_audifonos
                for i, j in enumerate(p):
                    suma += round(c[i] * p[j] * dos[i])

            elif cantidad == 3:
                aux = self.costos_dependiendo_gama(2)
                if self._gama == 'alta':
                    self._gama = 'media'
                elif self._gama == 'media':
                    self._gama = 'standard'
                aux2 = self.costos_dependiendo_gama(1)
                suma = aux + aux2

            elif cantidad == 4:
                aux = self.costos_dependiendo_gama(2)
                if self._gama == 'alta':
                    self._gama = 'media'
                elif self._gama == 'media':
                    self._gama = 'standard'
                else:
                    self._gama = 'standard'

                aux2 = self.costos_dependiendo_gama(2)

                suma = aux + aux2

            elif cantidad == 5:
                aux = self.costos_dependiendo_gama(4)
                if self._gama == 'alta':
                    self._gama = 'media'
                elif self._gama == 'media':
                    self._gama = 'standard'
                else:
                    self._gama = 'standard'

                aux2 = self.costos_dependiendo_gama(1)

                suma = aux + aux2

            elif cantidad == 6:
                aux = self.costos_dependiendo_gama(4)
                if self._gama == 'alta':
                    self._gama = 'media'
                elif self._gama == 'media':
                    self._gama = 'standard'
                else:
                    self._gama = 'standard'

                aux2 = self.costos_dependiendo_gama(2)

                suma= aux + aux2

            return suma
        except Exception as e:
            print('Ingrese un valor')

    def costo_total(self, cantidad):
        return self._precio*cantidad + self.costos_dependiendo_gama(cantidad)

    def ganancia(self, cantidad, utilidad):
        u = 1 + (utilidad / 100)

        redondeo = math.ceil(u * self.costo_total(cantidad)/100) * 100
        return redondeo

    def descuento(self, precio_final, descuento):
        return precio_final*(1-descuento/100)
    def __str__(self):
        return f"el precio es de {self._precio}"

# audif = audifonos('qweq', 'wqewq', 'qweqeqw', 'qqwe','sdf', 1320, 'alta')

# print(audif.ganancia(cantidad=1, utilidad=20))