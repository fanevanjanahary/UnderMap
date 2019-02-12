# -*- coding: utf-8 -*-
"""Ajouter pdf dialog."""

from os.path import join, dirname
from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from qgis.gui import QgsFileWidget
from qgis.core import QgsMessageLog, Qgis
from UnderMap.utilities.resources import get_ui_class
from UnderMap.utilities.utilities import (
        copy_file,
        split_pdf,
        get_project_path,
        PROJECT_GROUP,
        OPERATOR_SUB_DIR
    )


FORM_CLASS = get_ui_class('add_pdf_dialog_base.ui')


class DialogAddPDF(QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface= None):
        """Constructor."""
        super(DialogAddPDF, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        QDialog.__init__(self, parent)
        self.parent = parent
        self.iface = iface
        self.setupUi(self)
        self.select_pdf_action.setDialogTitle("Selectionner le(s) pdf")
        self.select_pdf_action.setFilter("*.pdf")
        self.select_pdf_action.setStorageMode(storageMode=QgsFileWidget.GetMultipleFiles)

        self.select_pdf_action.fileChanged.connect(self.check_form_validation)

        # Set up things for ok button
        self.save_button = self.button_add_pdf.button(QDialogButtonBox.Save)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.accept)

        # Set up things for cancel button
        self.cancel_button = self.button_add_pdf.button(QDialogButtonBox.Cancel)
        self.cancel_button.clicked.connect(self.reject)

    def check_form_validation(self):
        """Slot pour chaque modifs du formulaire."""
        file_operator = self.select_pdf_action.filePath()
        if file_operator != '':
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def accept(self):

        from qgis.utils import iface
        name_exploitant = iface.activeLayer().name()
        paths = self.select_pdf_action.filePath()
        file_operator = QgsFileWidget.splitFilePaths(paths)
        project_path = get_project_path()
        to_dir = join(project_path, PROJECT_GROUP[2], name_exploitant, OPERATOR_SUB_DIR[0])
        print(file_operator)
        QgsMessageLog.logMessage('UnderMap', "Ajout pdf dans: {} avec PDF: {}"
                                 .format(name_exploitant, ','.join(file_operator)), Qgis.Info)
        copy_file(file_operator, to_dir, None)
        self.close()

class DialogSplitPDF(QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface= None):
        """Constructor."""
        super(DialogSplitPDF, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect-
        QDialog.__init__(self, parent)
        self.setWindowTitle("Découpage PDF")
        self.parent = parent
        self.iface = iface
        self.setupUi(self)
        self.select_pdf_action.setDialogTitle("Selectionner le(s) pdf")
        self.select_pdf_action.setFilter("*.pdf")
        self.select_pdf_action.setStorageMode(storageMode=QgsFileWidget.GetMultipleFiles)

        self.select_pdf_action.fileChanged.connect(self.check_form_validation)

        # Set up things for ok button
        self.save_button = self.button_add_pdf.button(QDialogButtonBox.Save)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.accept)

        # Set up things for cancel button
        self.cancel_button = self.button_add_pdf.button(QDialogButtonBox.Cancel)
        self.cancel_button.clicked.connect(self.reject)

    def check_form_validation(self):
        """Slot pour chaque modifs du formulaire."""
        file_operator = self.select_pdf_action.filePath()
        if file_operator != '':
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def accept(self):
        paths = self.select_pdf_action.filePath()
        file_operator = QgsFileWidget.splitFilePaths(paths)
        root_dir = dirname(file_operator[0])
        to_dir = join(root_dir, "PDF DECOUPE")

        """QgsMessageLog.logMessage('UnderMap', "pdf dans: {} avec PDF: {}"
                                 .format(to_dir, ','.join(file_operator)), Qgis.Info)"""
        for item_file in file_operator:

            split_pdf(item_file, to_dir)
        self.close()
