# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_new_single.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New_Single(object):
    def setupUi(self, New_Single):
        New_Single.setObjectName("New_Single")
        New_Single.resize(598, 737)
        self.verticalLayout = QtWidgets.QVBoxLayout(New_Single)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(New_Single)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_create_date = QtWidgets.QLineEdit(New_Single)
        self.line_create_date.setReadOnly(True)
        self.line_create_date.setObjectName("line_create_date")
        self.horizontalLayout.addWidget(self.line_create_date)
        self.horizontalLayout_12.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_cancel = QtWidgets.QPushButton(New_Single)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_11.addWidget(self.btn_cancel)
        self.btn_done = QtWidgets.QPushButton(New_Single)
        self.btn_done.setObjectName("btn_done")
        self.horizontalLayout_11.addWidget(self.btn_done)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.line_2 = QtWidgets.QFrame(New_Single)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(New_Single)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.line_name = QtWidgets.QLineEdit(New_Single)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout_3.addWidget(self.line_name)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(New_Single)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.spin_dbp = QtWidgets.QSpinBox(New_Single)
        self.spin_dbp.setMaximum(300)
        self.spin_dbp.setObjectName("spin_dbp")
        self.horizontalLayout_10.addWidget(self.spin_dbp)
        self.gridLayout.addLayout(self.horizontalLayout_10, 5, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(New_Single)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.label_degree = QtWidgets.QLabel(New_Single)
        self.label_degree.setText("")
        self.label_degree.setObjectName("label_degree")
        self.horizontalLayout_8.addWidget(self.label_degree)
        self.spin_bmi = QtWidgets.QDoubleSpinBox(New_Single)
        self.spin_bmi.setReadOnly(True)
        self.spin_bmi.setDecimals(1)
        self.spin_bmi.setObjectName("spin_bmi")
        self.horizontalLayout_8.addWidget(self.spin_bmi)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(New_Single)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spin_weight = QtWidgets.QDoubleSpinBox(New_Single)
        self.spin_weight.setProperty("showGroupSeparator", False)
        self.spin_weight.setDecimals(1)
        self.spin_weight.setMaximum(250.0)
        self.spin_weight.setObjectName("spin_weight")
        self.horizontalLayout_6.addWidget(self.spin_weight)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(New_Single)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_id = QtWidgets.QLineEdit(New_Single)
        self.line_id.setObjectName("line_id")
        self.horizontalLayout_2.addWidget(self.line_id)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(New_Single)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.spin_stature = QtWidgets.QSpinBox(New_Single)
        self.spin_stature.setPrefix("")
        self.spin_stature.setMaximum(300)
        self.spin_stature.setObjectName("spin_stature")
        self.horizontalLayout_4.addWidget(self.spin_stature)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(New_Single)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.spin_bsa = QtWidgets.QDoubleSpinBox(New_Single)
        self.spin_bsa.setReadOnly(True)
        self.spin_bsa.setDecimals(4)
        self.spin_bsa.setObjectName("spin_bsa")
        self.horizontalLayout_7.addWidget(self.spin_bsa)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(New_Single)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.spin_age = QtWidgets.QSpinBox(New_Single)
        self.spin_age.setMaximum(150)
        self.spin_age.setObjectName("spin_age")
        self.horizontalLayout_5.addWidget(self.spin_age)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(New_Single)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.combo_gender = QtWidgets.QComboBox(New_Single)
        self.combo_gender.setObjectName("combo_gender")
        self.combo_gender.addItem("")
        self.combo_gender.addItem("")
        self.horizontalLayout_13.addWidget(self.combo_gender)
        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(New_Single)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.spin_sbp = QtWidgets.QSpinBox(New_Single)
        self.spin_sbp.setMaximum(300)
        self.spin_sbp.setObjectName("spin_sbp")
        self.horizontalLayout_9.addWidget(self.spin_sbp)
        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(New_Single)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(New_Single)
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
        self.label.setBuddy(self.line_create_date)
        self.label_3.setBuddy(self.line_name)
        self.label_10.setBuddy(self.spin_dbp)
        self.label_6.setBuddy(self.spin_bmi)
        self.label_5.setBuddy(self.spin_weight)
        self.label_2.setBuddy(self.line_id)
        self.label_8.setBuddy(self.spin_stature)
        self.label_7.setBuddy(self.spin_bsa)
        self.label_4.setBuddy(self.spin_age)
        self.label_11.setBuddy(self.combo_gender)
        self.label_9.setBuddy(self.spin_sbp)

        self.retranslateUi(New_Single)
        self.combo_gender.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(New_Single)
        New_Single.setTabOrder(self.line_create_date, self.graphicsView_2)
        New_Single.setTabOrder(self.graphicsView_2, self.graphicsView_4)
        New_Single.setTabOrder(self.graphicsView_4, self.graphicsView_5)
        New_Single.setTabOrder(self.graphicsView_5, self.graphicsView_6)
        New_Single.setTabOrder(self.graphicsView_6, self.graphicsView)
        New_Single.setTabOrder(self.graphicsView, self.graphicsView_8)
        New_Single.setTabOrder(self.graphicsView_8, self.graphicsView_9)
        New_Single.setTabOrder(self.graphicsView_9, self.graphicsView_10)
        New_Single.setTabOrder(self.graphicsView_10, self.graphicsView_7)
        New_Single.setTabOrder(self.graphicsView_7, self.graphicsView_3)
        New_Single.setTabOrder(self.graphicsView_3, self.btn_cancel)
        New_Single.setTabOrder(self.btn_cancel, self.btn_done)
        New_Single.setTabOrder(self.btn_done, self.line_name)
        New_Single.setTabOrder(self.line_name, self.spin_dbp)
        New_Single.setTabOrder(self.spin_dbp, self.spin_bmi)
        New_Single.setTabOrder(self.spin_bmi, self.spin_weight)
        New_Single.setTabOrder(self.spin_weight, self.line_id)
        New_Single.setTabOrder(self.line_id, self.spin_stature)
        New_Single.setTabOrder(self.spin_stature, self.spin_bsa)
        New_Single.setTabOrder(self.spin_bsa, self.spin_age)
        New_Single.setTabOrder(self.spin_age, self.combo_gender)
        New_Single.setTabOrder(self.combo_gender, self.spin_sbp)

    def retranslateUi(self, New_Single):
        _translate = QtCore.QCoreApplication.translate
        New_Single.setWindowTitle(_translate("New_Single", "新建患者信息"))
        self.label.setText(_translate("New_Single", "日期"))
        self.btn_cancel.setText(_translate("New_Single", "取消"))
        self.btn_done.setText(_translate("New_Single", "完成"))
        self.label_3.setText(_translate("New_Single", "姓名"))
        self.label_10.setText(_translate("New_Single", "舒张压DBP"))
        self.spin_dbp.setSuffix(_translate("New_Single", "mmHg"))
        self.label_6.setText(_translate("New_Single", "肥胖程度BMI"))
        self.label_5.setText(_translate("New_Single", "体重"))
        self.spin_weight.setSuffix(_translate("New_Single", "kg"))
        self.label_2.setText(_translate("New_Single", "编号"))
        self.label_8.setText(_translate("New_Single", "身高"))
        self.spin_stature.setSuffix(_translate("New_Single", "cm"))
        self.label_7.setText(_translate("New_Single", "体表面积BSA"))
        self.spin_bsa.setSuffix(_translate("New_Single", "m²"))
        self.label_4.setText(_translate("New_Single", "年龄"))
        self.spin_age.setSuffix(_translate("New_Single", "岁"))
        self.label_11.setText(_translate("New_Single", "性别"))
        self.combo_gender.setItemText(0, _translate("New_Single", "男"))
        self.combo_gender.setItemText(1, _translate("New_Single", "女"))
        self.label_9.setText(_translate("New_Single", "收缩压SBP"))
        self.spin_sbp.setSuffix(_translate("New_Single", "mmHg"))
