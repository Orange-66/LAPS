# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_new_patient_single.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Import_Patient_Single(object):
    def setupUi(self, Import_Patient_Single):
        Import_Patient_Single.setObjectName("Import_Patient_Single")
        Import_Patient_Single.resize(598, 706)
        self.verticalLayout = QtWidgets.QVBoxLayout(Import_Patient_Single)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Import_Patient_Single)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_12.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_2 = QtWidgets.QPushButton(Import_Patient_Single)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Import_Patient_Single)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.line_2 = QtWidgets.QFrame(Import_Patient_Single)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(Import_Patient_Single)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_10.addWidget(self.lineEdit_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Import_Patient_Single)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(Import_Patient_Single)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_9.addWidget(self.lineEdit_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_3 = QtWidgets.QFrame(Import_Patient_Single)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(Import_Patient_Single)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_3.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_3.addWidget(self.graphicsView_3, 0, 2, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_4.setSizePolicy(sizePolicy)
        self.graphicsView_4.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout_3.addWidget(self.graphicsView_4, 0, 3, 1, 1)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_5.sizePolicy().hasHeightForWidth())
        self.graphicsView_5.setSizePolicy(sizePolicy)
        self.graphicsView_5.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.gridLayout_3.addWidget(self.graphicsView_5, 0, 4, 1, 1)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_6.sizePolicy().hasHeightForWidth())
        self.graphicsView_6.setSizePolicy(sizePolicy)
        self.graphicsView_6.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout_3.addWidget(self.graphicsView_6, 1, 0, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_8.sizePolicy().hasHeightForWidth())
        self.graphicsView_8.setSizePolicy(sizePolicy)
        self.graphicsView_8.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout_3.addWidget(self.graphicsView_8, 1, 1, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_9.sizePolicy().hasHeightForWidth())
        self.graphicsView_9.setSizePolicy(sizePolicy)
        self.graphicsView_9.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout_3.addWidget(self.graphicsView_9, 1, 2, 1, 1)
        self.graphicsView_10 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_10.sizePolicy().hasHeightForWidth())
        self.graphicsView_10.setSizePolicy(sizePolicy)
        self.graphicsView_10.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.gridLayout_3.addWidget(self.graphicsView_10, 1, 3, 1, 1)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_7.sizePolicy().hasHeightForWidth())
        self.graphicsView_7.setSizePolicy(sizePolicy)
        self.graphicsView_7.setMaximumSize(QtCore.QSize(1000, 1000))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout_3.addWidget(self.graphicsView_7, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Import_Patient_Single)
        QtCore.QMetaObject.connectSlotsByName(Import_Patient_Single)

    def retranslateUi(self, Import_Patient_Single):
        _translate = QtCore.QCoreApplication.translate
        Import_Patient_Single.setWindowTitle(_translate("Import_Patient_Single", "新建患者信息"))
        self.label.setText(_translate("Import_Patient_Single", "日期"))
        self.pushButton_2.setText(_translate("Import_Patient_Single", "取消"))
        self.pushButton.setText(_translate("Import_Patient_Single", "新建"))
        self.label_2.setText(_translate("Import_Patient_Single", "编号"))
        self.label_3.setText(_translate("Import_Patient_Single", "姓名"))
        self.label_4.setText(_translate("Import_Patient_Single", "性别"))
        self.label_8.setText(_translate("Import_Patient_Single", "身高"))
        self.label_5.setText(_translate("Import_Patient_Single", "体重"))
        self.label_7.setText(_translate("Import_Patient_Single", "体表面积BSA"))
        self.label_6.setText(_translate("Import_Patient_Single", "肥胖程度BMI"))
        self.label_10.setText(_translate("Import_Patient_Single", "舒张压DBP"))
        self.label_9.setText(_translate("Import_Patient_Single", "收缩压SBP"))
