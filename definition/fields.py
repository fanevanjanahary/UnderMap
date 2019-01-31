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
    'CC': '#D85DFF',
    'MR': '#FFCCFF',
    'PC': '#FFB115',
    'AEP': '#97E4FF',
    'ASS': '#7CAB80',
    'GAZ': '#FFF411',
    'SIG': '#BFBFBF',
    'TEL': '#65F355',
    'ELEC': '#FF5353'
}
