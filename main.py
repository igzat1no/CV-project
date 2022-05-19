import sys
from PyQt5.QtWidgets import QApplication, QWidget

import ui

class UI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui.Ui_UI()
        self.ui.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = UI()
    myWindow.show()
    n = app.exec()
    sys.exit(n)