# OCA importer for Krita

from krita import *
from .ui_oca_import import OCAImportDialog

class OCAImport(krita.Extension):
    """The Krita Extension to import OCA format"""
    def __init__(self, parent):
        super(OCAImport, self).__init__(parent)

    def setup(self):
        """Nothing, but required by Krita"""

    def createActions(self, window):
        """Creates the Krita actions"""
        action = window.createAction("OCAimport", i18n("OCA Import")) # pylint: disable=undefined-variable
        action.setToolTip(i18n("Imports animation from OCA file.")) # pylint: disable=undefined-variable
        action.triggered.connect(self.initialize)

    def initialize(self):
        """Initializes the plugin and shows the window"""
        self.dialog = OCAImportDialog()
        self.dialog.initialize()
