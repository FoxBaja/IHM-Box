# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -20, 1280, 800))
        self.background.setText("")
        self.background.setTextFormat(QtCore.Qt.PlainText)
        self.background.setPixmap(QtGui.QPixmap("sketch/background.png"))
        self.background.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.background.setObjectName("background")
        self.lcd_rpm_value = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_value.setGeometry(QtCore.QRect(338, 154, 170, 80))
        self.lcd_rpm_value.setDigitCount(4)
        self.lcd_rpm_value.setProperty("value", 0.0)
        self.lcd_rpm_value.setProperty("intValue", 0)
        self.lcd_rpm_value.setObjectName("lcd_rpm_value")
        self.lcd_rpm_mean = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_mean.setGeometry(QtCore.QRect(663, 154, 170, 80))
        self.lcd_rpm_mean.setDigitCount(4)
        self.lcd_rpm_mean.setProperty("value", 0.0)
        self.lcd_rpm_mean.setProperty("intValue", 0)
        self.lcd_rpm_mean.setObjectName("lcd_rpm_mean")
        self.lcd_rpm_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_max.setGeometry(QtCore.QRect(985, 154, 170, 80))
        self.lcd_rpm_max.setDigitCount(4)
        self.lcd_rpm_max.setProperty("value", 0.0)
        self.lcd_rpm_max.setProperty("intValue", 0)
        self.lcd_rpm_max.setObjectName("lcd_rpm_max")
        self.lcd_speed_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_max.setGeometry(QtCore.QRect(985, 289, 170, 80))
        self.lcd_speed_max.setDigitCount(2)
        self.lcd_speed_max.setProperty("value", 0.0)
        self.lcd_speed_max.setProperty("intValue", 0)
        self.lcd_speed_max.setObjectName("lcd_speed_max")
        self.lcd_speed_value = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_value.setGeometry(QtCore.QRect(338, 289, 170, 80))
        self.lcd_speed_value.setDigitCount(2)
        self.lcd_speed_value.setProperty("value", 0.0)
        self.lcd_speed_value.setProperty("intValue", 0)
        self.lcd_speed_value.setObjectName("lcd_speed_value")
        self.lcd_speed_mean = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_mean.setGeometry(QtCore.QRect(663, 289, 170, 80))
        self.lcd_speed_mean.setDigitCount(2)
        self.lcd_speed_mean.setProperty("value", 0.0)
        self.lcd_speed_mean.setProperty("intValue", 0)
        self.lcd_speed_mean.setObjectName("lcd_speed_mean")
        self.lcd_distance = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_distance.setGeometry(QtCore.QRect(338, 424, 170, 80))
        self.lcd_distance.setSmallDecimalPoint(True)
        self.lcd_distance.setDigitCount(4)
        self.lcd_distance.setProperty("value", 0.0)
        self.lcd_distance.setProperty("intValue", 0)
        self.lcd_distance.setObjectName("lcd_distance")
        self.progress_battery = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_battery.setGeometry(QtCore.QRect(338, 549, 493, 80))
        self.progress_battery.setProperty("value", 0)
        self.progress_battery.setInvertedAppearance(False)
        self.progress_battery.setObjectName("progress_battery")
        self.progress_gasoline = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_gasoline.setGeometry(QtCore.QRect(338, 683, 494, 80))
        self.progress_gasoline.setProperty("value", 100)
        self.progress_gasoline.setObjectName("progress_gasoline")
        self.console = QtWidgets.QListWidget(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(853, 424, 410, 339))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "selection-background-color: rgb(0, 0, 0);\n"
                                    "selection-color: rgb(0, 0, 0);\n"
                                    "font: 8pt \"Consolas\";\n"
                                    "color: rgb(255, 0, 0);")
        self.console.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console.setLineWidth(0)
        self.console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console.setAutoScrollMargin(50)
        self.console.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.console.setProperty("showDropIndicator", False)
        self.console.setAlternatingRowColors(False)
        self.console.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.console.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.console.setTextElideMode(QtCore.Qt.ElideNone)
        self.console.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.console.setFlow(QtWidgets.QListView.TopToBottom)
        self.console.setProperty("isWrapping", False)
        self.console.setResizeMode(QtWidgets.QListView.Adjust)
        self.console.setLayoutMode(QtWidgets.QListView.Batched)
        self.console.setViewMode(QtWidgets.QListView.ListMode)
        self.console.setModelColumn(0)
        self.console.setUniformItemSizes(True)
        self.console.setObjectName("console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBar.sizePolicy().hasHeightForWidth())
        self.menuBar.setSizePolicy(sizePolicy)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuConnect = QtWidgets.QMenu(self.menuFile)
        self.menuConnect.setObjectName("menuConnect")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setEnabled(False)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.menuConnect.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fox Baja IHM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save as"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New report"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))