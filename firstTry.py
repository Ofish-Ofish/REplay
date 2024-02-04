# Form implementation generated from reading ui file 'firstTry.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import os

def Frame(parent, **kwargs):
    frame = QtWidgets.QFrame(parent=parent)
    for key, value in kwargs.items():
        if key == "Geometry":
            frame.setGeometry(value)
        elif key == "MaxSize":
            frame.setMaximumSize(value)
        elif key == "MinSize":
            frame.setMinimumSize(value)
        elif key == "frameShape":
            frame.setFrameShape(value)
        elif key == "frameShadow":
            frame.setFrameShadow(value)
        elif key == "name":
            frame.setObjectName(value)
        elif key == "BackgroundColor":
            frame.setStyleSheet(value)
    return frame

def VecticalLayout(parent, **kwargs):
    layout = QtWidgets.QVBoxLayout(parent)
    for key, value in kwargs.items():
        if key == "name":
            layout.setObjectName(value)
    return layout

def horizontalLayout(parent, **kwargs):
    layout = QtWidgets.QHBoxLayout(parent)
    for key, value in kwargs.items():
        if key == "name":
            layout.setObjectName(value)
    return layout

def Label(parent, **kwargs):
    label = QtWidgets.QLabel(parent=parent)
    for key, value in kwargs.items():
        if  key == "Geometry":
            label.setGeometry(value)
        elif  key == "MaxSize":
            label.setMaximumSize(value)
        elif  key == "MinSize":
            label.setMinimumSize(value)
        elif key == "Text":
            label.setText(value)
        elif key == "Pic":
            label.setPixmap(value)
        elif key == "Scaling":
            label.setScaledContents(value)
        elif key == "name":
            label.setObjectName(value)
        elif key == "Font":
            label.setFont(value)
        elif key == "Color":
            label.setStyleSheet(value)


    return label

def Font(**kwargs):
    font = QtGui.QFont()
    for key, value in kwargs.items():
        if  key == "Family":
            font.setFamily(value)
        elif  key == "Point":
            font.setPointSize(value)

    return font

def PushBtn(parent, **kwargs):
    pushBtn = QtWidgets.QPushButton(parent=parent)
    for key, value in kwargs.items():
        if key == "Geometry":
            pushBtn.setGeometry(value)
        elif key == "MaxSize":
            pushBtn.setMaximumSize(value)
        elif key == "MinSize":
            pushBtn.setMinimumSize(value)
        elif key == "frameShape":
            pushBtn.setFrameShape(value)
        elif key == "frameShadow":
            pushBtn.setFrameShadow(value)
        elif key == "name":
            pushBtn.setObjectName(value)
        elif key == "BackgroundColor":
            pushBtn.setStyleSheet(value)
        elif key == "Text":
            pushBtn.setText(value)
        elif key == "Icon":
            pushBtn.setIcon(value)
        elif key == "IconSize":
            pushBtn.setIconSize(value)
    return pushBtn

def Icon(*args, **kwargs):
    icon = QtGui.QIcon()
    for key, value in kwargs.items():
        if key == "Pic":
            icon.addPixmap(value, *args)

    return icon

class Ui_identifier(object):
    def setupUi(self, Form):
        #fonts
        GEORGIA20 = Font(Family="Georgia",
                         Point=20,
                         )

        #screen objects
        self.identifier = Frame(Form,
                                Geometry=QtCore.QRect(10, 10, 782, 64),
                                MinSize=QtCore.QSize(0, 0),
                                MaxSize=QtCore.QSize(16777215, 64),
                                BackgroundColor="background-color: rgb(18, 18, 18);",
                                frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                name="identifier"
                            )
        self.identifierLayout = horizontalLayout(self.identifier,
                                                 name="horizontalLayout_2"
                                            )
        self.YourLibrarylabel = Label(self.identifier,
                                      MaxSize=QtCore.QSize(16777215, 64),
                                      Font=GEORGIA20,
                                      Color="color: rgb(241, 241, 241)",
                                      name="YourLibrarylabel"
                                )
        searchIcon = Icon(QtGui.QIcon.Mode.Normal,
                          QtGui.QIcon.State.Off,
                          Pic=QtGui.QPixmap("images/Mediamodifier-Design.svg"),
                    )
        self.pushButtonSearchPlaylist = PushBtn(self.identifier,
                                                MaxSize=QtCore.QSize(64, 64),
                                                Font=GEORGIA20,
                                                BackgroundColor="background-color: rgba(255, 255, 255, 0);",
                                                Text="",
                                                Icon=searchIcon,
                                                IconSize=QtCore.QSize(64, 64),
                                                name="pushButtonSearchPlaylist",
                                            )
        plusIcon = Icon(QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off,
                        Pic=QtGui.QPixmap("images/plus 3.svg"),
                    )
        self.pushButtonAddPlaylist = PushBtn(self.identifier,
                                             MaxSize=QtCore.QSize(64, 64),
                                             Font=GEORGIA20,
                                             BackgroundColor="background-color: rgba(255, 255, 255, 0);",
                                             Text="",
                                             Icon=plusIcon,
                                             IconSize=QtCore.QSize(32, 32),
                                             name="pushButtonAddPlaylist",
                                        )

        #adding together
        self.identifierLayout.addWidget(self.YourLibrarylabel)
        self.identifierLayout.addWidget(self.pushButtonSearchPlaylist)
        self.identifierLayout.addWidget(self.pushButtonAddPlaylist)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        return self.identifier

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.YourLibrarylabel.setText(_translate("Form", "Your Library"))

