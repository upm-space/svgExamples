import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QGraphicsView)

from PySide2.QtGui import QImage

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.img = QImage('svg/horizon_mechanics.svg')
        #self.img.load('svg/horizon_mechanics.svg')
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        #layout.addWidget(self.button)
        layout.addWidget(self.img)
        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        self.resize(400,500)




    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())