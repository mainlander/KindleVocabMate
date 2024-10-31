import json
import os.path
from pathlib import Path

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui_EditDictionaryDialog import Ui_EditDictionaryDialog

class EditDictionaryDialog(QDialog, Ui_EditDictionaryDialog):
    
    updated = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.current_dictionary_index = -1

        # signals
        self.openJifoFileButton.clicked.connect(self.openJifoFile)
        self.openImageButton.clicked.connect(self.openImageFile)

    def setDictionaryIndex(self, index):
        settings = QSettings()
        dicts_json = settings.value("installed_dictionaries", "[]")
        dicts_json_obj = json.loads(dicts_json)
        if index >= 0 and index < len(dicts_json_obj):
            self.current_dictionary_index = index
            cur_dict = dicts_json_obj[index]
            self.dictionaryNameLineEdit.setText(cur_dict['name'])
            self.jifoFileLineEdit.setText(cur_dict['jifo_file'])
            self.imageLineEdit.setText(cur_dict['cover_image'])
            lang_index = self.dictionaryLangComboBox.findText(cur_dict['lang'])
            if lang_index >= 0:
                self.dictionaryLangComboBox.setCurrentIndex(lang_index)

    def openJifoFile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, filter='Json Dictionary ifo (*.jifo)')
        if filePath:
            self.jifoFileLineEdit.setText(filePath)

    def openImageFile(self):
        filePath, fileType = QFileDialog.getOpenFileName(self, filter='Images (*.jpeg *.jpg *.png  *.gif *.tif *.tiff *.bmp *.svg *.webp)')
        if filePath:
            self.imageLineEdit.setText(filePath)

    def accept(self):
        dict_name = self.dictionaryNameLineEdit.text()
        dict_lang = self.dictionaryLangComboBox.currentText()
        jifofile = self.jifoFileLineEdit.text()
        cover = self.imageLineEdit.text()

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

        dict_item = {"name":dict_name, "lang":dict_lang, "jifo_file":jifofile, "cover_image":cover}
        settings = QSettings()
        dicts_json = settings.value("installed_dictionaries", "[]")
        dicts_json_obj = json.loads(dicts_json)
        dicts_json_obj[self.current_dictionary_index] = dict_item
        settings.setValue("installed_dictionaries", json.dumps(dicts_json_obj))

        self.updated.emit()
        super().accept()

    def reject(self):
        super().reject()
