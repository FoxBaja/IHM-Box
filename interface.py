from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets
from MainWindow import Ui_MainWindow

import serial.tools.list_ports
from datetime import datetime
import csv

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Variáveis do programa
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

        # Funções que são chamadas na inicialização
        self.showSerialDevices()
        self.show()

        # Adiciona uma ação ao botão Start e Save do Menu
        self.actionNew.triggered.connect(self.startReport)
        self.actionSave.triggered.connect(self.saveReport)

    #Esta função é chamada na incialização, ela lista no menu os dispositivos serial
    def showSerialDevices(self):
        for element in serial.tools.list_ports.comports():
            device_button = QAction('{}'.format(element.device), self)
            # Adiciona-se uma ação na opção do dispositivo
            device_button.triggered.connect(lambda checked, device=element.device: self.defineDevice(device))
            self.menuConnect.addAction(device_button)

    # Essa função recebe a string com o nome do dispositivo
    def defineDevice(self, device):
        self.deviceName = device
        self.menuConnect.setEnabled(False)
        self.actionNew.setEnabled(True)
        self.consolePrint("Device on port {} selected".format(device))

    # Funciona como um print, escrevendo a string no Console da Interface
    def consolePrint(self, text):
        item = QtWidgets.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.console.addItem(item)

    # Limpa o console da interface gráfica
    def cleanConsole(self):
        self.console.clear()

    # Função que controla as flags de estado do programa
    def saveReport(self):
        self.recordReport = False
        self.actionSave.setEnabled(False)
        self.actionNew.setEnabled(False)
        self.deviceName = None
        self.menuConnect.setEnabled(True)

    # Função que atualiza os dados da interface gráfica, é chamada no loop
    def displayData(self, data):
        speed, battery, rpm, gasoline, timestamp = data

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

        self.calculateDistance(data)

        self.lcd_rpm_value.setProperty("value", rpm)
        self.lcd_speed_value.setProperty("value", speed)
        self.lcd_rpm_mean.setProperty("value", rpm_mean)
        self.lcd_speed_mean.setProperty("value", speed_mean)
        self.progress_battery.setProperty("value", battery)
        self.progress_gasoline.setProperty("value", gasoline)
        self.lcd_distance.setProperty("value", self.distanceAcc)

        self.lastData = data

    
    def startReport(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0] == '':
            pass
        else:
            self.recordReport = True
            self.actionNew.setEnabled(False)
            self.actionSave.setEnabled(True)
            self.lastData = [0, 0, 0, 0, datetime.now()]
            with open(filename[0]+'.csv', mode='w') as csvfile:
                vehicle_data = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                vehicle_data.writerow(['Speed', 'Battery', 'RPM', 'Gasoline', 'Distance', 'Date(DD/MM/YY - HH:MM:SS'])
                try:
                    inBuffer = serial.Serial(self.deviceName, self.devicePort)
                    while self.recordReport:
                        QtCore.QCoreApplication.processEvents()
                        if inBuffer.in_waiting != 0:
                            data = inBuffer.readline().decode('utf-8').strip('\r\n').split(';')
                            if len(data) != 4:
                                pass
                            formated_data = [int(float(i)) for i in data[:4]]
                            formated_data.append(datetime.now())
                            self.displayData(formated_data)
                            
                            date = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
                            vehicle_data.writerow([formated_data[0], formated_data[1], formated_data[2], formated_data[3], round(self.distanceAcc,3), date])
                except NameError:
                    self.consolePrint(NameError)

    def calculateDistance(self, newData):
        deltaTime = (newData[4] - self.lastData[4]).seconds/3600
        deltaSpeed = (newData[0] + self.lastData[0])/2
        distance = deltaSpeed * deltaTime
        self.distanceAcc += distance

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("IHM - Fox Baja")
    window = MainWindow()
    app.exec_()