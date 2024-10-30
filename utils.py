import urllib.request
import os, os.path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

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
        titles = [self.tr('Word'), self.tr('Usage'), self.tr('Language'), self.tr('Definition')]
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return titles[section]
            elif orientation == Qt.Orientation.Vertical:
                return f'{section + 1}'
        return super().headerData(section, orientation, role)

def load_icon_from_url(url):
    dataPath = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation)
    coverImagePath = os.path.join(dataPath, 'cover_images')
    if not os.path.isdir(coverImagePath):
        try:
            os.makedirs(coverImagePath)
        except FileExistsError:
            print("File already exists.")
        except PermissionError:
            print("No Premission.")
    pixmap = QPixmap()
    filename = os.path.basename(url)
    #file = QFile(os.path.join("." , "/cover_images/" + filename))
    #if file.open(QIODeviceBase.OpenModeFlag.ReadOnly):
    #    pixmap.loadFromData(file.readAll())
    #    file.close()
    local_filepath = os.path.join(coverImagePath, filename)
    if os.path.exists(local_filepath):
        with open(local_filepath, 'rb') as f:
            imgdata = f.read()
            pixmap.loadFromData(imgdata)
    else:
        try:
            response = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': USER_AGENT}))
            imgdata = response.read()
            img_file_path = os.path.join(coverImagePath, filename)
            with open(img_file_path, 'wb') as outf:
                outf.write(imgdata)
            pixmap.loadFromData(imgdata)
        except:
            print("Image URL request error.")
            return None
    return QIcon(pixmap)


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("Select Timestamp"))

        layout = QVBoxLayout(self)

        # nice widget for editing the date
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            Qt.Orientation.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def dateTime(self):
        return self.datetime.dateTime()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTime()
        return (date, result == QDialog.DialogCode.Accepted)
