# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI/ui_new_batch.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Import_Patient_Batch(object):
    def setupUi(self, Import_Patient_Batch):
        Import_Patient_Batch.setObjectName("Import_Patient_Batch")
        Import_Patient_Batch.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Import_Patient_Batch)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Import_Patient_Batch)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(Import_Patient_Batch)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(Import_Patient_Batch)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout.addWidget(self.lineEdit_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(Import_Patient_Batch)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(Import_Patient_Batch)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_2.addWidget(self.lineEdit_10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_2 = QtWidgets.QPushButton(Import_Patient_Batch)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Import_Patient_Batch)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi(Import_Patient_Batch)
        QtCore.QMetaObject.connectSlotsByName(Import_Patient_Batch)

    def retranslateUi(self, Import_Patient_Batch):
        _translate = QtCore.QCoreApplication.translate
        Import_Patient_Batch.setWindowTitle(_translate("Import_Patient_Batch", "批量导入"))
        self.pushButton_3.setText(_translate("Import_Patient_Batch", "模版文件"))
        self.label_9.setText(_translate("Import_Patient_Batch", "患者信息文件"))
        self.label_10.setText(_translate("Import_Patient_Batch", "患者影像文件"))
        self.pushButton_2.setText(_translate("Import_Patient_Batch", "取消"))
        self.pushButton.setText(_translate("Import_Patient_Batch", "新建"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Import_Patient_Batch = QtWidgets.QWidget()
    ui = Ui_Import_Patient_Batch()
    ui.setupUi(Import_Patient_Batch)
    Import_Patient_Batch.show()
    sys.exit(app.exec_())
