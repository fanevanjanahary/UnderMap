# coding=utf-8

from .digitalize_report import customize_cell_format
from UnderMap.gis.tools import (
    get_layers_from_folder,
    get_features_by_rsx_and_class
)

from UnderMap.definition.definitions import buffer_synth

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

    worksheet.merge_range('C7:L7', 'URBAINE',
                          customize_cell_format(1, 1, '#BFBFBF', workbook)
                          )
    """
    worksheet.write_array_formula(6, 2, 6, 12, '{=IF($I$1="URBAINE", "URBAINE", "NON URBAINE")")}',
                          customize_cell_format(1, 1, '#BFBFBF', workbook)
                          )
    """
    worksheet.merge_range('C8:L8', '2018112701029PBB', customize_cell_format(1, 1, '#BFBFBF', workbook))
    worksheet.merge_range('A8:B8', "N° GUICHET UNIQUE", customize_cell_format(1, 1, '#BFBFBF', workbook))


    for row in range(3, 14):
        worksheet.set_row(row, 25)

    worksheet.set_row(14, 27)

    for i, item in enumerate(titles):
        row = 9 + i
        worksheet.merge_range('A{0}:D{0}'.format(row), item, customize_cell_format(1, 1, '#FFFFCC', workbook))
    wrap = customize_cell_format(1, 1, '#d9d9d9', workbook)
    worksheet.merge_range('A15:D15',
                          'Proposition du BE - Choix et Validation du RP - Résultats entreprise IC',
                          wrap
                          )
    wrap.set_text_wrap()
def operators_content(worksheet, workbook):

    features = []
    cell_s = 4

    for i, layer in enumerate( get_layers_from_folder('SHP') ):
        features += [ item_f for item_f in get_features_by_rsx_and_class(layer) ]

    for item_f, i in zip(features, range(0, len(features)*4, +4) ):

        worksheet.write(8, cell_s + i, item_f.split('_')[0] )
        worksheet.write(9, cell_s + i,  item_f.split('_')[1] )
        worksheet.write(11, cell_s + i, item_f.split('_')[2] )

        for i_buff, buff in enumerate(buffer_synth):
            worksheet.write(14, cell_s + i_buff + i, buff,  customize_cell_format(1, 1, buffer_synth[buff] , workbook))


def write_report(workbook):

    worksheet = workbook.add_worksheet("Tableaux de synthèse 1")
    create_head_content(worksheet, workbook)
    operators_content(worksheet, workbook)
    workbook.close()
