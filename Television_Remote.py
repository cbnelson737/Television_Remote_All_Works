# Form implementation generated from reading ui file 'Television_Remote.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 650)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.channel_select_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_7.setGeometry(QtCore.QRect(170, 500, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_7.setFont(font)
        self.channel_select_7.setCheckable(True)
        self.channel_select_7.setObjectName("channel_select_7")
        self.channel_select_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_9.setGeometry(QtCore.QRect(310, 500, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_9.setFont(font)
        self.channel_select_9.setCheckable(True)
        self.channel_select_9.setObjectName("channel_select_9")
        self.channel_select_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_8.setGeometry(QtCore.QRect(240, 500, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_8.setFont(font)
        self.channel_select_8.setCheckable(True)
        self.channel_select_8.setObjectName("channel_select_8")
        self.channel_select_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_6.setGeometry(QtCore.QRect(310, 430, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_6.setFont(font)
        self.channel_select_6.setCheckable(True)
        self.channel_select_6.setObjectName("channel_select_6")
        self.channel_select_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_5.setGeometry(QtCore.QRect(240, 430, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_5.setFont(font)
        self.channel_select_5.setCheckable(True)
        self.channel_select_5.setObjectName("channel_select_5")
        self.channel_select_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_4.setGeometry(QtCore.QRect(170, 430, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_4.setFont(font)
        self.channel_select_4.setCheckable(True)
        self.channel_select_4.setObjectName("channel_select_4")
        self.channel_select_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_3.setGeometry(QtCore.QRect(310, 360, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_3.setFont(font)
        self.channel_select_3.setCheckable(True)
        self.channel_select_3.setObjectName("channel_select_3")
        self.channel_select_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_2.setGeometry(QtCore.QRect(240, 360, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_2.setFont(font)
        self.channel_select_2.setCheckable(True)
        self.channel_select_2.setObjectName("channel_select_2")
        self.channel_select_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_select_1.setGeometry(QtCore.QRect(170, 360, 75, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_select_1.setFont(font)
        self.channel_select_1.setCheckable(True)
        self.channel_select_1.setObjectName("channel_select_1")
        self.power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.power.setGeometry(QtCore.QRect(450, 10, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.power.setFont(font)
        self.power.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("power_button_symbol_cropped.PNG"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.power.setIcon(icon)
        self.power.setIconSize(QtCore.QSize(60, 60))
        self.power.setCheckable(True)
        self.power.setObjectName("power")
        self.volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_up.setGeometry(QtCore.QRect(100, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.volume_up.setFont(font)
        self.volume_up.setCheckable(False)
        self.volume_up.setObjectName("volume_up")
        self.volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volume_down.setGeometry(QtCore.QRect(100, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.volume_down.setFont(font)
        self.volume_down.setCheckable(False)
        self.volume_down.setObjectName("volume_down")
        self.channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_up.setGeometry(QtCore.QRect(320, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_up.setFont(font)
        self.channel_up.setCheckable(True)
        self.channel_up.setChecked(False)
        self.channel_up.setObjectName("channel_up")
        self.channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel_down.setGeometry(QtCore.QRect(320, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.channel_down.setFont(font)
        self.channel_down.setCheckable(True)
        self.channel_down.setObjectName("channel_down")
        self.mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mute.setGeometry(QtCore.QRect(240, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mute.setFont(font)
        self.mute.setCheckable(True)
        self.mute.setObjectName("mute")
        self.channel_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.channel_image.setGeometry(QtCore.QRect(150, 10, 250, 191))
        self.channel_image.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.channel_image.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.channel_image.setText("")
        self.channel_image.setPixmap(QtGui.QPixmap("Starting_Blank_TV_Screen.png"))
        self.channel_image.setScaledContents(True)
        self.channel_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.channel_image.setObjectName("channel_image")
        self.volume_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_slider.setEnabled(False)
        self.volume_slider.setGeometry(QtCore.QRect(160, 310, 241, 22))
        self.volume_slider.setMaximum(9)
        self.volume_slider.setPageStep(10)
        self.volume_slider.setProperty("value", 0)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(1)
        self.volume_slider.setObjectName("volume_slider")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 280, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.volume_output = QtWidgets.QLabel(parent=self.centralwidget)
        self.volume_output.setGeometry(QtCore.QRect(220, 330, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volume_output.setFont(font)
        self.volume_output.setText("")
        self.volume_output.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.volume_output.setObjectName("volume_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Television_Remote"))
        self.channel_select_7.setText(_translate("MainWindow", "7"))
        self.channel_select_9.setText(_translate("MainWindow", "9"))
        self.channel_select_8.setText(_translate("MainWindow", "8"))
        self.channel_select_6.setText(_translate("MainWindow", "6"))
        self.channel_select_5.setText(_translate("MainWindow", "5"))
        self.channel_select_4.setText(_translate("MainWindow", "4"))
        self.channel_select_3.setText(_translate("MainWindow", "3"))
        self.channel_select_2.setText(_translate("MainWindow", "2"))
        self.channel_select_1.setText(_translate("MainWindow", "1"))
        self.volume_up.setText(_translate("MainWindow", "Volume Up"))
        self.volume_down.setText(_translate("MainWindow", "Volume Down"))
        self.channel_up.setText(_translate("MainWindow", "Channel Up"))
        self.channel_down.setText(_translate("MainWindow", "Channel Down"))
        self.mute.setText(_translate("MainWindow", "Mute"))
        self.label.setText(_translate("MainWindow", "Volume Slider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())