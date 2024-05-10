from PyQt6.QtWidgets import *
from Television_Remote import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 9
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 9

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__previous_volume = None
        self.__muted: bool = False
        self.__status: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

        self.power.clicked.connect(self.power_status)
        self.mute.clicked.connect(self.mute_status)
        self.channel_up.clicked.connect(self.channel_up_status)
        self.channel_down.clicked.connect(self.channel_down_status)
        self.volume_up.clicked.connect(self.volume_up_status)
        self.volume_down.clicked.connect(self.volume_down_status)
        self.volume_slider.valueChanged.connect(self.volume_slider_status)
        self.channel_select_1.clicked.connect(self.channel_select_status_1)
        self.channel_select_2.clicked.connect(self.channel_select_status_2)
        self.channel_select_3.clicked.connect(self.channel_select_status_3)
        self.channel_select_4.clicked.connect(self.channel_select_status_4)
        self.channel_select_5.clicked.connect(self.channel_select_status_5)
        self.channel_select_6.clicked.connect(self.channel_select_status_6)
        self.channel_select_7.clicked.connect(self.channel_select_status_7)
        self.channel_select_8.clicked.connect(self.channel_select_status_8)
        self.channel_select_9.clicked.connect(self.channel_select_status_9)

    def power_status(self) -> None:
        """
        Method to power tv On & Off with desired statuses.
        """
        if self.__status:
            self.__status = False
            self.__muted = False
            self.volume_slider.setEnabled(False)
            self.volume_slider.setProperty("value", 0)
            self.__channel = self.MIN_CHANNEL
            self.__volume = Television.MIN_VOLUME
            self.channel_image.setPixmap(QtGui.QPixmap('Starting_Blank_TV_Screen.png'))
            self.volume_output.setText('')
            print('Power is off')
        else:
            self.__status = True
            self.volume_slider.setEnabled(True)
            self.channel_image.setPixmap(QtGui.QPixmap('Static_Screen_Channel_0.jpg'))
            print('Power is on')

    def mute_status(self) -> None:
        """
        Method to bring volume to 0 and then back to last selected volume.
        """
        if self.__status:
            if self.__muted:
                self.volume_slider.setTracking(True)
                self.volume_output.setText(f"Volume: {self.__volume}")
                self.volume_slider.update()
                self.volume_slider.repaint()
                self.__muted = False
                self.volume_slider.setEnabled(True)
                print('TV is no longer muted')
            else:
                self.__muted = True
                self.volume_output.setText("Volume: 0")
                self.volume_slider.setEnabled(False)
                print('TV is muted')

    def channel_up_status(self) -> None:
        """
        Method to increase tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                if self.__channel == 1:
                    self.channel_image.setPixmap(QtGui.QPixmap('CN_Logo.png'))
                    print('Cartoon Network')
                elif self.__channel == 2:
                    self.channel_image.setPixmap(QtGui.QPixmap('CNN_Logo.jpg'))
                    print('CNN')
                elif self.__channel == 3:
                    self.channel_image.setPixmap(QtGui.QPixmap('Fox_News_Logo.png'))
                    print('Fox News')
                elif self.__channel == 4:
                    self.channel_image.setPixmap(QtGui.QPixmap('Nickelodeon_Logo.png'))
                    print('Nickelodeon')
                elif self.__channel == 5:
                    self.channel_image.setPixmap(QtGui.QPixmap('Discovery_Logo.jpg'))
                    print('Discovery')
                elif self.__channel == 6:
                    self.channel_image.setPixmap(QtGui.QPixmap('ID_Logo.png'))
                    print('ID')
                elif self.__channel == 7:
                    self.channel_image.setPixmap(QtGui.QPixmap('ESPN_Logo.png'))
                    print('ESPN')
                elif self.__channel == 8:
                    self.channel_image.setPixmap(QtGui.QPixmap('Game_Show_Network_Logo.webp'))
                    print('GSN')
                elif self.__channel == 9:
                    self.channel_image.setPixmap(QtGui.QPixmap('HGTV_Logo.png'))
                    print('Home & Garden TV')
            else:
                self.__channel = Television.MIN_CHANNEL
                self.channel_image.setPixmap(QtGui.QPixmap('Static_Screen_Channel_0.jpg'))
                print('Static Screen')

    def channel_down_status(self) -> None:
        """
        Method to decrease the channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                if self.__channel == 9:
                    self.channel_image.setPixmap(QtGui.QPixmap('HGTV_Logo.png'))
                    print('Home & Garden TV')
                elif self.__channel == 8:
                    self.channel_image.setPixmap(QtGui.QPixmap('Game_Show_Network_Logo.webp'))
                    print('GSN')
                elif self.__channel == 7:
                    self.channel_image.setPixmap(QtGui.QPixmap('ESPN_Logo.png'))
                    print('ESPN')
                elif self.__channel == 6:
                    self.channel_image.setPixmap(QtGui.QPixmap('ID_Logo.png'))
                    print('ID')
                elif self.__channel == 5:
                    self.channel_image.setPixmap(QtGui.QPixmap('Discovery_Logo.jpg'))
                    print('Discovery')
                elif self.__channel == 4:
                    self.channel_image.setPixmap(QtGui.QPixmap('Nickelodeon_Logo.png'))
                    print('Nickelodeon')
                elif self.__channel == 3:
                    self.channel_image.setPixmap(QtGui.QPixmap('Fox_News_Logo.png'))
                    print('Fox News')
                elif self.__channel == 2:
                    self.channel_image.setPixmap(QtGui.QPixmap('CNN_Logo.jpg'))
                    print('CNN')
                elif self.__channel == 1:
                    self.channel_image.setPixmap(QtGui.QPixmap('CN_Logo.png'))
                    print('Cartoon Network')
                elif self.__channel == 0:
                    self.channel_image.setPixmap(QtGui.QPixmap('Static_Screen_Channel_0.jpg'))
                    print('Static Screen')
            else:
                self.__channel = Television.MAX_CHANNEL
                self.channel_image.setPixmap(QtGui.QPixmap('HGTV_Logo.png'))
                print('Home & Garden TV')

    def volume_up_status(self) -> None:
        """
        Method to increase volume and call to volume slider to adjust.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.volume_slider.setEnabled(True)
                self.volume_slider.setTracking(True)
                self.volume_slider.setValue(self.__volume)
                self.volume_slider.update()
                self.volume_slider.repaint()
                self.__muted = False
            else:
                self.__volume = Television.MAX_VOLUME
                self.volume_slider.setEnabled(True)
                self.__muted = False
                print('Already at max volume')

    def volume_down_status(self) -> None:
        """
        Method to decrease volume and call to volume slider to adjust.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.volume_slider.setEnabled(True)
                self.volume_slider.setTracking(True)
                self.volume_slider.setValue(self.__volume)
                self.volume_slider.update()
                self.volume_slider.repaint()
                self.__muted = False
            else:
                self.__volume = Television.MIN_VOLUME
                self.volume_slider.setEnabled(True)
                self.__muted = False
                print('Already at min volume')

    def volume_slider_status(self):
        """
        Method to set volume with slider tool, volume up & down methods affect slider position.
        """
        if self.__status:
            if self.volume_slider:
                self.volume_output.setText("Volume: " + str(self.sender().value()))
                self.__volume = self.sender().value()
                print(f'Volume is now {self.__volume}')

    def channel_select_status_1(self):
        """
        Method to select channel 1 with numeric keypad.
        """
        if self.__status:
            self.__channel = 1
            self.channel_image.setPixmap(QtGui.QPixmap('CN_Logo.png'))
            print('Cartoon Network')

    def channel_select_status_2(self):
        """
        Method to select channel 2 with numeric keypad.
        """
        if self.__status:
            self.__channel = 2
            self.channel_image.setPixmap(QtGui.QPixmap('CNN_Logo.jpg'))
            print('CNN')

    def channel_select_status_3(self):
        """
        Method to select channel 3 with numeric keypad.
        """
        if self.__status:
            self.__channel = 3
            self.channel_image.setPixmap(QtGui.QPixmap('Fox_News_Logo.png'))
            print('Fox News')

    def channel_select_status_4(self):
        """
        Method to select channel 4 with numeric keypad.
        """
        if self.__status:
            self.__channel = 4
            self.channel_image.setPixmap(QtGui.QPixmap('Nickelodeon_Logo.png'))
            print('Nickelodeon')

    def channel_select_status_5(self):
        """
        Method to select channel 5 with numeric keypad.
        """
        if self.__status:
            self.__channel = 5
            self.channel_image.setPixmap(QtGui.QPixmap('Discovery_Logo.jpg'))
            print('Discovery')

    def channel_select_status_6(self):
        """
        Method to select channel 6 with numeric keypad.
        """
        if self.__status:
            self.__channel = 6
            self.channel_image.setPixmap(QtGui.QPixmap('ID_Logo.png'))
            print('ID')

    def channel_select_status_7(self):
        """
        Method to select channel 7 with numeric keypad.
        """
        if self.__status:
            self.__channel = 7
            self.channel_image.setPixmap(QtGui.QPixmap('ESPN_Logo.png'))
            print('ESPN')

    def channel_select_status_8(self):
        """
        Method to select channel 8 with numeric keypad.
        """
        if self.__status:
            self.__channel = 8
            self.channel_image.setPixmap(QtGui.QPixmap('Game_Show_Network_Logo.webp'))
            print('GSN')

    def channel_select_status_9(self):
        """
        Method to select channel 9 with numeric keypad.
        """
        if self.__status:
            self.__channel = 9
            self.channel_image.setPixmap(QtGui.QPixmap('HGTV_Logo.png'))
            print('Home & Garden TV')
