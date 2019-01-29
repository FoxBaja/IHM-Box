# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
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
        self.background.setPixmap(QtGui.QPixmap("background.png"))
        self.background.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.background.setObjectName("background")
        self.lcd_rpm_value = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_value.setGeometry(QtCore.QRect(338, 154, 170, 80))
        self.lcd_rpm_value.setDigitCount(4)
        self.lcd_rpm_value.setProperty("value", 2453.0)
        self.lcd_rpm_value.setObjectName("lcd_rpm_value")
        self.lcd_rpm_mean = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_mean.setGeometry(QtCore.QRect(663, 154, 170, 80))
        self.lcd_rpm_mean.setDigitCount(4)
        self.lcd_rpm_mean.setProperty("value", 3476.0)
        self.lcd_rpm_mean.setObjectName("lcd_rpm_mean")
        self.lcd_rpm_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_rpm_max.setGeometry(QtCore.QRect(985, 154, 170, 80))
        self.lcd_rpm_max.setDigitCount(4)
        self.lcd_rpm_max.setProperty("value", 4797.0)
        self.lcd_rpm_max.setObjectName("lcd_rpm_max")
        self.lcd_speed_max = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_max.setGeometry(QtCore.QRect(985, 289, 170, 80))
        self.lcd_speed_max.setDigitCount(2)
        self.lcd_speed_max.setProperty("value", 41.0)
        self.lcd_speed_max.setObjectName("lcd_speed_max")
        self.lcd_speed_value = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_value.setGeometry(QtCore.QRect(338, 289, 170, 80))
        self.lcd_speed_value.setDigitCount(2)
        self.lcd_speed_value.setProperty("value", 34.0)
        self.lcd_speed_value.setObjectName("lcd_speed_value")
        self.lcd_speed_mean = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_speed_mean.setGeometry(QtCore.QRect(663, 289, 170, 80))
        self.lcd_speed_mean.setDigitCount(2)
        self.lcd_speed_mean.setProperty("value", 23.0)
        self.lcd_speed_mean.setObjectName("lcd_speed_mean")
        self.lcd_distance = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_distance.setGeometry(QtCore.QRect(338, 424, 170, 80))
        self.lcd_distance.setSmallDecimalPoint(True)
        self.lcd_distance.setDigitCount(4)
        self.lcd_distance.setProperty("value", 10.4)
        self.lcd_distance.setObjectName("lcd_distance")
        self.progress_battery = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_battery.setGeometry(QtCore.QRect(338, 549, 493, 80))
        self.progress_battery.setProperty("value", 57)
        self.progress_battery.setInvertedAppearance(False)
        self.progress_battery.setObjectName("progress_battery")
        self.progress_gasoline = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_gasoline.setGeometry(QtCore.QRect(338, 683, 494, 80))
        self.progress_gasoline.setProperty("value", 78)
        self.progress_gasoline.setObjectName("progress_gasoline")
        self.console_display = QtWidgets.QListWidget(self.centralwidget)
        self.console_display.setGeometry(QtCore.QRect(853, 424, 410, 339))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_display.sizePolicy().hasHeightForWidth())
        self.console_display.setSizePolicy(sizePolicy)
        self.console_display.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font: 8pt \"Consolas\";\n"
"color: rgb(255, 0, 0);")
        self.console_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console_display.setLineWidth(0)
        self.console_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console_display.setAutoScrollMargin(50)
        self.console_display.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.console_display.setProperty("showDropIndicator", False)
        self.console_display.setAlternatingRowColors(False)
        self.console_display.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.console_display.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.console_display.setTextElideMode(QtCore.Qt.ElideNone)
        self.console_display.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.console_display.setFlow(QtWidgets.QListView.TopToBottom)
        self.console_display.setProperty("isWrapping", False)
        self.console_display.setResizeMode(QtWidgets.QListView.Adjust)
        self.console_display.setLayoutMode(QtWidgets.QListView.Batched)
        self.console_display.setViewMode(QtWidgets.QListView.ListMode)
        self.console_display.setModelColumn(0)
        self.console_display.setUniformItemSizes(True)
        self.console_display.setObjectName("console_display")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionAbout_the_program = QtWidgets.QAction(MainWindow)
        self.actionAbout_the_program.setObjectName("actionAbout_the_program")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setVisible(True)
        self.actionConnect.setIconVisibleInMenu(True)
        self.actionConnect.setObjectName("actionConnect")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuHelp.addAction(self.actionAbout_the_program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fox Baja IHM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionAbout_the_program.setText(_translate("MainWindow", "About the program"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))

