# coding=utf-8

"""Otuils pour les couches vector"""

from os.path import join
from qgis.core import QgsProject, QgsVectorLayer, QgsVectorFileWriter, QgsField, QgsFields, QgsWkbTypes, QgsMemoryProviderUtils
from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    RSX_SUB_GROUP,
    QML_PATH,
    get_project_path,
    groupes_to_array,
    get_groupe,
    get_operator
    )
from UnderMap.definition.fields import(
    operator_def,
    class_def,
    diameter_def,
    rsx_def,
    abandoned_def
    )


def create_field(definition):
    field = QgsField()
    field.setName(definition['name'])
    field.setType(definition['type'])
    field.setPrecision(definition['precision'])
    field.setLength(definition['length'])
    return field


def add_layer_in_group (layer, group, style_path):
    """ Ajouter une couche dans un groupe dans qgis

    :param layer: Couche à ajouter
    :type: layer: QgsVectorLayer

    :param group:
    :param style_path:
    :return:
    """
    QgsProject.instance().addMapLayer(layer, False)
    if layer.isValid():
        group.addLayer(layer)
    if style_path is not None:
        layer.loadNamedStyle(join(style_path, 'line_style.qml'))
       


# convert file to shp
def save_as_shp(file_to_convert, shp_path, crs):
    if file_to_convert.isValid():
        QgsVectorFileWriter.writeAsVectorFormat(file_to_convert, shp_path, "utf-8", crs, "ESRI Shapefile")
        return True
    else:
        return False



def create_group(from_operators_brute):
    """ Creation des groupes dans le projet QGIS

    :param from_operators_brute: Les dossiers de l'operateurs depuis la donnée brute
    :type from_operators_brute: str
    """
    for g_item in PROJECT_GROUP:
        if g_item not in groupes_to_array(get_groupe()):
            get_groupe().addGroup(g_item)
    # add sub group on Reseau
    for item in get_groupe().children():
        if item.name() == 'Reseau':
            for s_item in RSX_SUB_GROUP:
                if s_item not in groupes_to_array(item):
                    item.addGroup(s_item)
        for sr_item in item.children():
            if sr_item.name() == 'TIF':
                for operator_folder_name in get_operator(from_operators_brute):
                    if operator_folder_name not in groupes_to_array(sr_item):
                        sr_item.addGroup(operator_folder_name)


def create_layer(to_dir, layer_name):
    """ Creation de couche

    :param to_dir: le dossier qui va contenier la couche
    :type to_dir: str

    :param layer_name: Nopm de la couche
    :type layer_name: str
    """
    layer_path = join(to_dir, layer_name)
    fields = QgsFields()
    fields.append(create_field(operator_def))
    fields.append(create_field(rsx_def))
    fields.append(create_field(diameter_def))
    fields.append(create_field(class_def))
    fields.append(create_field(abandoned_def))

    layer = QgsMemoryProviderUtils.createMemoryLayer(
        layer_name,
        fields,
        QgsWkbTypes.LineString,
        QgsProject.instance().crs()
    )
    QgsVectorFileWriter.writeAsVectorFormat(layer, layer_path, "utf-8", layer.crs(), "ESRI Shapefile")
    layer_ret = QgsVectorLayer(layer_path+".shp", layer_name, "ogr")
    return layer_ret


