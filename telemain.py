from television_remote_logic import *


def main():
    application = QApplication([])
    window = Television()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
