# -*- coding: utf-8 -*-
"""Ajouter pdf dialog."""

from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from qgis.gui import QgsFileWidget
from qgis.core import QgsMessageLog, Qgis
from UnderMap.utilities.resources import get_ui_class
#from UnderMap.utilities.utilities import copy_file


FORM_CLASS = get_ui_class('add_pdf_dialog_base.ui')


class DialogAddPDF(QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface=None):
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
        print("working")
        paths = self.select_pdf_action.filePath()
        file_operator = QgsFileWidget.splitFilePaths(paths)
        QgsMessageLog.logMessage('UnderMap', "Ajouter un opérateur: {} avec PDF: {}".format("lalla", ','.join(file_operator)), Qgis.Info)
        #copy_file(name_operator, file_operator)
        self.close()
