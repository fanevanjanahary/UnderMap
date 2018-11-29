# coding=utf-8

"""Définition des attributs"""


from qgis.PyQt.QtCore import QVariant


operator_def = {
    'name': 'Operateur',
    'type': QVariant.String,
    'length': 50,
    'precision': 0
}
class_def = {
    'name': 'Classe',
    'type': QVariant.String,
    'length': 1,
    'precision': 0,
}

diameter_def = {
    'name': 'Diametre',
    'type': QVariant.Double,
    'length': 10,
    'precision': 3,
}

rsx_def = {
    'name': 'Reseau',
    'type': QVariant.String,
    'length': 10,
    'precision': 0,
}

abandoned_def = {
    'name': 'Abandon',
    'type': QVariant.Int,
    'length': 1,
    'precision': 0,
}

rsx_color = {
    'ELEC': 'red',
    'GAZ': '#ffcf00',
    'PC': 'orange',
    'AEP': 'blue',
    'ASS': '#81300c',
    'CC': 'purple',
    'SIG': 'white',
    'MR': 'pink',
    'TEL': 'green'
}
