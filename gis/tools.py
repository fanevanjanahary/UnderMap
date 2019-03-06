# coding=utf-8

"""Otuils pour les couches vector"""

import os
from os.path import join, basename, exists, splitext
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsRasterLayer,
    QgsVectorFileWriter, QgsField, QgsFields,
    QgsWkbTypes, QgsMemoryProviderUtils,
    QgsSymbol, QgsRendererCategory,
    QgsCategorizedSymbolRenderer,
    QgsFeatureRequest, QgsApplication,
    QgsProcessingContext, QgsProcessingFeedback,
    QgsCoordinateReferenceSystem, Qgis, QgsMessageLog
    )

from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    QML_PATH,
    create_dir,
    get_project_path,
    groups_to_array,
    get_elements_name
    )
from UnderMap.definition.fields import(
    operator_def,
    class_def,
    diameter_def,
    rsx_def,
    abandoned_def,
    aerial_def
    )
import processing, gdal, glob


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


def add_layer_in_group(layer, group, position, style_file):
    """ Ajouter une couche dans un groupe dans qgis

    :param layer: Couche à ajouter
    :type: layer: QgsVectorLayer

    :param group: Nom de groupe dans qgis
    :type group: str

    :param position: la place où on va mettre la couche
    :type position: int

    :param style_file: Le fichier QML
    :type style_file: str

    """
    QgsProject.instance().addMapLayer(layer, False)
    if layer.isValid():
        group.insertLayer(position, layer)
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

    for i, g_item in enumerate(reversed(PROJECT_GROUP[:2])):
        if g_item not in groups_to_array(qgis_groups):
            qgis_groups.insertGroup(i,g_item)
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
    # fields.append(create_field(aerial_def))

    layer = QgsMemoryProviderUtils.createMemoryLayer(
        layer_name,
        fields,
        QgsWkbTypes.LineString,
        QgsProject.instance().crs()
    )

    QgsVectorFileWriter.writeAsVectorFormat(layer, layer_path, "utf-8", layer.crs(), "ESRI Shapefile")
    layer_ret = QgsVectorLayer(layer_path+".shp", layer_name, "ogr")
    if layer_ret.crs().authid() != QgsProject.instance().crs().authid():
        layer_ret.setCrs(QgsProject.instance().crs())
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

def manage_buffer(path):

    qgis_groups = get_group()
    operators_path = join(path, PROJECT_GROUP[2])
    operators_content = get_elements_name(operators_path, True, None)
    alg = QgsApplication.processingRegistry().algorithmById(
                                     "model:Génerer les buffers")

    for item in operators_content:
        params = {
            'reseau':'{}/{}/SHP/{}.shp'.format(operators_path, item, item),
            'qgis:deletecolumn_4:sortie':'{}/{}/SHP/{}_BUF.shp'.format(operators_path, item, item)
        }
        result = processing.run(alg, params)
        buf = qgis_groups.findGroup('BUF')
        layer_name = basename(result['qgis:deletecolumn_4:sortie']).replace(".shp", "")
        buf_layer = QgsVectorLayer(result['qgis:deletecolumn_4:sortie'], layer_name, "ogr")
        if buf is not None:
            add_layer_in_group(buf_layer, buf, 'buffer_style.qml')


def import_points(files, crs):

    qgis_groups = get_group()
    alg = QgsApplication.processingRegistry().algorithmById(
                                     "model:ImportPoints")

    for item in files:
        layer_point = item.replace(".csv", ".shp")
        params = {
            'fichiertexte':item,
            'systemedufichiertexte':QgsCoordinateReferenceSystem(crs),
            'native:reprojectlayer_1:Points transformés':layer_point
        }
        result = processing.run(alg, params)
    layer_name = basename(result['native:reprojectlayer_1:Points transformés']).replace(".shp", "")
    point_layer = QgsVectorLayer(result['native:reprojectlayer_1:Points transformés'], layer_name, "ogr")
    points = qgis_groups.findGroup('POINTS CALAGE')
    if points is not None:
        add_layer_in_group(point_layer, points, "point_style.qml")
    else:
        rsx = qgis_groups.findGroup('Reseaux')
        rsx.insertGroup(1, "POINTS CALAGE")
        points = qgis_groups.findGroup('POINTS CALAGE')
        add_layer_in_group(point_layer, points, "point_style.qml")

