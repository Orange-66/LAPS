# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_index.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Index(object):
    def setupUi(self, Index):
        Index.setObjectName("Index")
        Index.resize(812, 555)
        self.centralwidget = QtWidgets.QWidget(Index)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_new_single = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new_single.setObjectName("btn_new_single")
        self.horizontalLayout.addWidget(self.btn_new_single)
        self.btn_import = QtWidgets.QPushButton(self.centralwidget)
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout.addWidget(self.btn_import)
        self.btn_painting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_painting.setObjectName("btn_painting")
        self.horizontalLayout.addWidget(self.btn_painting)
        self.zoom_button = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_button.setObjectName("zoom_button")
        self.horizontalLayout.addWidget(self.zoom_button)
        self.retrieval_button = QtWidgets.QPushButton(self.centralwidget)
        self.retrieval_button.setObjectName("retrieval_button")
        self.horizontalLayout.addWidget(self.retrieval_button)
        self.label_button = QtWidgets.QPushButton(self.centralwidget)
        self.label_button.setObjectName("label_button")
        self.horizontalLayout.addWidget(self.label_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.lock_button = QtWidgets.QPushButton(self.centralwidget)
        self.lock_button.setObjectName("lock_button")
        self.horizontalLayout.addWidget(self.lock_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_up_page = QtWidgets.QPushButton(self.frame)
        self.btn_up_page.setObjectName("btn_up_page")
        self.horizontalLayout_2.addWidget(self.btn_up_page)
        self.btn_page_info = QtWidgets.QPushButton(self.frame)
        self.btn_page_info.setObjectName("btn_page_info")
        self.horizontalLayout_2.addWidget(self.btn_page_info)
        self.btn_down_page = QtWidgets.QPushButton(self.frame)
        self.btn_down_page.setObjectName("btn_down_page")
        self.horizontalLayout_2.addWidget(self.btn_down_page)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wid_original_image = QtWidgets.QGraphicsView(self.frame)
        self.wid_original_image.setObjectName("wid_original_image")
        self.horizontalLayout_3.addWidget(self.wid_original_image)
        self.horizontalLayout_3.setStretch(0, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.wid_processed_image = QtWidgets.QGraphicsView(self.frame)
        self.wid_processed_image.setObjectName("wid_processed_image")
        self.horizontalLayout_8.addWidget(self.wid_processed_image)
        self.horizontalLayout_8.setStretch(0, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_4.addWidget(self.graphicsView_3)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_4.addWidget(self.graphicsView_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_5.addWidget(self.listWidget)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        Index.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Index)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        Index.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Index)
        self.statusbar.setObjectName("statusbar")
        Index.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "LAP分析系统"))
        self.btn_new_single.setText(_translate("Index", "新建"))
        self.btn_import.setText(_translate("Index", "导入"))
        self.btn_painting.setText(_translate("Index", "绘图"))
        self.zoom_button.setText(_translate("Index", "缩放"))
        self.retrieval_button.setText(_translate("Index", "检索"))
        self.label_button.setText(_translate("Index", "标记"))
        self.delete_button.setText(_translate("Index", "删除"))
        self.lock_button.setText(_translate("Index", "锁定"))
        self.btn_up_page.setText(_translate("Index", "<"))
        self.btn_page_info.setText(_translate("Index", "第 NAN 张 / 共 NAN 张"))
        self.btn_down_page.setText(_translate("Index", ">"))
        self.menu.setTitle(_translate("Index", "LAPS"))
        self.menu_2.setTitle(_translate("Index", "设置"))
        self.menu_3.setTitle(_translate("Index", "帮助"))
