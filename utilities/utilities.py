# coding=utf-8
import os, shutil, typing, csv
from os.path import isfile, dirname, join, isdir, basename, exists
from qgis.core import QgsProject, Qgis, QgsMessageLog
from qgis.gui import QgsMessageBar
from UnderMap.library_extras.PyPDF2 import PdfFileWriter, PdfFileReader

PROJECT_GROUP = ['Reseaux', 'Fond de plan', 'RSX', 'TIF', 'BUF']
OPERATOR_SUB_DIR = ['PDF', 'SHP', 'TIF', 'POINTS CALAGE']
SHP_PATH = dirname(__file__).replace('utilities', 'resources/shape')
QML_PATH = dirname(__file__).replace('utilities', 'resources/qml')
LOGO_PATH = dirname(__file__).replace('utilities', 'resources/logo_futurmap.png')
PDF_SUB_DIR = ['PAGES A TRAITER', 'PAGES ANNEXES']
WORKSHEETS = ['Synthèse_exploitants', 'Synthèse_réseaux']


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
    pdf_treat = join(to_dir, PDF_SUB_DIR[0])
    if  isinstance(from_dir, typing.List):
        for item_path in from_dir:
            if isfile(item_path):
                shutil.copy(item_path, to_dir)
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
            try:
                shutil.copy(from_dir, to_dir)
            except shutil.SameFileError:
                return
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
    if dir_name is not None:
        new_dir = join(dir_path, dir_name)
    else:
        new_dir = dir_path
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)



def get_elements_name(path, type, ext):
    """ Mettre dans une liste le nom de tous les éléments dans une racine donnée

    :param path: Chemin de la racine
    :type path: str

    :param type: True si c'est un dossier, False si c'est un fichier
    :type type: bool

    :return: Liste de dossier
    :rtype: list
    """
    if type is False and ext is not None:
        list_elements_name = [item for item in os.listdir(path) if isfile(join(path, item)) and item.endswith(ext)]
        return list_elements_name
    if type is True:
        list_elements_name = [item for item in os.listdir(path) if isdir(join(path, item))]
        return list_elements_name
    else:
        list_elements_name = [item for item in os.listdir(path) if isfile(join(path, item))]
        return list_elements_name


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
    create_dir(to_dir, None)
    file_name = basename(pdf_file).split('.')[0]
    to_dir = join(to_dir, file_name)
    if pdf_file.endswith(".pdf"):
        QgsMessageLog.logMessage("Découpage du PDF {}".format(pdf_file), 'UnderMap', Qgis.Info)
        pdf_in_file = open(pdf_file, 'rb')
        input_pdf = PdfFileReader(pdf_in_file, strict=False)
        try:
            pages_no = input_pdf.numPages
        except AttributeError:
                        QgsMessageBar.pushCritical('Undermap',
                                                             "Y a une erreur lors de découpage"
                                                            "du fichier:{}".format(pdf_file))
        if pages_no > 1:
            for i in range(pages_no):
                input_pdf = PdfFileReader(pdf_in_file, strict=False)
                output = PdfFileWriter()
                output.addPage(input_pdf.getPage(i))
                with open(to_dir + '_{:02}.pdf'.format(i+1), "wb") as outputStream:
                    try:
                        output.write(outputStream)
                    except AttributeError:
                        QgsMessageBar.pushCritical('Undermap',
                                                             "Y a une erreur lors de découpage"
                                                             "du fichier:{}".format(pdf_file))
                del input_pdf
        else:
            shutil.copy(pdf_file, to_dir+'.pdf')
        pdf_in_file.close()


def count_pdf_file(dir_name):
    """ Compter les fichiers dans le dossier PDF d'un exploitant d'un RSX

    :param dir_name: Le nom de dossier
    :type dir_name: str

    :return: Une liste de nombre
    :rtype: list
    """
    path = get_project_path()
    operator_path = join(path, PROJECT_GROUP[2], dir_name)
    nbr_file = []
    pdf_path_opr = join(operator_path, OPERATOR_SUB_DIR[0])
    for item_dir_pdf in get_elements_name(pdf_path_opr, True, None):
        sub_pdf = join(pdf_path_opr, item_dir_pdf)
        nbr = len([file for file in os.listdir(sub_pdf) if isfile(join(sub_pdf, file)) and file.endswith(".pdf")])
        nbr_file.append(nbr)

    return nbr_file

def count_csv_line(csv_file):
    """ Compter le nombre de line dans un fichier csv

    :param csv_file: le fichier csv à compter
    :type csv_file: str

    :return: Le nombre des ligne du fichier
    :rtype: Integer
    """

    with open(csv_file) as count_file:
        csv_reader = csv.reader(count_file)
        try:
            row_count = sum(1 for row in csv_reader)
        except:
            return 0
        return row_count


def residual_list(gcp_file):
    """

    :param gcp_file:
    :return:
    """

    with open(gcp_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        residual = []
        for row in csv_reader:
            if len(row) >= 7:
                residual.append(row[7])
            else:
                return residual
    return list(map(float, residual[1:]))


def delete_unused_folder(project_path):

    operators_path = join(project_path, PROJECT_GROUP[2])
    operators_content = get_elements_name(operators_path, True, None)
    for i_op, item in enumerate(operators_content):
            path_to_delete = join(operators_path, item, 'SHP_')
            if exists(path_to_delete):
                shutil.rmtree(path_to_delete, ignore_errors=True)
