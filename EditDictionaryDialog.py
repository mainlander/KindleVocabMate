import json
import os.path
from pathlib import Path

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui_EditDictionaryDialog import Ui_EditDictionaryDialog

class EditDictionaryDialog(QDialog, Ui_EditDictionaryDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.current_dictionary_index = -1

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



    def accept(self):
        super().accept()

    def reject(self):
        super().reject()
