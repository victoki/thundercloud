#UI for running processes in Thundercloud. Built with QT Designer.

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 211)
        Dialog.setMinimumSize(QSize(401, 211))
        Dialog.setMaximumSize(QSize(401, 211))
        self.tcOutputWindow = QPlainTextEdit(Dialog)
        self.tcOutputWindow.setObjectName(u"tcOutputWindow")
        self.tcOutputWindow.setGeometry(QRect(10, 10, 381, 121))
        self.doneButton = QPushButton(Dialog)
        self.doneButton.setObjectName(u"doneButton")
        self.doneButton.setGeometry(QRect(210, 172, 181, 31))
        self.doneButton.setCheckable(False)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 172, 191, 31))
        self.tcProgressBar = QProgressBar(Dialog)
        self.tcProgressBar.setObjectName(u"tcProgressBar")
        self.tcProgressBar.setGeometry(QRect(10, 140, 381, 23))
        self.tcProgressBar.setValue(0)
        self.tcProgressBar.setTextVisible(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Processing Data", None))
        self.doneButton.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi
