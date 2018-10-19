# coding=utf-8
import os, shutil
from os.path import dirname
from qgis.core import QgsProject, QgsVectorLayer

project_groupe = ['Reseau', 'Fond-Plan', 'Impression']
sub_groupe_reseau = ['RSX', 'TIF', 'BUF']
sous_d_operateur = ['PDF','SHP', 'TIF']
project_path = QgsProject.instance().readPath("./")
shape_path = dirname(__file__).replace('utilities','resources/shape')
racine = os.path.join(project_path,'RSX----')

#copy shape file at operator dir
def copy_file(from_dir, to_dir):
    for item in os.listdir(from_dir):
        file = os.path.join(from_dir, item)
        shutil.copy(file,to_dir)

# les sous dossier
def create_operartors_subdir(from_operateur_brute):
    for item in get_operator(from_operateur_brute):
        operateur_dir = os.path.join(from_operateur_brute, item)
        if not os.path.exists(os.path.join(racine,item)):
            for item_sous_d in sous_d_operateur:
                os.makedirs(os.path.join(racine,item,item_sous_d))
                if item_sous_d == 'SHP':
                    copy_file(shape_path, os.path.join(racine,item,item_sous_d))
                elif item_sous_d == 'PDF':
                    copy_file(operateur_dir, os.path.join(racine,item,item_sous_d))
                    

#Crée les dossier
def create_operators_dir(from_operateur_brute):
    if not os.path.exists(racine):
        os.makedirs(racine)
        create_operartors_subdir(from_operateur_brute)
    else:
        create_operartors_subdir(from_operateur_brute)

# Prendre les dossiers dans un chemin donné
def get_operator(path_brute):
    lesdos = []
    for item in os.listdir(path_brute):
        if os.path.isdir(os.path.join(path_brute,item)):
            lesdos.append(item)
    return lesdos

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
                for dos in get_operator(from_operateur_brute):
                    layer = QgsVectorLayer(os.path.join(racine,dos,'SHP'), dos, "ogr")
                    QgsProject.instance().addMapLayer(layer, False)
                    if layer.isValid():
                        sr_item.addLayer(layer)
            elif sr_item.name() == 'TIF':
                for dos in get_operator(from_operateur_brute):
                    sr_item.addGroup(dos)
