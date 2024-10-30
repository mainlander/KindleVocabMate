# Form implementation generated from reading ui file 'ui_DictionarySettingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DictionarySettingDialog(object):
    def setupUi(self, DictionarySettingDialog):
        DictionarySettingDialog.setObjectName("DictionarySettingDialog")
        DictionarySettingDialog.resize(498, 396)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DictionarySettingDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=DictionarySettingDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dictListWidget = QtWidgets.QListWidget(parent=self.groupBox)
        self.dictListWidget.setIconSize(QtCore.QSize(51, 78))
        self.dictListWidget.setObjectName("dictListWidget")
        self.verticalLayout.addWidget(self.dictListWidget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addButton = QtWidgets.QPushButton(parent=DictionarySettingDialog)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.editButton = QtWidgets.QPushButton(parent=DictionarySettingDialog)
        self.editButton.setObjectName("editButton")
        self.verticalLayout_2.addWidget(self.editButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.deleteButton = QtWidgets.QPushButton(parent=DictionarySettingDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout_2.addWidget(self.deleteButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=DictionarySettingDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(DictionarySettingDialog)
        self.buttonBox.accepted.connect(DictionarySettingDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(DictionarySettingDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DictionarySettingDialog)

    def retranslateUi(self, DictionarySettingDialog):
        _translate = QtCore.QCoreApplication.translate
        DictionarySettingDialog.setWindowTitle(_translate("DictionarySettingDialog", "Installed Dictionaries"))
        self.groupBox.setTitle(_translate("DictionarySettingDialog", "Dictionaries:"))
        self.addButton.setText(_translate("DictionarySettingDialog", "Add"))
        self.editButton.setText(_translate("DictionarySettingDialog", "Edit"))
        self.deleteButton.setText(_translate("DictionarySettingDialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DictionarySettingDialog = QtWidgets.QDialog()
    ui = Ui_DictionarySettingDialog()
    ui.setupUi(DictionarySettingDialog)
    DictionarySettingDialog.show()
    sys.exit(app.exec())
