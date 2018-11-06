# coding=utf-8
import os, shutil, typing
from os.path import isfile, dirname, join, isdir, basename
from qgis.core import QgsProject, QgsVectorLayer, QgsVectorFileWriter, Qgis, QgsMessageLog
from qgis.gui import QgsMessageBar
from UnderMap.library_extras.PyPDF2 import PdfFileWriter, PdfFileReader

PROJECT_GROUP = ['Reseau', 'Fond-Plan', 'Impression']
RSX_SUB_GROUP = ['RSX', 'TIF', 'BUF']
OPERATOR_SUB_DIR = ['PDF', 'SHP', 'TIF']
SHP_PATH = dirname(__file__).replace('utilities', 'resources/shape')
QML_PATH = dirname(__file__).replace('utilities', 'resources/qml')
PDF_SUB_DIR = ['A-TRAITER', 'IGNORE', 'UTILE']


def get_project_path():
    """ Pour avoir le chemin du fichier projet sur QGIS

    :return: Le chemin du projet
    :rtype: str
    """
    project_path = QgsProject.instance().readPath("./")
    return project_path


def copy_file(from_dir, to_dir, file_type):
    """ Copier un ou plusieur fichiers

    :param from_dir: L'origine d'un fichier à copier
    :type from_dir: str

    :param to_dir: La destination de copie
    :type to_dir: str

    :param file_type: Type du fichier à copier
    :type file_type: str
    """
    pdf_treat = join(to_dir, 'A-TRAITER')
    if  isinstance(from_dir, typing.List):
        for item_path in from_dir:
            if isfile(item_path.replace('"', '')):
                shutil.copy(item_path.replace('"', ''), to_dir)
                if item_path.endswith(".pdf"):
                    split_pdf(item_path, pdf_treat)
    elif isdir(from_dir):
        for root, dirs, files in os.walk(from_dir):
            for file in files:
                if file.endswith(file_type):
                    pdf_from_brute = root + os.sep + file
                    shutil.copy(pdf_from_brute, to_dir)
                    if pdf_from_brute.endswith(".pdf"):
                        split_pdf(pdf_from_brute, pdf_treat)
    else:
        if isfile(from_dir):
            shutil.copy(from_dir, to_dir)
            if from_dir.endswith(".pdf"):
                split_pdf(from_dir, pdf_treat)


def rename_file(file, name):
    """ Renommer un fichier

    :param file: Le fichier à renommer
    :type file: str

    :param name: Nouveau nom
    :type name: str
    """
    for item in os.listdir(file):
        extension = os.path.splitext(item)[1]
        new_filename = name+extension
        os.rename(os.path.join(file, item), os.path.join(file, new_filename))


def create_dir(dir_path, dir_name):
    """ Creation d'un dossier

    :param dir_path: Le chemin où le dossier sera créer
    :type dir_path: str

    :param dir_name: Le nom du dossier
    :type dir_name: str
    """
    new_dir = join(dir_path, dir_name)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


def get_operator(path_brute):
    """ Mettre dans une liste le nom de tous les dossier depuis donné bruite

    :param path_brute: Chemin de la donnée brute
    :type path_brute: str

    :return: Liste de dossier
    :rtype: list
    """
    lesoperator_folder_name = []
    for item in os.listdir(path_brute):
        if isdir(join(path_brute, item)):
            lesoperator_folder_name.append(item)
    return lesoperator_folder_name


def get_group():
    """  Retourne un groupe d'un projet QGIS

    :return: Un groupe d'un projet QGIS
    :rtype: QgsProject
    """
    root = QgsProject.instance().layerTreeRoot()
    return root


def groups_to_array(children):
    """ Convertition de ListGroupe en liste array

    :param children: Groupe de QGIS
    :type children: QgsProject
    :return: Liste de groupes
    :rtype: List
    """
    groups = []
    for item in children.children():
        groups.append(item.name())
    return groups


def split_pdf(pdf_file, to_dir):
    """ Découpage par page d'un fichier pdf

    :param pdf_file: Fichier à découper
    :type: pdf_file: str

    :param to_dir: le dossier pour sauvegarder les fichier àpres le découpage
    :type to_dir: str
    """
    file_name = basename(pdf_file).split('.')[0]
    to_dir = join(to_dir, file_name)
    if pdf_file.endswith(".pdf"):
        QgsMessageLog.logMessage("Découpage du PDF {}".format(pdf_file), 'UnderMap', Qgis.Info)
        pdf_in_file = open(pdf_file, 'rb')
        input_pdf = PdfFileReader(pdf_in_file, strict=False)
        pages_no = input_pdf.numPages
        del input_pdf
        if pages_no > 1:
            for i in range(pages_no):
                input_pdf = PdfFileReader(pdf_in_file, strict=False)
                output = PdfFileWriter()
                output.addPage(input_pdf.getPage(i))
                with open(to_dir + '_{:02}.pdf'.format(i+1), "wb") as outputStream:
                    try:
                        output.write(outputStream)
                    except AttributeError:
                        QgsMessageBar.messageBar().pushError('Undermap',
                                                             "Y a une erreur lors de découpage"
                                                             "du fichier:{}".format(pdf_file))
                del input_pdf
        else:
            shutil.copy(pdf_file, to_dir+'.pdf')
        pdf_in_file.close()
