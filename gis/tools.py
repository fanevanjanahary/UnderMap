# coding=utf-8

"""Otuils pour les couches vector"""

from os.path import join
from qgis.core import (
    QgsProject, QgsVectorLayer,
    QgsVectorFileWriter, QgsField, QgsFields,
    QgsWkbTypes, QgsMemoryProviderUtils,
    QgsSymbol, QgsRendererCategory,
    QgsCategorizedSymbolRenderer,
    QgsFeatureRequest
    )

from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    QML_PATH,
    get_project_path,
    groups_to_array,
    )
from UnderMap.definition.fields import(
    operator_def,
    class_def,
    diameter_def,
    rsx_def,
    abandoned_def
    )


def create_field(definition):
    """ Création d'un champ dans un table attributaire

    :param definition: Définition de nom, type, taille et précision d'un champ
    :type definition: definition
    """
    field = QgsField()
    field.setName(definition['name'])
    field.setType(definition['type'])
    field.setPrecision(definition['precision'])
    field.setLength(definition['length'])
    return field


def add_layer_in_group(layer, group, style_file):
    """ Ajouter une couche dans un groupe dans qgis

    :param layer: Couche à ajouter
    :type: layer: QgsVectorLayer

    :param group: Nom de groupe dans qgis
    :type group: str

    :param style_file: Le fichier QML
    :type style_file: str

    """
    QgsProject.instance().addMapLayer(layer, False)
    if layer.isValid():
        group.addLayer(layer)
    if style_file is not None:
        layer.loadNamedStyle(join(QML_PATH, style_file))
       

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

    for g_item in PROJECT_GROUP[:2]:
        if g_item not in groups_to_array(qgis_groups):
            qgis_groups.addGroup(g_item)
    rsx_group = qgis_groups.findGroup(PROJECT_GROUP[0])
    if rsx_group is not None:
        for item in PROJECT_GROUP[2:]:
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
        category = QgsRendererCategory(item, symbol, item)
        categories.append(category)
    renderer = QgsCategorizedSymbolRenderer(attribute_name, categories)
    layer.setRenderer(renderer)


def length_feature(layer, rsx, cls, abd):
    """ Calcul d'un linéaire réseau donné d'une couche

    :param layer: Couche
    :param rsx: Type d'un réseau
    :param cls: Classe d'un réseau
    :param abd: Abandoné ou pas

    :type layer: QgsVectorLayer
    :type rsx: str
    :type cls: str
    :type abd: Integer

    :return: longueur d'un réseau
    :rtype: Double
    """
    expr = '"Reseau" = \'{}\' AND "Classe" = \'{}\' AND "Abandon" = {}'.format(rsx, cls, abd)
    request = QgsFeatureRequest().setFilterExpression(expr)
    sum = 0
    if layer is None:
        return sum
    try:
        features = layer.getFeatures(request)
        for f in features:
            geom = f.geometry()
            sum += geom.length()
        return round(sum)
    except AttributeError:
        return sum

def get_group():
    """  Retourne un groupe d'un projet QGIS

    :return: Un groupe d'un projet QGIS
    :rtype: QgsProject
    """
    root = QgsProject.instance().layerTreeRoot()
    return root

def get_layers_in_group(group_name):
    """Retourne les couches dans un groupé donné
    :param group_name: Le nom de groupe
    :type group_name: str

    :return: Liste des nom de couche
    :rtype: List
    """
    group = get_group().findGroup(group_name)
    return [child.name() for child in group.children()]
