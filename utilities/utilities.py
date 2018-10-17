# coding=utf-8
import os
from os.path import dirname
from qgis.core import QgsProject, QgsVectorLayer

project_groupe = ['Reseau', 'Fond-Plan', 'Impression']
sub_groupe_reseau = ['RSX', 'TIF', 'BUF']

class Util:

    # Prendre les dossiers dans un chemin donné

    def get_operateur(self,path_brute):
        lesdos = []
        for item in os.listdir(path_brute):
            if os.path.isdir(os.path.join(path_brute,item)):
                lesdos.append(item)
        return lesdos

    # Convertir ListGroup en array

    def groupesToArray(self,chl):
        lesgro = []
        for item in chl.children():
            lesgro.append(item.name())
        return lesgro

    # Créer les groupe dans le projet QGIS
    def createGroupe(self, pdf_path):
        root = QgsProject.instance().layerTreeRoot()
        shape_path = os.path.join(dirname(__file__),'resource/shape')
        # add project group if it's not exist
        for g_item in project_groupe:
            if g_item not in self.groupesToArray(root):
                root.addGroup(g_item)

        # add sub group on Reseau
        for item in root.children():
            if item.name() == 'Reseau':
                for s_item in sub_groupe_reseau:
                    if s_item not in self.groupesToArray(item):
                        item.addGroup(s_item)
            for sr_item in item.children():
                if sr_item.name() == 'RSX':
                    for dos in self.get_operateur(pdf_path):
                        layer = QgsVectorLayer(shape_path, dos, "ogr")
                        sr_item.addLayer(layer)





