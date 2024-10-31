from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

import sys
import MainWindow
import csv
import json
import os
import os.path
import platform
from pathlib import Path

from db import VocabDB
from utils import load_icon_from_url, DateDialog, VocabTableModel
from dicts import JsonDictionary
from DictionarySettingDialog import DictionarySettingDialog

RELEASE_VERSION = "1.0"

QApplication.setOrganizationDomain('dila.edu.tw')
QApplication.setOrganizationName('DILA')
QApplication.setApplicationName('KindleVocabMate')

class KindleVocabMateMainWindow(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, resources_dir):
        super().__init__()
        self.setupUi(self)

        self.resources_dir = resources_dir
        self.dictSettingDialog = DictionarySettingDialog(self)

        self.setWindowIcon(QIcon(os.path.join(self.resources_dir, 'kindle_vocab_mate.png')))

        # Signals
        self.connectSignals()

        self.currentVocabDB = None
        self.books = []
        self.all_words = None 
        self.currentWordTableModel = None
        self.max_timestamp = 0

        # [TODO] Remove all ditionary settings.
        #settings = QSettings()
        #settings.setValue("installed_dictionaries", "[]")
        
        self.loadDictionaries()

    def connectSignals(self):
        self.dbPathOpenButton.clicked.connect(self.openDBPathDialog)
        self.loadDBButton.clicked.connect(self.loadDB)
        self.loadVocabButton.clicked.connect(self.loadVocab)
        self.addDefinitionButton.clicked.connect(self.addDefinitionClick)
        self.langComboBox.currentIndexChanged.connect(self.dictComboBoxIndexChanged)
        self.exportTSVButton.clicked.connect(self.exportTSV)
        self.timestampDateButton.clicked.connect(self.timestampDateButtonClick)
        self.actionOpen_Vocab_DB .triggered.connect(self.openDBPathDialog)
        self.actionLoad_DB.triggered.connect(self.loadDB)
        self.actionSelect_Timestamp.triggered.connect(self.timestampDateButtonClick)
        self.actionLoad_Vocabulary.triggered.connect(self.loadVocab)
        self.actionAdd_Definitions.triggered.connect(self.addDefinitionClick)
        self.actionExport_TSV_File.triggered.connect(self.exportTSV)
        self.actionManage_Dictionaries.triggered.connect(self.manageDictionaries)
        self.autoDetectKindleButton.clicked.connect(self.autoDetectClicked)
        self.actionAuto_Detect.triggered.connect(self.autoDetectClicked)
        self.actionAbout.triggered.connect(self.about)

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
        if self.dbPathEdit.text().strip() == '':
            mbox = QMessageBox()
            mbox.critical(self, self.tr('No vocab.db Path'), self.tr('Please set the path of vocab.db first.'))
            return
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
        if curIndex < 0:
            mbox = QMessageBox()
            mbox.critical(self, self.tr('DB is Not Loaded.'), self.tr('Please load Kindle vocab.db first.'))
        elif curIndex == 0:
            currentTimeStamp = int(self.timestampEdit.text())
            self.all_words = self.currentVocabDB.all_books_words(currentTimeStamp)
            for word in self.all_words:
                timestamp = word['timestamp']
                if timestamp > self.max_timestamp:
                    self.max_timestamp = timestamp
            self.currentWordTableModel = VocabTableModel(self.all_words) 
            self.vocabTableView.setModel(self.currentWordTableModel)
            self.statusBar().showMessage(self.tr('All vocaburary is loaded.'), 5000)
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
        self.all_installed_dicts = {}
        settings = QSettings()
        dicts_json = settings.value('installed_dictionaries', '[]')
        dict_list = json.loads(dicts_json)
        if len(dict_list) <= 0:
            mbox = QMessageBox()
            mbox.information(self, self.tr('No Dictionaries'), self.tr('You have no dictionary. Please add dictionaries in the Setting.'))
            self.langComboBox.clear()
            self.dictionaryListWidget.clear()
            return
        for dictionary in dict_list:
            dict_prefix_path = os.path.join(os.path.dirname(dictionary['jifo_file']), Path(dictionary['jifo_file']).stem)
            dict_obj = JsonDictionary(dictionary['cover_image'], dict_prefix_path)
            if dictionary['lang'] not in self.all_installed_dicts:
                self.all_installed_dicts[dictionary['lang']] = [ dict_obj ]
            else:
                self.all_installed_dicts[dictionary['lang']].append(dict_obj)
        self.langComboBox.clear()
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
        lang = self.langComboBox.currentText()
        if lang == '':
            return
        self.dictionaryListWidget.clear()
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
        currentLang = self.langComboBox.currentText()
        currentDictIndex = self.dictionaryListWidget.currentRow()
        if not self.all_words:
            mbox = QMessageBox()
            mbox.critical(self, self.tr('No Words'), self.tr('Please load vocaburary first.'))
            return
        if currentDictIndex < 0:
            mbox = QMessageBox()
            mbox.critical(self, self.tr('Error'), self.tr('No selected dictionary.'))
            return
        currentDictionary = self.all_installed_dicts[currentLang][currentDictIndex]
        if not currentDictionary.is_loaded():
            currentDictionary.load()
        for i in range(len(self.all_words)):
            word = self.all_words[i]
            if word['lang'] in self.all_installed_dicts:
                lang_dicts = self.all_installed_dicts[word['lang']]
                defi = self.all_words[i]['definition']
                if defi == '':
                    defi = currentDictionary.query(word['word'])
                    if defi == '':
                        defi = currentDictionary.query(word['stem'])
                    if defi != '':
                        self.all_words[i]['definition'] = defi 
        self.currentWordTableModel.set_data(self.all_words) 
        self.currentWordTableModel.dataChanged.emit(self.currentWordTableModel.createIndex(0,0), self.currentWordTableModel.createIndex(self.currentWordTableModel.rowCount(),self.currentWordTableModel.columnCount()))
        mbox = QMessageBox()
        mbox.information(self, self.tr('Add Definitions'), self.tr('Definitions from the selected dictionary are all added.'))

    def exportTSV(self):
        file_name = 'out.tsv'
        today_string = QDateTime.currentDateTime().toString('yyyy-MM-dd')
        curIndex = self.bookListWidget.currentIndex().row()
        if curIndex < 0:
            mbox = QMessageBox()
            mbox.critical(self, self.tr('No Selected Book'), self.tr('Please select a book first.'))
            return
        elif curIndex == 0:
            file_name = f'AllBooks-{today_string}_{str(self.max_timestamp)}.tsv'
        elif curIndex > 0:
            file_name = f"{self.books[curIndex - 1]['title']}-{today_string}_{str(self.max_timestamp)}.tsv"
        
        filePath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, self.tr('Export TSV File'), file_name, filter='Tab Seperated Vector (*.tsv)')
        if filePath:
            with open(filePath, 'w', newline='') as csvfile:
                word_writer = csv.writer(csvfile, delimiter='\t')
                for item in self.all_words:
                    nitem = (item['word'], item['usage'], item['definition'].replace('\n', '').replace('\r', '').replace('\x00', '').strip())
                    word_writer.writerow(nitem)
            mbox =QMessageBox()
            mbox.information(self, self.tr('Export TSV File'), self.tr('The TSV file is saved successfully.'))

    def manageDictionaries(self):
        res = self.dictSettingDialog.exec()
        self.loadDictionaries()

    def autoDetectClicked(self):
        if platform.system() == 'Darwin':
            if os.path.exists('/Volumes/KINDLE'):
                if os.path.exists('/Volumes/KINDLE/system/vocabulary/vocab.db'):
                    self.dbPathEdit.setText('/Volumes/KINDLE/system/vocabulary/vocab.db')
                else:
                    mbox = QMessageBox()
                    mbox.information(self, self.tr('No vocab.db'), self.tr('vocab.db does not exists in the kindle device.'))
            else:
                mbox = QMessageBox()
                mbox.information(self, self.tr('No kindle'), self.tr('No kindle device is detected'))
        elif platform.system() == 'Windows':
            import wmi
            c = wmi.WMI()
            kindleDrive = None
            for drive in c.Win32_LogicalDisk():
                if drive.DriveType == 2 and drive.VolumeName == 'KINDLE':
                    kindleDrive = drive.Caption
                    break
            if kindleDrive:
                kindle_vocab_db_path = os.path.join(kindleDrive, '/system/vocabulary/vocab.db')
                if os.path.exists(kindle_vocab_db_path):
                    self.dbPathEdit.setText(kindle_vocab_db_path)
                else:
                    mbox = QMessageBox()
                    mbox.information(self, self.tr('no vocab.db'), self.tr('vocab.db does not exists in the kindle device.'))
            else:
                mbox = QMessageBox()
                mbox.information(self, self.tr('no kindle'), self.tr('No kindle device is detected'))

    def about(self):
        mbox = QMessageBox()
        mbox.about(self, self.tr('About Kindle VocabMate'), self.tr('Kindle VocabMate\n\n Version {}').format(RELEASE_VERSION))

if __name__ == '__main__':
    dataPath = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation)

    app = QtWidgets.QApplication(sys.argv)
    appPath = app.applicationDirPath()

    resources_dir = './'

    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
        if platform.system() == 'Darwin':
            resources_dir = os.path.join(bundle_dir, "../Resources/")
        else:
            resources_dir = bundle_dir
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = bundle_dir

    base_translator = QTranslator()
    base_translator.load('qtbase_' + QLocale.system().name() + '.qm', os.path.join(resources_dir, 'translate'))
    translator = QTranslator()
    translator.load(QLocale.system().name() + '.qm', os.path.join(resources_dir, 'translate'))
    app.installTranslator(base_translator)
    app.installTranslator(translator)

    window = KindleVocabMateMainWindow(resources_dir)
    window.show()
    sys.exit(app.exec())
