# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Dosyalarım/Resimler/123.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 271))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lbl_player = QtWidgets.QLabel(self.groupBox)
        self.lbl_player.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.lbl_player.setObjectName("lbl_player")
        self.lbl_ai = QtWidgets.QLabel(self.groupBox)
        self.lbl_ai.setGeometry(QtCore.QRect(10, 180, 47, 13))
        self.lbl_ai.setObjectName("lbl_ai")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(10, 310, 75, 51))
        self.btn_exit.setObjectName("btn_exit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 351, 371))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 333, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn1.setFont(font)
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.gridLayout_2.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn2.setFont(font)
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.gridLayout_2.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn3.setFont(font)
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.gridLayout_2.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn4.setFont(font)
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.gridLayout_2.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn5.setFont(font)
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.gridLayout_2.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn6.setFont(font)
        self.btn6.setAcceptDrops(False)
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.gridLayout_2.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn7.setFont(font)
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.gridLayout_2.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn8.setFont(font)
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.gridLayout_2.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn9.setFont(font)
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        self.gridLayout_2.addWidget(self.btn9, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.radioButton.setText(_translate("MainWindow", "Kolay"))
        self.radioButton_2.setText(_translate("MainWindow", "Zor"))
        self.label.setText(_translate("MainWindow", "Oyuncu : "))
        self.label_2.setText(_translate("MainWindow", "Yapay Zeka : "))
        self.lbl_player.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_ai.setText(_translate("MainWindow", "TextLabel"))
        self.btn_exit.setText(_translate("MainWindow", "Kapat"))