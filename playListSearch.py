# Form implementation generated from reading ui file 'playListSearch.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.identifier = QtWidgets.QFrame(parent=Form)
        self.identifier.setGeometry(QtCore.QRect(10, 10, 782, 64))
        self.identifier.setMinimumSize(QtCore.QSize(0, 0))
        self.identifier.setMaximumSize(QtCore.QSize(16777215, 64))
        self.identifier.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.identifier.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.identifier.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.identifier.setObjectName("identifier")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.identifier)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.YourLibrarylabel = QtWidgets.QLabel(parent=self.identifier)
        self.YourLibrarylabel.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        self.YourLibrarylabel.setFont(font)
        self.YourLibrarylabel.setStyleSheet("color: rgb(241, 241, 241)")
        self.YourLibrarylabel.setObjectName("YourLibrarylabel")
        self.horizontalLayout_2.addWidget(self.YourLibrarylabel)
        self.pushButtonSearchPlaylist = QtWidgets.QPushButton(parent=self.identifier)
        self.pushButtonSearchPlaylist.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButtonSearchPlaylist.setFont(font)
        self.pushButtonSearchPlaylist.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButtonSearchPlaylist.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Mediamodifier-Design.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearchPlaylist.setIcon(icon)
        self.pushButtonSearchPlaylist.setIconSize(QtCore.QSize(64, 64))
        self.pushButtonSearchPlaylist.setObjectName("pushButtonSearchPlaylist")
        self.horizontalLayout_2.addWidget(self.pushButtonSearchPlaylist)
        self.pushButtonAddPlaylist = QtWidgets.QPushButton(parent=self.identifier)
        self.pushButtonAddPlaylist.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.pushButtonAddPlaylist.setFont(font)
        self.pushButtonAddPlaylist.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButtonAddPlaylist.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/plus 3.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonAddPlaylist.setIcon(icon1)
        self.pushButtonAddPlaylist.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonAddPlaylist.setObjectName("pushButtonAddPlaylist")
        self.horizontalLayout_2.addWidget(self.pushButtonAddPlaylist)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.YourLibrarylabel.setText(_translate("Form", "Your LIbrary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
