# coding=utf-8
from os.path import join
from qgis.core import QgsVectorLayer, QgsProject
from UnderMap.library_extras import xlsxwriter
from UnderMap.gis.tools import length_feature
from UnderMap.definition.fields import rsx_color
from UnderMap.utilities.utilities import (
    get_project_path,
    get_operators,
    LOGO_PATH,
    count_pdf_file
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


def create_content(worksheet, worksheet_title, cell_header, cell_format, row, column, data, layer):
    """ Création de contenue type de réseau

    :param worksheet: La feuille de travail
    :type worksheet: Worksheet

    :param worksheet_title: Titre de la feuille
    :type worksheet_title: str

    :param cell_header: Style entête de la feuille
    :type cell_header: Format

    :param cell_format: Style entête contenue
    :type cell_format: Format

    :param data: Les données à insérer
    :type data: List

     :param column: Colonne où ça va inserser
    :type column: str

    :param row: Ligne où ça va inserser
    :type row: int

    :param layer: une couche
    :type layer: QgsVectorLayer
    """

    create_head_content(worksheet, worksheet_title, cell_header, column)
    cell_letter_to_nbr = ord(column)
    cell_cord = cell_letter_to_nbr - 65
    last_row = row

    for i, item_value in enumerate(data):
        last_row  += i
        col_liner = 0
        sum_by_class = 0
        worksheet.write(row + i, cell_cord - 1, item_value, cell_format.set_fg_color(rsx_color[item_value]))
        for j, item_class in enumerate(['A', 'B', 'C']):

            if layer is None:
                worksheet.write_formula(row + i, cell_cord + j,
                                 '=SUMIF(Recapitulatif_Operateurs!D9:D9999, $A%d, Recapitulatif_Operateurs!{}9:{}9999)'
                                        .format(chr(ord('E') + j),
                                        chr(ord('E') + j)) % (row + i+ 1),
                                 cell_format.set_fg_color(rsx_color[item_value]))
                worksheet.write_formula(row + i, cell_cord + 4 +j,
                                 '=SUMIF(Recapitulatif_Operateurs!D9:D9999, $A%d, Recapitulatif_Operateurs!{}9:{}9999)'
                                        .format(chr(ord('I') + j),
                                        chr(ord('I') + j)) % (row + i+ 1),
                                 cell_format.set_fg_color(rsx_color[item_value]))
            else:
                worksheet.write(last_row, cell_cord + j, length_feature(layer, item_value, item_class,0),
                                cell_format.set_fg_color(rsx_color[item_value]))
                worksheet.write(last_row, cell_cord + 4 +j, length_feature(layer, item_value, item_class,1),
                                cell_format.set_fg_color(rsx_color[item_value]))

        while sum_by_class<3 and col_liner < 9:
            cell_length_class = cell_letter_to_nbr + col_liner
            cell_by_class = cell_letter_to_nbr + sum_by_class
            cell_sum_by_func = cell_cord + col_liner + 3
            cell_sum_by_class = cell_cord + sum_by_class + 8
            worksheet.write_formula(row + i, cell_sum_by_func,
                            '=SUM(${}%d:${}%d)'.format(chr(cell_length_class), chr(cell_length_class + 2)) %
                            (row + i + 1, row + i + 1),
                            cell_format.set_fg_color(rsx_color[item_value]))
            worksheet.write_formula(row + i, cell_sum_by_class,
                            '=${}%d+${}%d'.format(chr(cell_by_class), chr(cell_by_class + 4)) %
                            (row + i + 1, row + i + 1),
                            cell_format.set_fg_color(rsx_color[item_value]))
            col_liner += 4
            sum_by_class += 1
    return last_row


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

    worksheets = ['Recapitulatif_Operateurs', 'Recapitulatif_Réseaux']

    for i_worksheet, item_worksheet in  (worksheets):
        worksheet = workbook.add_worksheet(item_worksheet)
        for i, item in enumerate(operators_content):
            layer_path = join(operators_path, item, 'SHP', item)
            layer = QgsVectorLayer(layer_path+".shp")
            field = layer.dataProvider().fieldNameIndex('Reseau')
            values = sorted(layer.uniqueValues(field))

            if i_worksheet == 0:
                last_row = create_content(worksheet, 'Recapitulatif par opérateur',
                                          cell_header, cell_format, 8 + i, 'E', values, layer)
                worksheet.write(last_row, 0, item)
                worksheet.write(last_row, 2, count_pdf_file(item)[0])

            if i_worksheet == 1:
                worksheet_rsx = workbook.add_worksheet(item)
                create_content(worksheet_rsx, item, cell_header, cell_format, 8, 'F', values, layer)
                for i_count_file, item_count_file in enumerate(count_pdf_file(item)[:2]):
                    worksheet_rsx.write(8, i_count_file + 1, item_count_file)
                worksheet_rsx.write_formula(8, 3,
                            '=${}%d+${}%d'.format('B', 'C')%(8 + 1, 8 + 1)
                )

        if i_worksheet ==  1:
            create_content(worksheet, 'Recapitulatif par réseau', cell_header, cell_format, 8, 'B', rsx_color, None)

    workbook.close()