def export_layer_as(layer, layer_format, ext, to_dir):
    """Convertir un fichier sph en format donné
    :param layer: la couche
    :type layer: str

    :param layer_format: le format final
    :type layer_format: str

    :param to_dir: le nouveau chemin
    :type to_dir: str

    """

    layer_name = basename(layer).replace(".shp", "")
    layer = QgsVectorLayer(layer, layer_name, "ogr")
    layer_path = join(to_dir, layer_name+'{}'.format(ext))
    if exists(layer_path):
        os.remove(layer_path)
    QgsVectorFileWriter.writeAsVectorFormat(layer, layer_path, "utf-8", layer.crs(), layer_format)
    QgsMessageLog.logMessage('Les fichiers GeoJSON sont bien enregistrés dans {}'
                                             .format(to_dir), 'UnderMap', Qgis.Info)


def export_tfw(path):

    operators_path = join(path, PROJECT_GROUP[2])
    operators_content = get_elements_name(operators_path, True, None)

    for item in operators_content:
        tif_path = join(operators_path, item, 'TIF')
        for infile in glob.glob(join(tif_path, '*.tif')):
            src = gdal.Open(infile)
            xform = src.GetGeoTransform()

            edit1=xform[0]+xform[1]/2
            edit2=xform[3]+xform[5]/2

            tfw = open(splitext(infile)[0] + '.tfw', 'wt')
            tfw.write("%0.8f\n" % xform[1])
            tfw.write("%0.8f\n" % xform[2])
            tfw.write("%0.8f\n" % xform[4])
            tfw.write("%0.8f\n" % xform[5])
            tfw.write("%0.8f\n" % edit1)
            tfw.write("%0.8f\n" % edit2)
            tfw.close()
        QgsMessageLog.logMessage('Le(s) fichier(s) tfw sont bien enregistré(s) dans {}'
                                             .format(tif_path), 'UnderMap', Qgis.Info)


def transparency_raster():
    """ Pour changer la transparence des rater dans sur qgis

    :param percent: la valeur de pourcentage
    :type percent: int

    """
    tif_children = get_layers_in_group('TIF')
    percent = None
    for item in tif_children:
        tif_child = get_group().findGroup(item)
        for child in tif_child.children():
            if child.layer().renderer().opacity() <= 0.5:
                percent = 1
            elif child.layer().renderer().opacity() >= 1:
                percent = 0.5
            child.layer().renderer().setOpacity(percent)
            child.layer().triggerRepaint()


def zoom_to_selected(num_chant):
    from qgis.utils import iface
    layer = iface.activeLayer()
    expr = '"num_chant" = \'{}\''.format(num_chant)
    request = QgsFeatureRequest().setFilterExpression(expr)
    features = layer.getFeatures(request)
    for item in features:
        layer.select(item.id())


def load_uloaded_data(project_path):

    operators_path = join(project_path, PROJECT_GROUP[2])
    try:
        operators_content = get_elements_name(operators_path, True, None)
    except FileNotFoundError:
        return
    qgis_groups = get_group()
    for i_op, item in enumerate(operators_content):
        # load vectors
        shp_path = join(operators_path, item, 'SHP')
        for shp_file in glob.glob(join(shp_path, '*.shp')):

            layer_name = basename(shp_file).replace(".shp", "")
            layer = QgsVectorLayer(shp_file, layer_name, "ogr")
            if layer.geometryType() == 1:
                if layer_name not in get_layers_in_group('RSX'):
                    add_layer_in_group(layer, qgis_groups.findGroup('RSX'), i_op, 'line_style.qml')
            else:
                if layer_name not in get_layers_in_group('BUF'):
                    add_layer_in_group(layer, qgis_groups.findGroup('BUF'), i_op, 'buffer_style.qml')

        #load raster
        tif_path = join(operators_path, item, 'TIF')
        for i_tif, tif_file in enumerate(glob.glob(join(tif_path, '*.tif'))):
            raster_name = basename(tif_file).replace(".tif", "")
            raster = QgsRasterLayer(tif_file, raster_name, 'gdal')
            if raster_name not in get_layers_in_group(item):
                add_layer_in_group(raster, qgis_groups.findGroup(item), i_tif, None)
