# -*- coding: utf-8 -*-
"""Zoom to feature dialog."""

from qgis.PyQt.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from UnderMap.utilities.resources import get_ui_class
from UnderMap.gis.tools import zoom_to_selected

FORM_CLASS = get_ui_class('zoom_to_feature_dialog_base.ui')


class DialogZoomToFeature(QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(DialogZoomToFeature, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        QDialog.__init__(self, parent)
        self.parent = parent
        self.iface = iface
        self.setupUi(self)

        self.num_chant.textChanged.connect(self.check_form_validation)

        # Set up things for ok button
        self.ok_button = self.button_zoom_to.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)
        self.ok_button.clicked.connect(self.accept)

        # Set up things for cancel button
        self.cancel_button = self.button_zoom_to.button(QDialogButtonBox.Cancel)
        self.cancel_button.clicked.connect(self.reject)

    def check_form_validation(self):
        """Slot pour chaque modifs du formulaire."""
        num_chant = self.num_chant.value()
        if num_chant != '':
            self.ok_button.setEnabled(True)
        else:
            self.ok_button.setEnabled(False)

    def accept(self):
        """Method invoked when OK button is clicked."""
        num_chant = self.num_chant.value()
        zoom_to_selected(num_chant)
        self.close()
