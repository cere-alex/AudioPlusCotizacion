#! /usr/bin/env python3

import class_audifonos as audifonos
import pandas as pd
import numpy as np


def seleccion_audifono(caja=[
    'Mostrar Todos', 'Mostrar Todos', 'Mostrar Todos', 'Mostrar Todos',
    'Seleccione Uno']):

    starkey = pd.read_csv('./starkey_precios.csv', index_col=False)
    audio_service = pd.read_csv('./audioService_precios.csv', index_col=False)

    marca_audifono = pd.concat((starkey, audio_service))

    marca_audifono['Familia'].fillna('ERROR', inplace=True)
    marca_audifono['Modelo'].fillna('ERROR', inplace=True)
    marca_audifono['Fuente'].fillna('ERROR', inplace=True)
    marca_audifono['Potencia'].fillna('ERROR', inplace=True)

    mostar_todo = 'Mostrar Todos'

    atributos = ['Gama', 'Familia', 'Potencia', 'Modelo']

    audifono_selected = marca_audifono.copy()

    lista_seleccionados = []

    # seleccion de columnas
    for j, i in enumerate(atributos):
        lista = list(set(audifono_selected[i]))
        lista.sort()
        lista.insert(0, mostar_todo)
        lista_seleccionados.append(lista)
        # print(lista)
        nro = lista.index(caja[j])
        item_selected = lista[nro]  # gama aleatorio
        if item_selected != 'Mostrar Todos':
            audifono_selected = audifono_selected[audifono_selected[i] ==
                                                  item_selected]

    audifono_selected.reset_index(drop=True, inplace=True)

    c = np.shape(audifono_selected)

    aux = [
        '{0} {1} {2} {3} {4}'.format(
            audifono_selected.Familia.values[i],
            audifono_selected.Tecnologia.values[i],
            audifono_selected.Modelo.values[i],
            audifono_selected.Fuente.values[i],
            audifono_selected.Potencia.values[i],
        ) for i in range(c[0])
    ]
    aux.insert(0, 'Seleccione Uno')
    lista_seleccionados.append(aux)
    if caja[-1] != 'Seleccione Uno':
        nro = int(caja[-1])
        try:
            audifono_selected = audifono_selected.iloc[[nro - 1]]
        except:
            audifono_selected = audifono_selected.iloc[[0]]
        print(audifono_selected)
        # creacion del objeto Audifono
        audifono = audifonos.audifonos(
            familia=audifono_selected.Familia.values[0],
            tecnologia=audifono_selected.Tecnologia.values[0],
            modelo=audifono_selected.Modelo.values[0],
            fuente=audifono_selected.Fuente.values[0],
            potencia=audifono_selected.Potencia.values[0],
            precio=audifono_selected.Precio.values[0],
            gama=audifono_selected.Gama.values[0])

        return audifono

    return lista_seleccionados


# caja = ['media', 'CROS G4', 'STANDARD', 'RIC', 0]
# simulacion = seleccion_audifono(caja, cantidad=3)

# print(simulacion.costos_dependiendo_gama(3))
