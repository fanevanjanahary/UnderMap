# coding=utf-8

"""Otuils pour les couches vector"""


from os.path import join, basename, splitext, dirname, exists
from qgis.core import (
    QgsLayerDefinition,QgsProject, QgsVectorLayer, QgsRasterLayer,
    QgsVectorFileWriter, QgsField, QgsFields,
    QgsWkbTypes, QgsMemoryProviderUtils,
    QgsSymbol, QgsRendererCategory,
    QgsCategorizedSymbolRenderer,
    QgsFeatureRequest, QgsApplication,
    QgsCoordinateReferenceSystem, Qgis, QgsMessageLog    
    )

from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    QML_PATH,
    OPERATOR_SUB_DIR,
    create_dir,
    get_project_path,
    groups_to_array,
    get_elements_name
    )
from UnderMap.definition.definitions import(
    operator_def,
    class_def,
    diameter_def,
    rsx_def,
    abandoned_def,
    aerial_def,
    extension
    )
import processing, gdal, glob

from UnderMap.utilities.utilities import get_elements_name


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
            if geom.isNull():
                layer.startEditing()
                layer.deleteFeature(f.id())
                layer.commitChanges()
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
    try:
        return [child.name() for child in group.children()]
    except AttributeError:
        return []


def manage_buffer(path):

    qgis_groups = get_group()
    operators_path = join(path, PROJECT_GROUP[2])
    operators_content = get_elements_name(operators_path, True, None)
    alg = QgsApplication.processingRegistry().algorithmById(
                                     "model:Génerer les buffers")

    for index, item in enumerate(operators_content):
        params = {
            'reseau':'{}/{}/SHP/{}.shp'.format(operators_path, item, item),
            'qgis:deletecolumn_4:sortie':'{}/{}/SHP/{}_BUF.shp'.format(operators_path, item, item)
        }
        result = processing.run(alg, params)
        buf = qgis_groups.findGroup('BUF')
        layer_name = basename(result['qgis:deletecolumn_4:sortie']).replace(".shp", "")
        buf_layer = QgsVectorLayer(result['qgis:deletecolumn_4:sortie'], layer_name, "ogr")
        if buf is not None:
            add_layer_in_group(buf_layer, buf, index, 'buffer_style.qml')


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
        add_layer_in_group(point_layer, points, 0, "point_style.qml")
    else:
        rsx = qgis_groups.findGroup('Reseaux')
        rsx.insertGroup(1, "POINTS CALAGE")
        points = qgis_groups.findGroup('POINTS CALAGE')
        add_layer_in_group(point_layer, points, 0, "point_style.qml")


def export_layer_as(layer, layer_name, layer_format, to_dir):
    """Convertir un fichier sph en format donné
    :param layer: la couche
    :type layer: str ou QgsVectorLayer

    :param layer_name nom du fichier en sorti
    :type layer_name: str

    :param layer_format: le format final
    :type layer_format: str

    :param to_dir: le nouveau chemin
    :type to_dir: str

    """
    if layer_name is None:
        if isinstance(layer, str):
            layer_name = basename(layer).replace(".shp", "")
            layer = QgsVectorLayer(layer, layer_name, "ogr")
        else:
            layer_name = layer.name()

    layer_path = join(to_dir, layer_name+'{}'.format(extension[layer_format]))

    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = layer_format
    options.layerName = layer_name
    options.fileEncoding = 'utf-8'
    QgsVectorFileWriter.writeAsVectorFormat(layer,
                                            layer_path,
                                            options
                                            )
    QgsMessageLog.logMessage("Les fichiers {} sont bien enregistrés dans {}"
                             .format(layer_format, to_dir), 'UnderMap', Qgis.Info)


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
        QgsMessageLog.logMessage("Le(s) fichier(s) tfw sont bien enregistré(s) dans {}"
                                             .format(tif_path), 'UnderMap', Qgis.Info)


