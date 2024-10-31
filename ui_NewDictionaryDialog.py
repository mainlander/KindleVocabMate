# Form implementation generated from reading ui file 'ui_NewDictionaryDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NewDictionaryDialog(object):
    def setupUi(self, NewDictionaryDialog):
        NewDictionaryDialog.setObjectName("NewDictionaryDialog")
        NewDictionaryDialog.resize(600, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewDictionaryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=NewDictionaryDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jifoFileLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.jifoFileLineEdit.setObjectName("jifoFileLineEdit")
        self.horizontalLayout.addWidget(self.jifoFileLineEdit)
        self.openJifoFileButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.openJifoFileButton.setObjectName("openJifoFileButton")
        self.horizontalLayout.addWidget(self.openJifoFileButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.coverImageLineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.coverImageLineEdit.setObjectName("coverImageLineEdit")
        self.horizontalLayout_2.addWidget(self.coverImageLineEdit)
        self.openImageFileButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.openImageFileButton.setObjectName("openImageFileButton")
        self.horizontalLayout_2.addWidget(self.openImageFileButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=NewDictionaryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewDictionaryDialog)
        self.buttonBox.accepted.connect(NewDictionaryDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(NewDictionaryDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewDictionaryDialog)

    def retranslateUi(self, NewDictionaryDialog):
        _translate = QtCore.QCoreApplication.translate
        NewDictionaryDialog.setWindowTitle(_translate("NewDictionaryDialog", "Add New Dictionary"))
        self.groupBox.setTitle(_translate("NewDictionaryDialog", "New Dictionary"))
        self.label_3.setText(_translate("NewDictionaryDialog", ".jifo File:"))
        self.openJifoFileButton.setText(_translate("NewDictionaryDialog", "Open..."))
        self.label_4.setText(_translate("NewDictionaryDialog", "Cover Image:"))
        self.openImageFileButton.setText(_translate("NewDictionaryDialog", "Open..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDictionaryDialog = QtWidgets.QDialog()
    ui = Ui_NewDictionaryDialog()
    ui.setupUi(NewDictionaryDialog)
    NewDictionaryDialog.show()
    sys.exit(app.exec())
