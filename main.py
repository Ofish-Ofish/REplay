# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.Playlists = QtWidgets.QFrame(parent=Form)
        self.Playlists.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.Playlists.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Playlists.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Playlists.setObjectName("Playlists")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Playlists)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
