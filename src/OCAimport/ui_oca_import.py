# references : see 
# https://github.com/RxLaboratory/Bluik/blob/github/bluik/oca.py
# https://krita-artists.org/t/create-layer-via-python/59073
# https://krita-artists.org/t/various-pykrita-questions-3/39888/21?page=2
# https://scripting.krita.org/action-dictionary
# https://scripting.krita.org/lessons/reference-api-krita
# https://krita-artists.org/t/importing-animation-frames-with-python/66093/5
# https://api.kde.org/krita/html/classNode.html#a18aa2116f2bba210fbdd495f169edd99
# says "Currently, the scripting framework does not give access to the animation features." !

import os
import json
import krita
from PyQt5.QtCore import Qt,QStandardPaths
from PyQt5.QtWidgets import (
    QFileDialog,
    QDialog
    )
from PyQt5.QtGui import QImage

class OCAImportDialog(QDialog):
    def __init__(self, parent = None):
        super(OCAImportDialog, self).__init__(parent)
        
    def initialize(self):
        self.importOcaFile()
        
    def importOcaFile(self):
        defaultPath = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filename,_ = QFileDialog.getOpenFileName(self, 'Open file', defaultPath, "oca files (*.oca)")
        if filename:
            print('loading OCA file ' + filename)
            with open(filename, "r") as read_file:
                oca = json.load(read_file)
                title = os.path.basename(filename)
                DPI = 300
                document = Krita.instance().createDocument(oca["width"], oca["height"], title, "RGBA", oca["colorDepth"], "", DPI)
                document.setFramesPerSecond(int(oca["frameRate"]))
                Krita.instance().activeWindow().addView(document)
                self.importLayers(document, oca, os.path.dirname(filename))
                
    def importLayers(self, document, oca, parentDir):
        add_blank_frame_action = Krita.instance().action("add_blank_frame")
        for layer in oca["layers"]:
            if layer["type"] == "paintlayer":
                # layer['width']
                newLayer = document.createNode(layer["name"], "paintLayer")
                document.rootNode().addChildNode(newLayer, None)
                newLayer.setOpacity(layer["opacity"] * 255)
                newLayer.setVisible(layer["visible"])
                newLayer.setPinnedToTimeline(layer["visible"])
                if(layer["animated"]):
                    newLayer.enableAnimation()
                for frame in layer["frames"]:
                    document.setCurrentTime(frame["frameNumber"])
                    add_blank_frame_action.trigger()
                    imagePath = frame["fileName"]
                    image = QImage(parentDir + "/" + imagePath)  # note: pixel format conversion is skipped!
                    if oca["colorDepth"] == "U8":
                        pixelData = bytes(image.constBits().asarray(image.byteCount()))
                        newLayer.setPixelData(pixelData, 0, 0, image.width(), image.height())
        document.refreshProjection()
        document.waitForDone()
