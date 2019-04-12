# coding=utf-8

from .digitalize_report import customize_cell_format
from UnderMap.gis.tools import (
    get_layers_from_folder,
    get_features_by_rsx_and_class
)

BUFFER_SYNTH = ["Longueurs concernées", "BE", "RP", "Résultats"]

def create_head_content(worksheet, workbook):

    titles = [
                "Exploitant concerné",
                "Type",
                "Sensible O/N",
                "Classe de précision",
                "RDV sur site O/N",
                "IC obligatoires O/N"
              ]


    worksheet.write(0, 2, "Lg Tranchée")
    worksheet.write(0, 3, 'S. m²')
    worksheet.write(0, 5, 'COMMUNE:')
    worksheet.write(0, 8, 'URBAINE')
    worksheet.merge_range('G1:H1', 'TRELAZE', customize_cell_format(0, 0, '#D9D9D9', workbook))
    worksheet.write('C6', "Terrassement > 100² ?", customize_cell_format(1, 1, '#CCFF99', workbook))
    worksheet.write('C2', "40", customize_cell_format(1, 1, '#BFBFBF', workbook))
    worksheet.write_formula('D2', '=C2*0.6', customize_cell_format(1, 1, '#BFBFBF', workbook))
    worksheet.write_formula('D6', '=IF(D2>100, "OUI", "NON")', customize_cell_format(1, 1, '#D9D9D9', workbook))
    worksheet.write_formula('G6', '=IF(I1="URBAINE", "OUI", "NON")', customize_cell_format(1, 1, '#D9D9D9', workbook))
    worksheet.merge_range('E6:F6', 'Unité Urbaine ?', customize_cell_format(1, 1, '#99FF99', workbook))
    worksheet.merge_range('H6:I6', 'Réseaux en classe B ou C ?', customize_cell_format(1, 1, '#33CC33', workbook))
    worksheet.write('J6', 'OUI', customize_cell_format(1, 1, '#D9D9D9', workbook))

    worksheet.merge_range('G1:H1', 'URBAINE')
    worksheet.set_column('C:C', 25)

    worksheet.merge_range('A4:B6', "Tableau de Synthèse", customize_cell_format(1, 1, '#FFFFFF', workbook))
    worksheet.merge_range('C4:L4', "N°/ REFERENCE PROJET", customize_cell_format(1, 1, '#FFC090', workbook))
    worksheet.merge_range('C5:L5', 'TYPE DE TRAVAUX ENEDIS', customize_cell_format(1, 1, '#FFC090', workbook))
    worksheet.merge_range('M4:S4', 'DA27/049947', customize_cell_format(1, 1, '#FFC090', workbook))
    worksheet.merge_range('M5:S8', '- COLL IMM - Ilot Nord -Avenue de la Quantiniere TRELAZE ',
                          customize_cell_format(1, 1, '#FFC090', workbook)
                          )
    worksheet.merge_range('A7:B7', "Unité selon l'INSEE", customize_cell_format(1, 1, '#BFBFBF', workbook))
    worksheet.merge_range('C7:L7', '=IF($I$1="URBAINE", "URBAINE", "NON URBAINE")")',
                          customize_cell_format(1, 1, '#BFBFBF', workbook)
                          )
    worksheet.merge_range('C8:L8', '2018112701029PBB', customize_cell_format(1, 1, '#BFBFBF', workbook))
    worksheet.merge_range('A8:B8', "N° GUICHET UNIQUE", customize_cell_format(1, 1, '#BFBFBF', workbook))

    for row in range(3, 14):
        worksheet.set_row(row, 25)

    for i, item in enumerate(titles):
        row = 9 + i
        worksheet.merge_range('A{0}:D{0}'.format(row), item, customize_cell_format(1, 1, '#FFFFCC', workbook))

def operators_content(worksheet):

    for i, layer in enumerate( get_layers_from_folder('SHP') ):
        features = get_features_by_rsx_and_class(layer)
        for i_f, item in enumerate(features):
            worksheet.write(8, 4 + i + i_f, layer.name())
            worksheet.write(9, 4 + i + i_f, item.split('_')[0])
            worksheet.write(11, 4 + i + i_f, item.split('_')[1])

def write_report(workbook):

    worksheet = workbook.add_worksheet("Tableaux de synthèse 1")
    create_head_content(worksheet, workbook)
    operators_content(worksheet)
    workbook.close()