class Ui_PlaylistHolder(object):
    def setupUi(self, Form):
        self.Playlists = Frame(Form,
                               BackgroundColor="background-color: rgb(26, 26, 26);",
                               frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                               frameShadow=QtWidgets.QFrame.Shadow.Raised,
                               name="Playlists")
        self.PlaylistsLayout = VecticalLayout(self.Playlists,
                                              name="PlaylistsLayout"
                            )
        
        files = os.listdir("./playList")
        for i in range(len(files)):
            os.chdir(f"./playList/{files[i]}")
            txtfile = open(f"{files[i]}.txt","r")
            
            playlist = Ui_Playlist().setupUi(self.Playlists,
                                             f"playList/{files[i]}/{files[i]}.jpg",
                                             txtfile.readline().replace("_", " ").replace("\n",""),
                                             txtfile.readline().replace("_", " ").replace("\n",""),
                                             txtfile.readline().replace("_", " ").replace("\n",""))
            self.PlaylistsLayout.addWidget(playlist)
        # #creating playListWigit
        # self.PlaylistWidget = Ui_Playlist().setupUi(self.Playlists, "bagget","fish", "999")
        # #adding toghether
        # self.PlaylistsLayout.addWidget(self.PlaylistWidget)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        return self.Playlists

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

class Ui_Playlist(object):
    def setupUi(self, Form, *argv):
        os.chdir("..")
        os.chdir("..")
        #fonts
        GEORGIA16 = Font(Family="Georgia", Point=16)
        GEORGIA12 = Font(Family="Georgia", Point=12)

        #screen objects
        self.playlistWidget = Frame(Form,
                                    Geometry=QtCore.QRect(0, 240, 762, 100),
                                    MaxSize=QtCore.QSize(16777215, 128),
                                    frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                    frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                    name="playlistWidget",
                                )
        self.playlistWidgetLayout = horizontalLayout(self.playlistWidget,
                                                     name="playlistWidgetLayout"
                                                )
        self.framePic = Frame(self.playlistWidget,
                              MaxSize=QtCore.QSize(80, 80),
                              frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                              frameShadow=QtWidgets.QFrame.Shadow.Raised,
                              name="framePic",
                            )
        self.framePicLayout = horizontalLayout(self.framePic,
                                                   name="framePicLayout",
                                                )
        self.playlistPic = Label(self.framePic,
                                 MaxSize=QtCore.QSize(64, 64),
                                 Text="",
                                 Pic=QtGui.QPixmap(argv[0]),
                                 Scaling=True,
                                 name="playlistPic",
                            )
        self.playlistDetails = Frame(self.playlistWidget,
                                     MaxSize=QtCore.QSize(16777215, 80),
                                     frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                     frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                     name="playlistDetails",
                                )
        self.playlistDetailsLayout = VecticalLayout(self.playlistDetails,
                                                    name="playlistDetailsLayout",
                                                )
        self.playListName = Label(self.playlistDetails,
                                  MinSize=QtCore.QSize(0, 0,),
                                  MaxSize=QtCore.QSize(16777215, 50),
                                  Font=GEORGIA16,
                                  Color="color: rgb(202, 202, 202);",
                                  name="playListName",
                            )
        self.artist = Label(self.playlistDetails,
                            MaxSize=QtCore.QSize(16777215, 50),
                            Font=GEORGIA12,
                            Color="color: rgb(202, 202, 202);",
                            name="artist",
                        )
        self.numOfSongs = Frame(self.playlistWidget,
                                MinSize=QtCore.QSize(120, 0),
                                MaxSize=QtCore.QSize(100, 80),
                                frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                name="numOfSongs",
                            )
        self.numOfSongsLayout = VecticalLayout(self.numOfSongs,
                                               name="numOfSongsLayout",
                                            )
        self.songNum = Label(self.numOfSongs,
                             MinSize=QtCore.QSize(0, 0),
                             MaxSize=QtCore.QSize(200, 16777215),
                             Font=GEORGIA12,
                             Color="color: rgb(202, 202, 202);",
                             name="songNum",
                        )
        self.emptySpace = Label(self.numOfSongs,
                                Text="",
                                name="emptySpace",
                            )

        #adding together
        self.framePicLayout.addWidget(self.playlistPic)
        self.playlistWidgetLayout.addWidget(self.framePic)
        self.playlistDetailsLayout.addWidget(self.playListName)
        self.playlistDetailsLayout.addWidget(self.artist)
        self.playlistWidgetLayout.addWidget(self.playlistDetails)
        self.numOfSongsLayout.addWidget(self.songNum)
        self.numOfSongsLayout.addWidget(self.emptySpace)
        self.playlistWidgetLayout.addWidget(self.numOfSongs)

        self.retranslateUi(Form,*argv)
        QtCore.QMetaObject.connectSlotsByName(Form)

        return self.playlistWidget

    def retranslateUi(self, Form, *argv):
        _translate = QtCore.QCoreApplication.translate
        self.playListName.setText(_translate("Form", argv[1]))
        self.artist.setText(_translate("Form", argv[2]))
        self.songNum.setText(_translate("Form", f"{argv[3]} songs"))

