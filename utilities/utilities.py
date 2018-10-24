# coding=utf-8
import os, shutil
from os.path import dirname
from qgis.core import QgsProject, QgsVectorLayer

project_groupe = ['Reseau', 'Fond-Plan', 'Impression']
sub_groupe_reseau = ['RSX', 'TIF', 'BUF']
sous_d_operateur = ['PDF','SHP', 'TIF']
project_path = QgsProject.instance().readPath("./")
shape_path = dirname(__file__).replace('utilities','resources/shape')
qml_path = dirname(__file__).replace('utilities','resources/qml')
racine = os.path.join(project_path,'RSX')
sub_pdf = ['A-TRAITER', 'IGNORE', 'UTILE']

#copy shape file at operator dir
def copy_file(from_dir, to_dir):
    for item in os.listdir(from_dir):
        file = os.path.join(from_dir, item)
        shutil.copy(file,to_dir)

# rename file
def rename_file(dir,name):
    for item in os.listdir(dir):
        extension = os.path.splitext(item)[1]
        new_filename = name+extension
        os.rename(os.path.join(dir,item),os.path.join(dir, new_filename))


# les sous operator_folder_namesier
def create_operartors_subdir(from_operateur_brute):
    for item in get_operator(from_operateur_brute):
        operateur_dir = os.path.join(from_operateur_brute, item)
        if not os.path.exists(os.path.join(racine,item)):
            for item_sous_d in sous_d_operateur:
                os.makedirs(os.path.join(racine,item,item_sous_d))
                if item_sous_d == 'SHP':
                    copy_file(shape_path, os.path.join(racine,item,item_sous_d))
                    rename_file(os.path.join(racine,item,item_sous_d),item)
                elif item_sous_d == 'PDF':
                    for root, dirs, files in os.walk(operateur_dir):
                        for file in files:
                            if file.endswith(".pdf"):
                                pdf_from_brute = root + os.sep
                                copy_file(pdf_from_brute, os.path.join(racine,item,item_sous_d))
                    for item_sous_pdf in sub_pdf:
                        sous_pdf = os.path.join(racine,item,item_sous_d,item_sous_pdf)
                        os.makedirs(sous_pdf)
        else:
            pass

                    

#Crée les operator_folder_namesier
def create_operators_dir(from_operateur_brute):
    if not os.path.exists(racine):
        os.makedirs(racine)
        create_operartors_subdir(from_operateur_brute)
    else:
        create_operartors_subdir(from_operateur_brute)

# Prendre les operator_folder_namesiers dans un chemin donné
def get_operator(path_brute):
    lesoperator_folder_name = []
    for item in os.listdir(path_brute):
        if os.path.isdir(os.path.join(path_brute,item)):
            lesoperator_folder_name.append(item)
    return lesoperator_folder_name

# Convertir ListGroup en array
def groupesToArray(chl):
        lesgro = []
        for item in chl.children():
            lesgro.append(item.name())
        return lesgro

# Créer les groupe dans le projet QGIS
def createGroupe(from_operateur_brute):
    root = QgsProject.instance().layerTreeRoot()
    print(shape_path)
    # create folders
    create_operators_dir(from_operateur_brute)
    # add project group if it's not exist
    for g_item in project_groupe:
        if g_item not in groupesToArray(root):
            root.addGroup(g_item)
    # add sub group on Reseau
    for item in root.children():
        if item.name() == 'Reseau':
            for s_item in sub_groupe_reseau:
                if s_item not in groupesToArray(item):
                    item.addGroup(s_item)
        for sr_item in item.children():
            if sr_item.name() == 'RSX':
                for operator_folder_name in get_operator(from_operateur_brute):
                    if operator_folder_name not in groupesToArray(sr_item):
                        layer = QgsVectorLayer(os.path.join(racine,operator_folder_name,'SHP'), operator_folder_name, "ogr")
                        QgsProject.instance().addMapLayer(layer, False)
                        if layer.isValid():
                            sr_item.addLayer(layer)
                            layer.loadNamedStyle(os.path.join(qml_path,'line_style.qml'))
            elif sr_item.name() == 'TIF':

                for operator_folder_name in get_operator(from_operateur_brute):
                    if operator_folder_name not in groupesToArray(sr_item):
                        sr_item.addGroup(operator_folder_name)
