# coding=utf-8

from .digitalize_report import customize_cell_format

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


    worksheet.write(2, 0, "Lg Tranchée")
    worksheet.write(3, 0, 'S. m²')
    worksheet.write(5, 0, 'COMMUNE:')
    worksheet.write(8, 0, 'COMMUNE:')
    worksheet.merge_range('G1:H1', 'TRELAZE')
    worksheet.merge_range('G1:H1', 'URBAINE')
    worksheet.set_column('C:C', 25)

    worksheet.merge_range('A4:B6', "Tableau de Synthèse")
    worksheet.merge_range('C4:L4', "N°/ REFERENCE PROJET", customize_cell_format(1, 1, '#FFC090', workbook))
    worksheet.set_row('C4:L4', 47)
    worksheet.merge_range('C5:L5', 'TYPE DE TRAVAUX ENEDIS')
    worksheet.set_row('C5:L5', 47)
    worksheet.merge_range('M4:S4', 'DA27/049947')
    worksheet.set_row('M4:S4', 47)
    worksheet.merge_range('M5:S8', '- COLL IMM - Ilot Nord -Avenue de la Quantiniere TRELAZE ')
    worksheet.merge_range('A7:B7', "Unité selon l'INSEE")
    worksheet.set_row('A7:B7', 47)
    worksheet.merge_range('C7:L7', '=IF($I$1="URBAINE", "URBAINE", "NON URBAINE")")')
    worksheet.set_row('C7:L7', 47)
    worksheet.merge_range('C8:L8', '2018112701029PBB')
    worksheet.set_row('C8:L8', 47)
    worksheet.merge_range('A8:B8', "N° GUICHET UNIQUE")
    worksheet.set_row('A8:B8', 47)

    for i, item in enumerate(titles):
        row = 9 + i
        worksheet.merge_range('A{0}:D{0}'.format(row), item)
        worksheet.set_row('A{0}:D{0}'.format(row), 47)


def write_report(workbook):

    worksheet = workbook.add_worksheet("Tableaux de synthèse 1")
    create_head_content(worksheet, workbook)
    workbook.close()
