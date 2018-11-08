# coding=utf-8

"""Otuils pour les couches vector"""

from os.path import join
from qgis.core import (
    QgsProject, QgsVectorLayer,
    QgsVectorFileWriter, QgsField, QgsFields,
    QgsWkbTypes, QgsMemoryProviderUtils,
    QgsSymbol, QgsRendererCategory,
    QgsCategorizedSymbolRenderer
    )

from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    RSX_SUB_GROUP,
    QML_PATH,
    get_project_path,
    groups_to_array,
    get_group,
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


def add_layer_in_group(layer, group, style_path):
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
       

def save_as_shp(file_to_convert, shp_path, crs):
    if file_to_convert.isValid():
        QgsVectorFileWriter.writeAsVectorFormat(file_to_convert, shp_path, "utf-8", crs, "ESRI Shapefile")
        return True
    else:
        return False


def create_group():
    """ Creation des groupes dans le projet QGIS

    """
    qgis_groups = get_group()

    for g_item in PROJECT_GROUP:
        if g_item not in groups_to_array(qgis_groups):
            qgis_groups.addGroup(g_item)
    rsx_group = qgis_groups.findGroup("Reseau")
    if rsx_group is not None:
        for item in RSX_SUB_GROUP:
            if qgis_groups.findGroup(item) is None:
                rsx_group.addGroup(item)


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


def categorized_layer(layer, attribute_name):
    """ Categorisation d'une couche

    :param layer: La couche à catégoriser
    :type layer: QgsVectorLayer

    :param attribute_name: Nom de colonne à classifier
    :type attribute_name: str
    """
    field = layer.dataProvider().fieldNameIndex(attribute_name)
    values = sorted(layer.uniqueValues(field))
    categories = []
    for item in values:
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())
        category = QgsRendererCategory(item, symbol, str(item))
        categories.append(category)
    renderer = QgsCategorizedSymbolRenderer(attribute_name, categories)
    layer.setRenderer(renderer)
