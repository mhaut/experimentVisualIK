# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created: Fri Jul 10 13:54:16 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_guiDlg(object):
    def setupUi(self, guiDlg):
        guiDlg.setObjectName(_fromUtf8("guiDlg"))
        guiDlg.resize(915, 569)
        self.verticalLayout = QtGui.QVBoxLayout(guiDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.testButton = QtGui.QPushButton(guiDlg)
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.horizontalLayout.addWidget(self.testButton)
        self.stopButton = QtGui.QPushButton(guiDlg)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(guiDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.errorLabel = QtGui.QLabel(guiDlg)
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.verticalLayout.addWidget(self.errorLabel)
        self.scrollArea_2 = QtGui.QScrollArea(guiDlg)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 893, 205))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setMinimumSize(QtCore.QSize(800, 100))
        self.textEdit_2.setMaximumSize(QtCore.QSize(800, 200))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_2.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.line_2 = QtGui.QFrame(guiDlg)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.poseLabel = QtGui.QLabel(guiDlg)
        self.poseLabel.setObjectName(_fromUtf8("poseLabel"))
        self.verticalLayout.addWidget(self.poseLabel)
        self.scrollArea = QtGui.QScrollArea(guiDlg)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 874, 341))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setMinimumSize(QtCore.QSize(800, 300))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.ficheroLabel = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.ficheroLabel.setObjectName(_fromUtf8("ficheroLabel"))
        self.gridLayout.addWidget(self.ficheroLabel, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(guiDlg)
        QtCore.QMetaObject.connectSlotsByName(guiDlg)

    def retranslateUi(self, guiDlg):
        guiDlg.setWindowTitle(_translate("guiDlg", "visualiktester", None))
        self.testButton.setText(_translate("guiDlg", "Run test", None))
        self.stopButton.setText(_translate("guiDlg", "Stop", None))
        self.errorLabel.setText(_translate("guiDlg", "Error Detectado:", None))
        self.poseLabel.setText(_translate("guiDlg", "Pose Actual:", None))
        self.ficheroLabel.setText(_translate("guiDlg", "Datos del fichero: ", None))