def transparency_raster():
    """ Pour changer la transparence des rater dans sur qgis

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


def load_unloaded_data(project_path):

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
                try:
                    if layer_name not in get_layers_in_group(PROJECT_GROUP[2]):
                        add_layer_in_group(layer, qgis_groups.findGroup(PROJECT_GROUP[2]), i_op, 'line_style.qml')
                except TypeError:
                    return
            else:
                try:
                    if layer_name not in get_layers_in_group('BUF'):
                        add_layer_in_group(layer, qgis_groups.findGroup('BUF'), i_op, 'buffer_style.qml')
                except TypeError:
                    return

        # load raster
        tif_path = join(operators_path, item, 'TIF')
        for i_tif, tif_file in enumerate(glob.glob(join(tif_path, '*.tif'))):
            raster_name = basename(tif_file).replace(".tif", "")
            raster = QgsRasterLayer(tif_file, raster_name, 'gdal')
            if raster_name not in get_layers_in_group(item):
                add_layer_in_group(raster, qgis_groups.findGroup(item), i_tif, None)


def merge_features_connected(layer, path):
    """
    Fusionner les entités qui se joignent

    :param layer: la couche à traiter
    :type layer: QgsVectorLayer

    :param path: le chemin pour enregistre
    :type path: str

    """

    layer_name = basename(path).replace(".shp", "")
    # Field calculator parameters
    alg_params_calculator = {
        'FIELD_LENGTH': 20,
        'FIELD_NAME': 'resume',
        'FIELD_PRECISION': 0,
        'FIELD_TYPE': 2,
        'FORMULA': ' \"Reseau\"   || if( \"Diametre\"  is NULL, \'\',  \"Diametre\" ) '
                   '||    \"Classe\"  ||  \"Abandon\"  ',
        'INPUT': layer,
        'NEW_FIELD': True,
        'OUTPUT': 'TEMPORARY_OUTPUT'
    }
    result = processing.run('qgis:fieldcalculator', alg_params_calculator)
    layer = result['OUTPUT']
    field = layer.dataProvider().fieldNameIndex('resume')
    values = layer.uniqueValues(field)

    for item in values:
        expr = '"resume" = \'{}\' '.format(item)
        request = QgsFeatureRequest().setFilterExpression(expr)
        features = layer.getFeatures(request)
        features_el = [i_f for i_f in features]

        for i, feature in enumerate(features_el):
            layer.startEditing()
            layer.changeAttributeValue(feature.id(), field, item+'{}'.format(feature.id()))
            layer.commitChanges ()

        for i, feature in enumerate(features_el):
            inc = 1 + i
            f_geo = feature.geometry()

            if not f_geo.isMultipart():
                f_geo_pts = f_geo.get().points()
                f_geo_start = f_geo.get().startPoint()
                f_geo_end = f_geo.get().endPoint()
            else:
                f_geo_pts = f_geo.get()[0].points()
                f_geo_start = f_geo.get()[0].startPoint()
                f_geo_end = f_geo.get()[0].endPoint()

            if f_geo.isNull():
                layer.startEditing()
                layer.deleteFeature(feature.id())
                layer.commitChanges()
                continue
            # changer l'attribut resume si l'entité joint une autre entité
            for i_feature in features_el[inc:]:
                f_i_geo = i_feature.geometry()
                if not f_i_geo.isMultipart():
                    f_i_geo_pts = f_i_geo.get().points()
                    f_i_geo_start = f_i_geo.get().startPoint()
                    f_i_geo_end = f_i_geo.get().endPoint()
                else:
                    f_i_geo_pts = f_i_geo.get()[0].points()
                    f_i_geo_start = f_i_geo.get()[0].startPoint()
                    f_i_geo_end = f_i_geo.get()[0].endPoint()
                if f_geo.touches(f_i_geo):
                    try:
                        common = [com for com in f_i_geo_pts if com in f_geo_pts][0]
                    except IndexError:
                        continue
                    if common.distance(f_geo_start) == 0.0 or common.distance(f_geo_end) == 0.0:
                        if common.distance(f_i_geo_start) == 0.0 or common.distance(f_i_geo_end) == 0.0:
                            layer.startEditing()
                            layer.changeAttributeValue(feature.id(), field, item+'_connected_{}'.format(i))
                            layer.changeAttributeValue(i_feature.id(), field, item+'_connected_{}'.format(i))
                            layer.commitChanges()

    # Dissolve parameters
    alg_params_dissolve = {
        'INPUT': layer,
        'FIELD': ['resume'],
        'OUTPUT': 'TEMPORARY_OUTPUT'
    }
    result = processing.run('native:dissolve', alg_params_dissolve)

    # Drop Field parameters
    alg_params_deletecolumn = {
        'INPUT': result['OUTPUT'],
        'COLUMN': ['resume'],
        'OUTPUT': 'TEMPORARY_OUTPUT'
    }
    result = processing.run('qgis:deletecolumn', alg_params_deletecolumn)

    if layer.featureCount() != result['OUTPUT'].featureCount():
        merge_features_connected(result['OUTPUT'], path)

    else:

        layer = result['OUTPUT']
        field = layer.dataProvider().fieldNameIndex('Exploitant')
        value = list(layer.uniqueValues(field))[0]
        expr = '"Exploitant" = \'{}\' '.format(value)
        request = QgsFeatureRequest().setFilterExpression(expr)
        features = layer.getFeatures(request)

        # change geometry type
        for f in features:
            geom = f.geometry()
            if geom.isMultipart():
                new_geom = geom.mergeLines()
                layer.startEditing()
                layer.changeGeometry(f.id(), new_geom)
                layer.commitChanges()

        # convert geometry type parameters
        alg_params_convert_geometry_type = {
            'INPUT': layer,
            'TYPE': 2,
            'OUTPUT': 'TEMPORARY_OUTPUT'
        }
        result = processing.run('qgis:convertgeometrytype', alg_params_convert_geometry_type)

        result['OUTPUT'].setCrs(QgsProject.instance().crs())
        create_dir(dirname(path)+'_', None)
        export_layer_as(layer, layer_name, "ESRI Shapefile", dirname(path)+'_')

        # create layer
        # layer = QgsVectorLayer(join(path, layer_name+'.shp'), layer_name, "ogr")
        """
        layer = QgsVectorLayer(path, layer_name, "ogr")
        qgis_groups = get_group()
        add_layer_in_group(layer, qgis_groups.findGroup(PROJECT_GROUP[2]), index , 'line_style.qml')
        """


def get_number_element_rsx_layers(operators_path, operators_content):

    n_elements_rsx = [0]
    value = 0
    for i, item in enumerate(operators_content):
        layer_path = join(operators_path, item, OPERATOR_SUB_DIR[1], item)
        layer = QgsVectorLayer(layer_path+".shp")
        field = layer.dataProvider().fieldNameIndex('Reseau')
        values = sorted(layer.uniqueValues(field))
        if len(values) > 0:
            value += len(values)-1
            n_elements_rsx.append(value)
        else:
            value += len(values)
            n_elements_rsx.append(value)
    return n_elements_rsx


def get_features_by_rsx_and_class(layer):

    alg_params_calculator = {
        'FIELD_LENGTH': 20,
        'FIELD_NAME': 'resume',
        'FIELD_PRECISION': 0,
        'FIELD_TYPE': 2,
        'FORMULA': ' \"Exploitant\" || \'_\' || \"Reseau\" || \'_\'  || \"Classe\"',
        'INPUT': layer,
        'NEW_FIELD': True,
        'OUTPUT': 'TEMPORARY_OUTPUT'
    }
    result = processing.run('qgis:fieldcalculator', alg_params_calculator)
    layer = result['OUTPUT']
    field = layer.dataProvider().fieldNameIndex('resume')

    return layer.uniqueValues(field)


def get_layers_from_folder(folder):
    """ Convert les fichies shp en QgsVectorLayer

    :param folder: dossier où se trouve le fichier à convertir
    :type folder: str

    :return: liste de QgsVectorLayer
    :rtype: list
    """

    layers = []
    project_path = get_project_path()
    operators_path = join(project_path, PROJECT_GROUP[2])
    operators_content = get_elements_name(operators_path, True, None)
    for i_op, item in enumerate(operators_content):
        shp_path = join(operators_path, item, folder)
        if exists(shp_path):
            for shp_file in glob.glob(join(shp_path, '*.shp')):
                layer_name = basename(shp_file).replace(".shp", "")
                layer = QgsVectorLayer(shp_file, layer_name, "ogr")
                layers.append(layer)
        else:
            return None
    return layers
