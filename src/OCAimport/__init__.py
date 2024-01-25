# OCA importer for Krita

import krita # pylint: disable=import-error
from .OCAimport import OCAImport

Scripter.addExtension(OCAImport(krita.Krita.instance())) # pylint: disable=undefined-variable
