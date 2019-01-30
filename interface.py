from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets
from MainWindow import Ui_MainWindow

import serial.tools.list_ports
from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.deviceName = None
        self.devicePort = 9600
        self.recordReport = True
        self.speedMax = 0
        self.speedAcc = 0
        self.rpmMax = 0
        self.rpmAcc = 0
        self.distanceAcc = 0
        self.dataCounter = 0
        self.lastData = None
        self.showSerialDevices()
        self.show()
        self.actionNew.triggered.connect(self.startReport)
        self.actionSave.triggered.connect(self.saveReport)

    def showSerialDevices(self):
        for element in serial.tools.list_ports.comports():
            device_button = QAction('{}'.format(element.device), self)
            device_button.triggered.connect(lambda checked, device=element.device: self.defineDevice(device))
            self.menuConnect.addAction(device_button)

    def defineDevice(self, device):
        self.deviceName = device
        self.menuConnect.setEnabled(False)
        self.actionNew.setEnabled(True)
        self.consolePrint("Device on port {} selected".format(device))

    def consolePrint(self, text):
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.console.addItem(item)

    def cleanConsole(self):
        self.console.clear()
    
    def saveReport(self):
        self.recordReport = False
        self.actionSave.setEnabled(False)
        self.actionNew.setEnabled(False)
        self.deviceName = None
        self.menuConnect.setEnabled(True)

    def displayData(self, data):
        rpm, speed, battery, gas_1, gas_2, timestamp = data

        self.rpmAcc += rpm
        self.dataCounter += 1
        self.speedAcc += speed
        rpm_mean = self.rpmAcc/self.dataCounter
        speed_mean = self.speedAcc/self.dataCounter

        if speed > self.speedMax:
            self.lcd_speed_max.setProperty("value", speed)
            self.speedMax = speed

        if rpm > self.rpmMax:
            self.lcd_rpm_max.setProperty("value", rpm)
            self.rpmMax = rpm

        if not gas_2:
            self.progress_gasoline.setProperty("value", 66)
        if not gas_1:
            self.progress_gasoline.setProperty("value", 33)

        distance = self.calculateDistance(data)

        self.lcd_rpm_value.setProperty("value", rpm)
        self.lcd_speed_value.setProperty("value", speed)
        self.lcd_rpm_mean.setProperty("value", rpm_mean)
        self.lcd_speed_mean.setProperty("value", speed_mean)
        self.progress_battery.setProperty("value", battery)
        self.lcd_distance.setProperty("value", self.distanceAcc)

        self.lastData = data

    def startReport(self):
        self.recordReport = True
        self.actionNew.setEnabled(False)
        self.actionSave.setEnabled(True)
        self.lastData = [0, 0, 0, 0, 0, datetime.now()]
        try:
            inBuffer = serial.Serial(self.deviceName, self.devicePort)
            while self.recordReport:
                QtCore.QCoreApplication.processEvents()
                if inBuffer.in_waiting != 0:
                    data = inBuffer.readline().decode('utf-8').strip('\r\n').split(';')
                    formated_data = [int(float(i)) for i in data[1:]]
                    formated_data.append(datetime.now())
                    self.displayData(formated_data)
        except ValueError as error:
            print(error)
        
    def calculateDistance(self, newData):
        deltaTime = (newData[5] - self.lastData[5]).seconds/3600
        deltaSpeed = (newData[1] + self.lastData[1])/2
        distance = deltaSpeed * deltaTime
        self.distanceAcc += distance
        return distance

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("IHM - Fox Baja")
    window = MainWindow()
    app.exec_()