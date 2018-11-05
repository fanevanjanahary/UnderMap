# coding=utf-8

"""les actions"""
import os
from os.path import  join, basename, exists
from qgis.core import QgsProject, QgsVectorLayer, QgsVectorFileWriter
from UnderMap.utilities.utilities import (
    PDF_SUB_DIR,
    OPERATOR_SUB_DIR,
    QML_PATH,
    create_dir,
    copy_file,
    get_project_path,
    groupes_to_array,
    get_groupe,
    get_operator
    )
from UnderMap.gis.tools import (
    save_as_shp,
    add_layer_in_group,
    create_group,
    create_layer
    )

def initialise_PDF(from_operateur_brute):
    """ Initialiser PDF

    :param from_operateur_brute: Chemin des données brutes
    :return:
    """
    for item in get_operator(from_operateur_brute):
        operateur_dir = join(from_operateur_brute, item)
        print(operateur_dir)
        create_group(from_operateur_brute)
        create_operator(item, operateur_dir)


def create_operator(name, pdf):
    """ Creation d'un opeérateur

    :param name: Le nom de l'opérateur
    :type name: str


    :param pdf: Le(s) fichier(s) pdf associé(s) à un opérateur
    :type pdf: str
    """
    root = join(get_project_path(),'RSX')
    operator_dir = join(root, name)
    if not exists(root):
        os.makedirs(root)
    if not exists(join(root, name)):
        for item_operator_sub_dir in OPERATOR_SUB_DIR:
            os.makedirs(join(operator_dir, item_operator_sub_dir))
            if item_operator_sub_dir == 'SHP':
                layer = create_layer(join(operator_dir, item_operator_sub_dir), name)
                add_layer_in_group(layer, get_groupe().findGroup("RSX"), QML_PATH)
            elif item_operator_sub_dir == 'PDF':
                for item_sous_pdf in PDF_SUB_DIR:
                    sub_pdf = join(operator_dir, item_operator_sub_dir, item_sous_pdf)
                    os.makedirs(sub_pdf)
                copy_file(pdf, join(operator_dir, item_operator_sub_dir), ".pdf")
    else:
        pass


def initialise_FDP(dxf_file):
    """ Initialisation d'un fond de plan

    :param dxf_file: Le fichier dxf
    :type dxf_file: str
    """
    create_dir(get_project_path(), 'FDP/SHP')
    copy_file(dxf_file[0], join(get_project_path(), 'FDP'), None)
    if get_groupe().findGroup("Fond-Plan") is None :
        get_groupe().addGroup("Fond-Plan")
    shp_path = join(get_project_path(),'FDP/SHP',basename(dxf_file[0].replace('dxf', 'shp')))
    dxf_info = "|layername=entities|geometrytype=LineString"
    layer_name = basename(dxf_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(dxf_file[0]+dxf_info, layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, QgsProject.instance().crs()):
        layer = QgsVectorLayer(shp_path,  layer_name)
        add_layer_in_group(layer, get_groupe().findGroup("Fond-Plan"),None)


def initialise_Emprise(kml_file):
    """ Initialisation d'une emprise

    :param kml_file: Le fichier kml
    :type kml_file: str
    """
    create_dir(get_project_path(), 'FDP/SHP')
    copy_file(kml_file[0], join(get_project_path(),'FDP'), None)
    if get_groupe().findGroup("Fond-Plan") is None :
        get_groupe().addGroup("Fond-Plan")
    shp_path = join(get_project_path(), 'FDP/SHP', basename(kml_file[0].replace('kml','shp')))
    layer_name = basename(kml_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(kml_file[0], layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, QgsProject.instance().crs()):
        layer = QgsVectorLayer(shp_path,  layer_name)
        add_layer_in_group(layer, get_groupe().findGroup("Fond-Plan"), None)
