# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre.ui'
#
# Created: Thu Jan 18 16:09:38 2018
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(984, 738)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 620, 110, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 345, 111, 21))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.VitesseTimerlSlider = QtGui.QSlider(self.centralwidget)
        self.VitesseTimerlSlider.setGeometry(QtCore.QRect(800, 400, 160, 16))
        self.VitesseTimerlSlider.setMaximum(1000)
        self.VitesseTimerlSlider.setSingleStep(100)
        self.VitesseTimerlSlider.setPageStep(100)
        self.VitesseTimerlSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VitesseTimerlSlider.setObjectName(_fromUtf8("VitesseTimerlSlider"))
        self.PourcentagelSlider = QtGui.QSlider(self.centralwidget)
        self.PourcentagelSlider.setGeometry(QtCore.QRect(800, 290, 160, 16))
        self.PourcentagelSlider.setMaximum(99)
        self.PourcentagelSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PourcentagelSlider.setObjectName(_fromUtf8("PourcentagelSlider"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 260, 111, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 380, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.PourcentagelineEdit = QtGui.QLineEdit(self.centralwidget)
        self.PourcentagelineEdit.setGeometry(QtCore.QRect(860, 330, 41, 20))
        self.PourcentagelineEdit.setObjectName(_fromUtf8("PourcentagelineEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 530, 111, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_Perco = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_Perco.setGeometry(QtCore.QRect(640, 610, 113, 20))
        self.lineEdit_Perco.setObjectName(_fromUtf8("lineEdit_Perco"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 480, 111, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 570, 111, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 430, 111, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.VitesseTimerlSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.VitessevalueChanged)
        QtCore.QObject.connect(self.PourcentagelSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.PourcentagevalueChanged)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.StartCalcul)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ArretCalcul)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.StartResultat)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.NouveauDessin)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "FIN", None))
        self.label_2.setText(_translate("MainWindow", "   Pourcentage Sable", None))
        self.label_3.setText(_translate("MainWindow", "  Vitesse Eau", None))
        self.pushButton_3.setText(_translate("MainWindow", "Calcul", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_4.setText(_translate("MainWindow", "Resultat", None))
        self.pushButton_5.setText(_translate("MainWindow", "NouveauDes", None))