class Ui_Footer(object):

    def setupUi(self, Form):
        #fonts
        GEORGIA16 = Font(Family="Georgia", Point=16)
        GEORGIA12 = Font(Family="Georgia", Point=12)
        GEORGIA9 = Font(Family="Georgia", Point=9)

        #screen objects
        self.footer = Frame(Form,
                            MinSize=QtCore.QSize(0, 0),
                            MaxSize=QtCore.QSize(16777215, 90),
                            frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                            frameShadow=QtWidgets.QFrame.Shadow.Raised,
                            name="footer",
                        )
        self.footerLayout = horizontalLayout(self.footer,
                                                 name="footerLayout",
                                            )
        self.footerSearchFrame = Frame(self.footer,
                                       MaxSize=QtCore.QSize(100, 100),
                                       frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                       frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                       name="footerSearchFrame",
                                    )
        self.footerSearchFrameLayout = VecticalLayout(self.footerSearchFrame,
                                                      name="footerSearchFrameLayout",
                                                    )
        searchIcon = Icon(QtGui.QIcon.Mode.Normal,
                          QtGui.QIcon.State.Off,
                          Pic=QtGui.QPixmap("images/Mediamodifier-Design.svg"),
                        )
        self.footerSearchBtn = PushBtn(self.footerSearchFrame,
                                       MaxSize=QtCore.QSize(64, 64),
                                       BackgroundColor="background-color: rgba(255, 255, 255, 0);",
                                       Text="",
                                       Icon=searchIcon,
                                       IconSize=QtCore.QSize(64, 64),
                                       name="footerSearchBtn",
                                    )
        self.searchLabel = Label(self.footerSearchFrame,
                                 Font=GEORGIA9,
                                 Color="color: rgb(241, 241, 241)",
                                 name="searchLabel",
                            )
        self.footerLibraryFrame = Frame(self.footer,
                                        MaxSize=QtCore.QSize(100, 100),
                                        frameShape=QtWidgets.QFrame.Shape.StyledPanel,
                                        frameShadow=QtWidgets.QFrame.Shadow.Raised,
                                        name="footerLibraryFrame",
                                    )
        self.footerLibraryFrameLayout = VecticalLayout(self.footerLibraryFrame,
                                                       name="footerLibraryFrameLayout",
                                                )
        libraryIcon = Icon(QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off,
                            Pic=QtGui.QPixmap("images/whiote libraray.svg"),
                        )
        self.footerLibraryhBtn = PushBtn(self.footerLibraryFrame,
                                         MaxSize=QtCore.QSize(64, 64),
                                         BackgroundColor="background-color: rgba(255, 255, 255, 0);",
                                         Text="",
                                         Icon=libraryIcon,
                                         IconSize=QtCore.QSize(64, 64),
                                         name="footerLibraryhBtn",
                                    )
        self.libraryLabel = Label(self.footerLibraryFrame,
                                  Font=GEORGIA9,
                                  Color="color: rgb(241, 241, 241);",
                                  name="libraryLabel",
                            )

        #adding together
        self.footerSearchFrameLayout.addWidget(self.footerSearchBtn)
        self.footerSearchFrameLayout.addWidget(self.searchLabel, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.footerLayout.addWidget(self.footerSearchFrame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.footerLibraryFrameLayout.addWidget(self.footerLibraryhBtn)
        self.footerLibraryFrameLayout.addWidget(self.libraryLabel)
        self.footerLayout.addWidget(self.footerLibraryFrame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        return self.footer

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchLabel.setText(_translate("Form", "Search"))
        self.libraryLabel.setText(_translate("Form", "Your Library"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindowLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainWindowLayout.setObjectName("MainWindowLayout")
        self.identifier = Ui_identifier().setupUi(self.centralwidget)
        self.Playlists = Ui_PlaylistHolder().setupUi(self.centralwidget)
        self.footer = Ui_Footer().setupUi(self.Playlists)

        #adding together
        self.MainWindowLayout.addWidget(self.identifier)
        self.MainWindowLayout.addWidget(self.Playlists)
        self.MainWindowLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
