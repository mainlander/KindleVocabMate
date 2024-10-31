# Form implementation generated from reading ui file 'ui_EditDictionaryDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditDictionaryDialog(object):
    def setupUi(self, EditDictionaryDialog):
        EditDictionaryDialog.setObjectName("EditDictionaryDialog")
        EditDictionaryDialog.resize(600, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditDictionaryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=EditDictionaryDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.dictionaryNameLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.dictionaryNameLineEdit.setReadOnly(True)
        self.dictionaryNameLineEdit.setObjectName("dictionaryNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dictionaryNameLineEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.dictionaryLangComboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.dictionaryLangComboBox.setEnabled(False)
        self.dictionaryLangComboBox.setEditable(False)
        self.dictionaryLangComboBox.setObjectName("dictionaryLangComboBox")
        self.dictionaryLangComboBox.addItem("")
        self.dictionaryLangComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dictionaryLangComboBox)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jifoFileLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.jifoFileLineEdit.setObjectName("jifoFileLineEdit")
        self.horizontalLayout.addWidget(self.jifoFileLineEdit)
        self.openJifoFileButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.openJifoFileButton.setObjectName("openJifoFileButton")
        self.horizontalLayout.addWidget(self.openJifoFileButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.imageLineEdit.setObjectName("imageLineEdit")
        self.horizontalLayout_2.addWidget(self.imageLineEdit)
        self.openImageButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.openImageButton.setObjectName("openImageButton")
        self.horizontalLayout_2.addWidget(self.openImageButton)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=EditDictionaryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditDictionaryDialog)
        self.buttonBox.accepted.connect(EditDictionaryDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(EditDictionaryDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EditDictionaryDialog)

    def retranslateUi(self, EditDictionaryDialog):
        _translate = QtCore.QCoreApplication.translate
        EditDictionaryDialog.setWindowTitle(_translate("EditDictionaryDialog", "Edit Dictionary"))
        self.groupBox.setTitle(_translate("EditDictionaryDialog", "Dictionary"))
        self.label.setText(_translate("EditDictionaryDialog", "Name:"))
        self.label_2.setText(_translate("EditDictionaryDialog", "Language:"))
        self.dictionaryLangComboBox.setItemText(0, _translate("EditDictionaryDialog", "en"))
        self.dictionaryLangComboBox.setItemText(1, _translate("EditDictionaryDialog", "ja"))
        self.label_3.setText(_translate("EditDictionaryDialog", ".jifo File:"))
        self.openJifoFileButton.setText(_translate("EditDictionaryDialog", "Open..."))
        self.label_4.setText(_translate("EditDictionaryDialog", "Cover Image:"))
        self.openImageButton.setText(_translate("EditDictionaryDialog", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditDictionaryDialog = QtWidgets.QDialog()
    ui = Ui_EditDictionaryDialog()
    ui.setupUi(EditDictionaryDialog)
    EditDictionaryDialog.show()
    sys.exit(app.exec())
