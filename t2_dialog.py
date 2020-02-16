from PyQt5.QtGui import *

# msg = QMessageBox()
# msg.setText("This is a simple information message.")
# msg.show()

def openMain_dialog():
    msg = QMessageBox()
    msg.setText("This is a simple information message.")
    #msg.show()
    return msg

def openFile_dialog():
    qfd = QFileDialog()
    title = 'Open File'
    path = "C:/Users/soiqu/Desktop/2000/"
    return QFileDialog.getOpenFileName(qfd, title, path)
    
# m=openMain_dialog()
# m.show()
f=openFile_dialog()
print(f[0])