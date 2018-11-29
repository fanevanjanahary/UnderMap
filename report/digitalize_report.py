# coding=utf-8
from os.path import join
from qgis.core import QgsVectorLayer, QgsProject
from UnderMap.library_extras import xlsxwriter
from UnderMap.gis.tools import length_feature
from UnderMap.definition.fields import rsx_color
from UnderMap.utilities.utilities import (
    get_project_path,
    get_operators,
    LOGO_PATH
)


def create_head_content(worksheet, title, header_format, cell):
    logo = LOGO_PATH
    cell_to_nbr = ord(cell)
    cell_incr = 0
    item_head = 1
    head = ['Lineaire réseau (m)', 'En fonction', 'Abandonné', 'Total', 'Remarques']

    worksheet.set_column('A:A', 25)
    worksheet.insert_image('A1', logo)
    worksheet.set_column('{}:{}'.format(chr(cell_to_nbr + 12), chr(cell_to_nbr + 12)), 40)
    worksheet.merge_range('{}6:{}6'.format(cell, chr(cell_to_nbr + 11)), head[0], header_format)
    worksheet.merge_range('{}6:{}8'.format(chr(cell_to_nbr + 12), chr(cell_to_nbr + 12)), head[4], header_format)
    worksheet.merge_range('B2:{}2'.format(chr(cell_to_nbr + 11)), 'UnderMap', header_format)


    while item_head < 4 and cell_incr < 9:
        cell_head = cell_to_nbr + cell_incr
        worksheet.merge_range('{}7:{}7'.format(chr(cell_head), chr(cell_head+3)), head[item_head], header_format)
        cell_incr += 4
        item_head += 1
        for i, item in enumerate(['A', 'B', 'C', 'Total']):
            if item == 'Total':
                worksheet.write(7, cell_head + i - 65, item, header_format)
            else:
                 worksheet.write(7, cell_head + i - 65, 'Classe {}'.format(item), header_format)
    if cell == 'E':
        worksheet.set_column('B:B', 20)
        worksheet.merge_range('A6:A8', 'Opérateur', header_format)
        worksheet.merge_range('B6:B8', 'Etat', header_format)
        worksheet.merge_range('C6:C8', 'Pages Traitées', header_format)
        worksheet.merge_range('D6:D8', 'Type de réseau', header_format)
        worksheet.merge_range('B3:{}3'.format(chr(cell_to_nbr + 11)), title, header_format)

    if cell == 'F':
        worksheet.merge_range('A6:A8', 'Etat', header_format)
        worksheet.merge_range('B6:D6', 'Pages', header_format)
        worksheet.merge_range('B7:B8', 'Traitées', header_format)
        worksheet.merge_range('C7:C8', 'Ingorées', header_format)
        worksheet.merge_range('D7:D8', 'Total', header_format)
        worksheet.merge_range('E6:E8', 'Type de réseau', header_format)
        worksheet.merge_range('B3:{}3'.format(chr(cell_to_nbr + 11)), title, header_format)

    if cell == 'B':
        worksheet.merge_range('A6:A8', 'Réseau', header_format)
        worksheet.merge_range('B3:{}3'.format(chr(cell_to_nbr + 11)), title, header_format)


def create_content(worksheet, worksheet_title, cell_header, cell_format, row, column, layer):
    """ Création de contenue type de réseau

    :param column: Colonne où ça va inserser
    :type column: str

    :param row: Ligne où ça va inserser
    :type row: int

    :param worksheet: La feuille de travail
    :type worksheet: Worksheet

    :param layer: une couche
    :type layer: QgsVectorLayer
    """

    create_head_content(worksheet, worksheet_title, cell_header, column)
    cell_letter_to_nbr = ord(column)
    cell_cord = cell_letter_to_nbr - 65
    field = layer.dataProvider().fieldNameIndex('Reseau')
    values = sorted(layer.uniqueValues(field))
    row_formula = row
    for i, item_value in enumerate(values):
        worksheet.write(row + i, cell_cord - 1, item_value, cell_format.set_fg_color(rsx_color[item_value]))
        row_formula  += i
        col_liner = 0
        sum_by_class = 0
        for j, item_class in enumerate(['A', 'B', 'C']):
             worksheet.write(row + i, cell_cord + j, length_feature(layer, item_value, item_class,0),
                             cell_format.set_fg_color(rsx_color[item_value]))
             worksheet.write(row + i, cell_cord + 4 +j, length_feature(layer, item_value, item_class,1),
                             cell_format.set_fg_color(rsx_color[item_value]))
        while sum_by_class<3 and col_liner < 9:
            cell_length_class = cell_letter_to_nbr + col_liner
            cell_by_class = cell_letter_to_nbr + sum_by_class
            cell_sum_by_func = cell_cord + col_liner + 3
            cell_sum_by_class = cell_cord + sum_by_class + 8
            worksheet.write_formula(row_formula, cell_sum_by_func,
                            '=SUM(${}%d:${}%d)'.format(chr(cell_length_class), chr(cell_length_class + 2)) %
                            (row_formula + 1, row_formula +1),
                            cell_format.set_fg_color(rsx_color[item_value]))
            worksheet.write_formula(row_formula, cell_sum_by_class,
                            '=${}%d+${}%d'.format(chr(cell_by_class), chr(cell_by_class + 4)) %
                            (row_formula + 1, row_formula +1),
                            cell_format.set_fg_color(rsx_color[item_value]))
            col_liner += 4
            sum_by_class += 1
    return row_formula


def export_report_file(path):

    name_file = QgsProject.instance().baseName()
    file = join(path, name_file+'.xlsx')
    workbook = xlsxwriter.Workbook(file)
    operators_path = join(path, 'RSX')
    operators_content = get_operators(operators_path)

    cell_header = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#bebebe'})

    cell_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
        })

    worksheets = ['Recapitulatif-Operateurs', 'Recapitulatif-Réseaux']

    for i_worksheet, item_worksheet in enumerate(worksheets):
        worksheet = workbook.add_worksheet(item_worksheet)
        for i, item in enumerate(operators_content):
            layer_path = join(operators_path, item, 'SHP', item)
            layer = QgsVectorLayer(layer_path+".shp")
            if i_worksheet == 0:
                last_row = create_content(worksheet, 'Recapitulatif par opérateur', cell_header, cell_format, 8+i, 'E', layer)
                worksheet.write(last_row, 0, item)
            if i_worksheet == 1:
                create_content(worksheet, 'Recapitulatif par réseau', cell_header, cell_format, 8+i, 'B', layer)
                worksheet_rsx = workbook.add_worksheet(item)
                create_content(worksheet_rsx, item, cell_header, cell_format, 8, 'F', layer)

    workbook.close()
