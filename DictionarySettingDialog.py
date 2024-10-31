import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui_DictionarySettingDialog import Ui_DictionarySettingDialog

from NewDictionaryDialog import NewDictionaryDialog
from EditDictionaryDialog import EditDictionaryDialog

class DictionarySettingDialog(QDialog, Ui_DictionarySettingDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        #self.buttonBox.accepted.connect(self.accept)
        #self.buttonBox.rejected.connect(self.reject)

        self.addButton.clicked.connect(self.addDictionary)
        self.editButton.clicked.connect(self.editDictionary)
        self.deleteButton.clicked.connect(self.deleteDictionary)

        self.settings = QSettings()
        self.dicts_json = self.settings.value('installed_dictionaries', '[]')
        self.updateDictionaryList()

    def updateDictionaryList(self):
        self.dictListWidget.clear()
        self.dicts_json = self.settings.value('installed_dictionaries', '[]')
        dict_json_obj = json.loads(self.dicts_json)
        for dictionary in dict_json_obj:
            dict_item = QListWidgetItem()
            dict_item.setText(dictionary['name'])
            dict_item.setIcon(QIcon(dictionary['cover_image']))
            self.dictListWidget.addItem(dict_item)
        if len(dict_json_obj) > 0:
            self.dictListWidget.setCurrentRow(0)

    def addDictionary(self):
        new_dialog = NewDictionaryDialog(self)
        res = new_dialog.exec()
        print(res)
        self.updateDictionaryList()

    def editDictionary(self):
        select_row = self.dictListWidget.currentRow()
        if select_row >= 0:
            edit_dialog = EditDictionaryDialog(self)
            edit_dialog.setDictionaryIndex(select_row)
            edit_dialog.updated.connect(self.updateDictionaryList)
            res = edit_dialog.exec()
            print(res)
        else:
            mbox = QMessageBox()
            mbox.critical(self, self.tr('No Dictionary Selected'), self.tr('Please select a dictionary you want to edit.'))

    def deleteDictionary(self):
        select_row = self.dictListWidget.currentRow()
        select_text = self.dictListWidget.currentItem().text()
        if select_row >= 0:
            mbox = QMessageBox()
            res = mbox.question(self, self.tr('Delete Dictionary'), self.tr('Are you sure to delete {}?').format(select_text))
            if res == QMessageBox.StandardButton.Yes:
                settings = QSettings()
                dicts_json = settings.value("installed_dictionaries", "[]")
                dicts_json_obj = json.loads(dicts_json)
                del dicts_json_obj[select_row]
                settings.setValue("installed_dictionaries", json.dumps(dicts_json_obj))
                self.updateDictionaryList()


    def accept(self):
        super().accept()

    def reject(self):
        super().reject()
