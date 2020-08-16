import sys
from PyQt4 import QtGui, QtCore

class ejemplo_GUI(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(350,100,300,300)
        self.setWindowTitle("Primer ejemplo de GUI con PyQt")
        salir = QtGui.QPushButton("Salir", self)
        salir.setGeometry(100,100,100,100)
        salir.clicked.connect(self.close)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mi_app = ejemplo_GUI()
    mi_app.show()
    sys.exit(app.exec_())
