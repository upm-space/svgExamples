import sys
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2 import QtCore


# example event handler
def quit_app():
    global application
    #print("Quit!")
    #application.exit()
    global label
    #label.setProperty("rotation","45")
    # ver especificaciones
    # https://srinikom.github.io/pyside-docs/PySide/QtGui/QWidget.html#PySide.QtGui.PySide.QtGui.QWidget.setGeometry
    label.setGeometry(50, 140, picture.width(), picture.height())


# base application object for our app
application = QApplication(sys.argv)

# Create a Window
window = QWidget()
window.setWindowTitle("View Image")

# button
button = QPushButton("Quit", window)

# on click handler
button.clicked.connect(quit_app)

# Load Pic
picture = QPixmap("svg/horizon_mechanics.svg")
picture2 = QPixmap("svg/horizon_circle.svg")

# set up the label widget to display the pic


label2 = QLabel(window)
label2.setPixmap(picture2)
label2.setGeometry(QtCore.QRect(10, 40, picture2.width(), picture2.height()))

label = QLabel(window)
label.setPixmap(picture)
label.setGeometry(QtCore.QRect(10, 40, picture.width(), picture.height()))
label.setProperty("set_rotation",45)
label._rotation = 45

#https://stackoverflow.com/questions/31892557/rotating-a-pixmap-in-pyqt4-gives-undesired-translation
#ixmap = QtGui.QPixmap(self.img)
rotation = 45

transform = QTransform().rotate(rotation)
pixmap = label.pixmap().transformed(transform, QtCore.Qt.SmoothTransformation)

#---- update label ----

label.setPixmap(pixmap)

# embiggen the window to correctly fit the pic
window.resize(picture.width()+20, picture.height()+100)
window.show()

# Let QT do its thing
sys.exit(application.exec_())

# rotation example
#https://wiki.qt.io/Using-QtMobility-sensors-and-QML-from-PySide

# link donce carga una imagen en un QImage
#ttps://stackoverflow.com/questions/31892557/rotating-a-pixmap-in-pyqt4-gives-undesired-translation