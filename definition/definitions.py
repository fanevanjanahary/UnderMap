# coding=utf-8

""" Tous les définitions """


from qgis.PyQt.QtCore import QVariant


operator_def = {
    'name': 'Exploitant',
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

aerial_def = {
    'name': 'Aérien',
    'type': QVariant.Int,
    'length': 1,
    'precision': 0,
}

rsx_color = {
    'ELEC': '#FF5353',
    'GAZ': '#FFF411',
    'PC': '#FFB115',
    'AEP': '#97E4FF',
    'ASS': '#D6AB80',
    'CC': '#D85DFF',
    'TEL': '#65F355',
    'SIG': '#BFBFBF',
    'MR': '#FFCCFF',

}

extension = {
    'ESRI Shapefile' : '.shp',
    'GeoJSON' : '.geojson'
}
