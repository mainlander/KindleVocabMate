import json
import os.path
from pathlib import Path

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui_NewDictionaryDialog import Ui_NewDictionaryDialog

class NewDictionaryDialog(QDialog, Ui_NewDictionaryDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.openJifoFileButton.clicked.connect(self.openJifoFile)
        self.openImageFileButton.clicked.connect(self.openImageFile)

    def openJifoFile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, filter='Json Dictionary ifo (*.jifo)')
        if filePath:
            self.jifoFileLineEdit.setText(filePath)

    def openImageFile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, filter='Images (*.jpeg *.jpg *.png  *.gif *.tif *.tiff *.bmp *.svg *.webp)')
        if filePath:
            self.coverImageLineEdit.setText(filePath)

    def accept(self):
        jifofile = self.jifoFileLineEdit.text()
        cover = self.coverImageLineEdit.text()

        dict_prefix_path = os.path.join(os.path.dirname(jifofile), Path(jifofile).stem)
        for ext in ['jifo', 'jidx', 'jdict']:
            curfile = f'{dict_prefix_path}.{ext}'
            if not os.path.exists(curfile):
                mbox = QMessageBox()
                mbox.critical(self, self.tr('File Not Found'), self.tr('The file "{}" is not found.').format(curfile))
                return

        if not os.path.exists(cover):
            mbox = QMessageBox()
            mbox.critical(self, self.tr('File Not Found'), self.tr('The cover image file "{}" is not found.').format(cover))
            return

        try:
            with open(f'{dict_prefix_path}.jifo', 'r', encoding='utf-8') as f:
                dict_jifo = json.load(f)

            dict_item = {"name":dict_jifo['name'], "lang":dict_jifo['lang'], "jifo_file":jifofile, "cover_image":cover}

            settings = QSettings()
            dicts_json = settings.value("installed_dictionaries", "[]")
            dicts_json_obj = json.loads(dicts_json)
            dicts_json_obj.append(dict_item)
            settings.setValue("installed_dictionaries", json.dumps(dicts_json_obj))
        except:
            print("Load jifo file error.")
            mbox = QMessageBox()
            mbox.critical(self, self.tr('Cannot Load Dictionary'), self.tr('The .jifo file cannot be loaded.'))
            return

        super().accept()

    def reject(self):
        super().reject()
