# coding=utf-8
import os, shutil
from os.path import dirname
from qgis.core import QgsProject, QgsVectorLayer, QgsVectorFileWriter


project_groupe = ['Reseau', 'Fond-Plan', 'Impression']
sub_groupe_reseau = ['RSX', 'TIF', 'BUF']
sous_d_operateur = ['PDF','SHP', 'TIF']
shape_path = dirname(__file__).replace('utilities','resources/shape')
qml_path = dirname(__file__).replace('utilities','resources/qml')
sub_pdf = ['A-TRAITER', 'IGNORE', 'UTILE']

# get project path
def get_project_path():
    project_path = QgsProject.instance().readPath("./")
    return project_path


#copy shape file at operator dir
def copy_file(from_dir, to_dir):
    if os.path.isfile(from_dir):
        shutil.copy(from_dir,to_dir)
    else:
        for item in os.listdir(from_dir):
            file = os.path.join(from_dir, item)
            shutil.copy(file,to_dir)

# rename file
def rename_file(dir,name):
    for item in os.listdir(dir):
        extension = os.path.splitext(item)[1]
        new_filename = name+extension
        os.rename(os.path.join(dir,item),os.path.join(dir, new_filename))

# create directory
def create_dir(dir_path,dir_name):
    new_dir = os.path.join(dir_path,dir_name)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


#create operator
def create_operator(name, pdf):
    racine = os.path.join(get_project_path(),'RSX')
    if not os.path.exists(racine):
        os.makedirs(racine)
    if not os.path.exists(os.path.join(racine,name)):
            for item_sous_d in sous_d_operateur:
                os.makedirs(os.path.join(racine,name,item_sous_d))
                if item_sous_d == 'SHP':
                    #shp_to = os.path.join(racine,item,item_sous_d)
                    #default_layer = QgsVectorLayer(shape_path, item, "ogr")
                    #save_as_shp(default_layer, shp_to , QgsProject.instance().crs())
                    copy_file(shape_path, os.path.join(racine,name,item_sous_d))
                    rename_file(os.path.join(racine,name,item_sous_d),name)
                elif item_sous_d == 'PDF':
                    for root, dirs, files in os.walk(pdf):
                        for file in files:
                            if file.endswith(".pdf"):
                                pdf_from_brute = root + os.sep
                                copy_file(pdf_from_brute, os.path.join(racine,name,item_sous_d))
                    for item_sous_pdf in sub_pdf:
                        sous_pdf = os.path.join(racine,name,item_sous_d,item_sous_pdf)
                        os.makedirs(sous_pdf)
    else:
        pass



# get the folder names from the path
def get_operator(path_brute):
    lesoperator_folder_name = []
    for item in os.listdir(path_brute):
        if os.path.isdir(os.path.join(path_brute,item)):
            lesoperator_folder_name.append(item)
    return lesoperator_folder_name

# get groupe in qgis
def get_groupe():
    root = QgsProject.instance().layerTreeRoot()
    return root

# Convertir ListGroup en array
def groupes_to_array(chl):
        lesgro = []
        for item in chl.children():
            lesgro.append(item.name())
        return lesgro

# Créer les groupe dans le projet QGIS
def create_groupe(from_operators_brute):
    racine = os.path.join(get_project_path(),'RSX')
    # add project group if it's not exist
    for g_item in project_groupe:
        if g_item not in groupes_to_array(get_groupe()):
            get_groupe().addGroup(g_item)
    # add sub group on Reseau
    for item in get_groupe().children():
        if item.name() == 'Reseau':
            for s_item in sub_groupe_reseau:
                if s_item not in groupes_to_array(item):
                    item.addGroup(s_item)
        for sr_item in item.children():
            if sr_item.name() == 'RSX':
                for operator_folder_name in get_operator(from_operators_brute):
                    if operator_folder_name not in groupes_to_array(sr_item):
                        layer = QgsVectorLayer(os.path.join(racine,operator_folder_name,'SHP'), operator_folder_name, "ogr")
                        add_layer(layer,sr_item,qml_path)
            elif sr_item.name() == 'TIF':
                for operator_folder_name in get_operator(from_operators_brute):
                    if operator_folder_name not in groupes_to_array(sr_item):
                        sr_item.addGroup(operator_folder_name)


# add layer in qgis groupe
def add_layer (layer,  groupe, style_path):
    QgsProject.instance().addMapLayer(layer, False)
    if layer.isValid():
        groupe.addLayer(layer)
    if style_path is not None:
        layer.loadNamedStyle(os.path.join(style_path,'line_style.qml'))


# convert file to shp
def save_as_shp(file_to_convert, shp_path, crs):
    if file_to_convert.isValid():
        writer = QgsVectorFileWriter.writeAsVectorFormat(file_to_convert, shp_path ,"utf-8", crs,"ESRI Shapefile")
        return 1


# initialise PDF
def initialise_PDF(from_operateur_brute):
    # create folders
    for item in get_operator(from_operateur_brute):
        operateur_dir = os.path.join(from_operateur_brute, item)
        create_operator(item, operateur_dir)
    create_groupe(from_operateur_brute)


# initialise Fond de plan
def initialise_FDP(dxf_file):
    create_dir(get_project_path(),'FDP/SHP')
    copy_file(dxf_file[0],os.path.join(get_project_path(),'FDP'))
    if get_groupe().findGroup("Fond-Plan") is None :
        get_groupe().addGroup("Fond-Plan")
    shp_path = os.path.join(get_project_path(),'FDP/SHP',os.path.basename(dxf_file[0].replace('dxf','shp')))
    dxf_info = "|layername=entities|geometrytype=LineString"
    layer_name = os.path.basename(dxf_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(dxf_file[0]+dxf_info, layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, dxf_vl.crs()) == 1:
        layer = QgsVectorLayer(shp_path,  layer_name)
        add_layer(layer, get_groupe().findGroup("Fond-Plan"),None)

# initialise Emprise
def initialise_Emprise(kml_file):
    create_dir(get_project_path(),'FDP/SHP')
    copy_file(kml_file[0],os.path.join(get_project_path(),'FDP'))
    if get_groupe().findGroup("Fond-Plan") is None :
        get_groupe().addGroup("Fond-Plan")
    shp_path = os.path.join(get_project_path(),'FDP/SHP',os.path.basename(kml_file[0].replace('kml','shp')))
    layer_name = os.path.basename(kml_file[0]).split('.')[0]
    dxf_vl = QgsVectorLayer(kml_file[0], layer_name, "ogr")
    if save_as_shp(dxf_vl, shp_path, QgsProject.instance().crs()) == 1:
        layer = QgsVectorLayer(shp_path,  layer_name)
        add_layer(layer, get_groupe().findGroup("Fond-Plan"),None)


