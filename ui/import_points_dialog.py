# -*- coding: utf-8 -*-
"""Import points dialog."""

from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from qgis.gui import QgsFileWidget
from UnderMap.utilities.resources import get_ui_class
from UnderMap.gis.tools import import_points


FORM_CLASS = get_ui_class('import_points_dialog_base.ui')


class DialogImportPoint(QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(DialogImportPoint, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        QDialog.__init__(self, parent)
        self.parent = parent
        self.iface = iface_  
        self.setupUi(self)
        self.select_points_action.setDialogTitle("Selectionner le(s) csv")
        self.select_points_action.setFilter("*.csv")
        self.select_points_action.setStorageMode(storageMode=QgsFileWidget.GetMultipleFiles)

        # Set up things for ok button
        self.mQgsProjectionSelectionWidget.crsChanged.connect(self.check_form_validation)
        self.select_points_action.fileChanged.connect(self.check_form_validation)

        self.save_button = self.button_import_points.button(QDialogButtonBox.Save)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.accept)

        # Set up things for cancel button
        self.cancel_button = self.button_import_points.button(QDialogButtonBox.Cancel)
        self.cancel_button.clicked.connect(self.reject)



    def check_form_validation(self):
        """Slot pour chaque modifs du formulaire."""
        file_points = self.select_points_action.filePath()
        crs_selected = self.mQgsProjectionSelectionWidget.crs()
        if file_points != '' and crs_selected != '' :
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def accept(self):
        """Method invoked when OK button is clicked."""

        paths = self.select_points_action.filePath()
        file_points = QgsFileWidget.splitFilePaths(paths)
        crs_selected = self.mQgsProjectionSelectionWidget.crs()
        crs = crs_selected.authid()
        import_points(file_points, crs)

        self.close()
