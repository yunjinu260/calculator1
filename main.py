import sys
from PyQt5.QtWidgets import QApplication, QWidget
class Calculator1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator1')
        self.resize(256,256)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator1()
    sys.exit(app.exec_())