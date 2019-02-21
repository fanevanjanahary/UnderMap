# coding=utf-8

"""les actions"""
import os
from os.path import join, basename, exists
from qgis.core import QgsProject, QgsVectorLayer
from UnderMap.library_extras import xlsxwriter
from UnderMap.report.digitalize_report import export_report_file
from UnderMap.utilities.utilities import (
    PROJECT_GROUP,
    PDF_SUB_DIR,
    OPERATOR_SUB_DIR,
    create_dir,
    copy_file,
    get_project_path,
    groups_to_array,
    get_elements_name
    )
from UnderMap.gis.tools import (
    save_as_shp,
    add_layer_in_group,
    create_group,
    create_layer,
    categorized_layer,
    get_group,
    export_layer_as
    )


def initialise_pdf(from_operators):
    """ Initialiser PDF

    :param from_operators: Chemin des données brutes
    :return:
    """
    create_group()
    for item in get_elements_name(from_operators, True, None):
        operator_dir = join(from_operators, item)
        create_operator(item, operator_dir)


def create_operator(name, pdf):
    """ Creation d'un opeérateur

    :param name: Le nom de l'opérateur
    :type name: str


    :param pdf: Le(s) fichier(s) pdf associé(s) à un opérateur
    :type pdf: str
    """
    root = join(get_project_path(), PROJECT_GROUP[2])
    operator_dir = join(root, name)
    qgis_groups = get_group()
    tif_group = qgis_groups.findGroup(PROJECT_GROUP[3])
    if tif_group is not None:
        if qgis_groups.findGroup(name) is None:
            tif_group.addGroup(name)
    if not exists(root):
        os.makedirs(root)
    if not exists(join(root, name)):
        for item_operator_sub_dir in OPERATOR_SUB_DIR:
            os.makedirs(join(operator_dir, item_operator_sub_dir))
            if item_operator_sub_dir == 'SHP':
                layer = create_layer(join(operator_dir, item_operator_sub_dir), name)
                add_layer_in_group(layer, qgis_groups.findGroup(PROJECT_GROUP[2]), 'line_style.qml')
            elif item_operator_sub_dir == 'PDF':
                for item_sous_pdf in PDF_SUB_DIR:
                    sub_pdf = join(operator_dir, item_operator_sub_dir, item_sous_pdf)
                    os.makedirs(sub_pdf)
                copy_file(pdf, join(operator_dir, item_operator_sub_dir), ".pdf")
    else:
        pass


def initialise_fdp(dxf_file):
    """ Initialisation d'un fond de plan

    :param dxf_file: Le fichier dxf
    :type dxf_file: str
    """
    create_dir(get_project_path(), 'FDP/SHP')
    copy_file(dxf_file[0], join(get_project_path(), 'FDP'), None)
    if get_group().findGroup(PROJECT_GROUP[1]) is None :
        get_group().addGroup(PROJECT_GROUP[1])
    shp_path = join(get_project_path(),'FDP/SHP',basename(dxf_file[0].replace('dxf', 'shp')))
    dxf_info = "|layername=entities|geometrytype=LineString"
    layer_name = basename(dxf_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(dxf_file[0]+dxf_info, layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, dxf_vl.crs()):
        layer = QgsVectorLayer(shp_path,  layer_name)
        layer.setCrs(QgsProject.instance().crs())
        add_layer_in_group(layer, get_group().findGroup(PROJECT_GROUP[1]),None)
        categorized_layer(layer, 'Layer')


def initialise_emprise(kml_file):
    """ Initialisation d'une emprise

    :param kml_file: Le fichier kml
    :type kml_file: str
    """
    qgis_groups = get_group()
    create_dir(get_project_path(), 'FDP/SHP')
    copy_file(kml_file[0], join(get_project_path(), 'FDP'), None)
    if qgis_groups.findGroup(PROJECT_GROUP[1]) is None:
        qgis_groups.addGroup(PROJECT_GROUP[1])
    shp_path = join(get_project_path(), 'FDP/SHP', basename(kml_file[0].replace('kml', 'shp')))
    layer_name = basename(kml_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(kml_file[0], layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, QgsProject.instance().crs()):
        layer = QgsVectorLayer(shp_path,  layer_name)
        add_layer_in_group(layer, qgis_groups.findGroup(PROJECT_GROUP[1]), 'emprise_style.qml')


def export_xlsx_report(path):
    """Générer le fichier de rapport xlsx

    :param path: chemin du projet
    :return: l'état de géneration
    :rtype: Boolean
    """
    name_file = QgsProject.instance().baseName()
    file = join(path, name_file+'.xlsx')
    workbook = xlsxwriter.Workbook(file)

    try:
        export_report_file(workbook, path)
        return True
    except PermissionError:
        return False

def export_as_geojson(path):

    rsx_path = join(path, 'RSX')

    for root, dirs, files in os.walk(rsx_path):
        for file in files:
            if  root[-3:] == 'SHP' and file.endswith(".shp"):
                to_dir = join(root[0:-3], 'GEOJSON')
                create_dir(to_dir, None)
                layer = root + os.sep +file
                export_layer_as(layer, "GeoJSON", ".geojson", to_dir)
    return True
