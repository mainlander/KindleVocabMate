from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
import MainWindow
import csv

from db import VocabDB
from utils import load_icon_from_url, DateDialog
from installed_dicts import INSTALLED_DICTS

#QApplication.setOrganizationDomain('tw.edu')
QApplication.setOrganizationName('DILA')
QApplication.setApplicationName('KindleVocabMate')

class VocabTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def set_data(self, new_data):
        self._data = new_data
    
    def data(self, index, role):
        row = index.row()
        col = index.column()
        if role in {Qt.ItemDataRole.DisplayRole}:
            book = self._data[row]
            if col == 0:
                return book['word']
            elif col == 1:
                return book['usage']
            elif col == 2:
                return book['lang']
            elif col == 3:
                return book['definition']
            else:
                return None

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 4

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        titles = ['Word', 'Usage', 'Language', 'Definition']
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return titles[section]
            elif orientation == Qt.Orientation.Vertical:
                return f'{section + 1}'
        return super().headerData(section, orientation, role)


class KindleVocabMateMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Signals
        self.connectSignals()

        self.currentVocabDB = None
        self.books = []
        self.all_words = None 
        self.currentWordTableModel = None
        self.max_timestamp = 0

        self.loadDictionaries()

    def connectSignals(self):
        self.dbPathOpenButton.clicked.connect(self.openDBPathDialog)
        self.loadDBButton.clicked.connect(self.loadDB)
        self.loadVocabButton.clicked.connect(self.loadVocab)
        self.outputFileSelectButton.clicked.connect(self.openOutputPathDialog)
        self.addDefinitionButton.clicked.connect(self.addDefinitionClick)
        self.langComboBox.currentIndexChanged.connect(self.dictComboBoxIndexChanged)
        self.saveTSVButton.clicked.connect(self.saveTSV)
        self.timestampDateButton.clicked.connect(self.timestampDateButtonClick)
        self.actionOpen_Vocab_DB .triggered.connect(self.openDBPathDialog)
        self.actionLoad_DB.triggered.connect(self.loadDB)

    def openDBPathDialog(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, filter='Kindle DB (*.db)')
        print(filePath, fileType)
        self.dbPathEdit.setText(filePath)

    def openOutputPathDialog(self):
        file_name = 'out.tsv'
        today_string = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        curIndex = self.bookListWidget.currentIndex().row()
        if curIndex == 0:
            file_name = f'AllBooks-{today_string}_{str(self.max_timestamp)}.tsv'
        elif curIndex > 0:
            file_name = f"{self.books[curIndex - 1]['title']}-{today_string}_{str(self.max_timestamp)}.tsv"
        
        filePath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, 'Save TSV File', file_name, filter='Tab Seperated Vector (*.tsv)')
        print(filePath, fileType)
        self.outputFileEdit.setText(filePath)

    def loadDB(self):
        self.currentVocabDB = VocabDB(self.dbPathEdit.text())
        self.books = self.currentVocabDB.book_infos()
        self.bookListWidget.clear()
        allBookItem = QListWidgetItem()
        allBookItem.setText(self.tr('All Books'))
        allBookItem.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon))
        self.bookListWidget.addItem(allBookItem)
        for book in self.books:
            listItem = QListWidgetItem()
            listItem.setText(book['title'])
            if len(book['asin']) == 10:
                book_icon = load_icon_from_url(f'https://images.amazon.com/images/P/{book["asin"]}.01.20TRZZZZ.jpg')
                if book_icon:
                    listItem.setIcon(book_icon)
                else:
                    listItem.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon))
            else:
                listItem.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon))
            self.bookListWidget.addItem(listItem)
        self.statusBar().showMessage(self.tr('Kindle vocab.db is loaded'), 5000)

    def loadVocab(self):
        curIndex = self.bookListWidget.currentIndex().row()
        if curIndex == 0:
            print("select All Books!")
        else:
            currentBookId = self.books[curIndex - 1]['id']
            currentTimeStamp = int(self.timestampEdit.text())
            self.all_words = self.currentVocabDB.words(currentBookId, currentTimeStamp)
            for word in self.all_words:
                timestamp = word['timestamp']
                if timestamp > self.max_timestamp:
                    self.max_timestamp = timestamp
            self.currentWordTableModel = VocabTableModel(self.all_words) 
            self.vocabTableView.setModel(self.currentWordTableModel)
        self.statusBar().showMessage(self.tr('All vocaburary from {} is loaded.').format(self.books[curIndex - 1]["title"]), 5000)
            
    def loadDictionaries(self):
        self.all_installed_dicts = INSTALLED_DICTS
        self.langComboBox.addItems([key for key in self.all_installed_dicts])
        self.dictionaryListWidget.clear()
        for dkey in self.all_installed_dicts:
            dict_list = self.all_installed_dicts[dkey]
            for dictionary in dict_list:
                dict_item = QListWidgetItem()
                dict_item.setText(dictionary.name)
                dict_item.setIcon(QIcon(dictionary.cover_image))
                self.dictionaryListWidget.addItem(dict_item)
            break

    def dictComboBoxIndexChanged(self):
        self.dictionaryListWidget.clear()
        lang = self.langComboBox.currentText()
        dict_list = self.all_installed_dicts[lang]
        for dictionary in dict_list:
            dict_item = QListWidgetItem()
            dict_item.setText(dictionary.name)
            dict_item.setIcon(QIcon(dictionary.cover_image))
            self.dictionaryListWidget.addItem(dict_item)

    def timestampDateButtonClick(self):
        date_time, ok = DateDialog.getDateTime()
        if ok:
            self.timestampEdit.setText(str(date_time.toMSecsSinceEpoch()))

    def addDefinitionClick(self):
        for i in range(len(self.all_words)):
            word = self.all_words[i]
            if word['lang'] in self.all_installed_dicts:
                lang_dicts = self.all_installed_dicts[word['lang']]
                defi = ""
                for dictionary in lang_dicts:
                    defi = dictionary.query(word['word'])
                    if defi == '':
                        defi = dictionary.query(word['stem'])
                    if defi != '':
                        self.all_words[i]['definition'] = defi 
                        break
        self.currentWordTableModel.set_data(self.all_words) 
        self.currentWordTableModel.dataChanged.emit(self.currentWordTableModel.createIndex(0,0), self.currentWordTableModel.createIndex(self.currentWordTableModel.rowCount(),self.currentWordTableModel.columnCount()))

    def saveTSV(self):
        out_file_path = self.outputFileEdit.text()
        with open(out_file_path, 'w', newline='') as csvfile:
            word_writer = csv.writer(csvfile, delimiter='\t')
            for item in self.all_words:
                nitem = (item['word'], item['usage'], item['definition'].replace('\n', '').replace('\r', '').replace('\x00', '').strip())
                word_writer.writerow(nitem)



if __name__ == '__main__':
    dataPath = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation)
    print(dataPath)
    app = QtWidgets.QApplication(sys.argv)
    window = KindleVocabMateMainWindow()
    window.show()
    sys.exit(app.exec())
