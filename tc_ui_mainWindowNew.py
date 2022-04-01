from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        super(Ui_MainWindow, self).__init__()

        self.centralwidget = QWidget(MainWindow)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.exportTab = QWidget()
        self.exportReloadButton = QPushButton(self.exportTab)
        self.exportSelectAllButton = QPushButton(self.exportTab)
        self.exportSelectionClearButton = QPushButton(self.exportTab)
        self.exportTreeView = QTreeView(self.exportTab)
        self.exportRunButton = QPushButton(self.exportTab)
        self.exportLightSearch = QLineEdit(self.exportTab)
        self.exportSortComboBox = QComboBox(self.exportTab)
        self.importTab = QWidget()
        self.importLoadJsonButton = QPushButton(self.importTab)
        self.importRunButton = QPushButton(self.importTab)
        self.importClearSelection = QPushButton(self.importTab)
        self.importSortBox = QComboBox(self.importTab)
        self.importLightSearch = QLineEdit(self.importTab)
        self.importSelectAllButton = QPushButton(self.importTab)
        self.importTreeView = QTreeView(self.importTab)
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(295, 580)
        MainWindow.setMinimumSize(QSize(295, 580))
        MainWindow.setMaximumSize(QSize(295, 580))
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 277, 561))
        self.exportTab = QWidget()
        self.exportTab.setObjectName(u"exportTab")
        self.gridLayoutWidget_4 = QWidget(self.exportTab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 271, 541))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(4)
        self.gridLayout_5.setVerticalSpacing(7)
        self.gridLayout_5.setContentsMargins(7, 7, 5, 9)
        self.exportSearchBox = QLineEdit(self.gridLayoutWidget_4)
        self.exportSearchBox.setObjectName(u"exportSearchBox")
        self.exportSearchBox.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.exportSearchBox, 3, 0, 1, 1)

        self.exportReloadButton = QPushButton(self.gridLayoutWidget_4)
        self.exportReloadButton.setObjectName(u"exportReloadButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportReloadButton.sizePolicy().hasHeightForWidth())
        self.exportReloadButton.setSizePolicy(sizePolicy)
        self.exportReloadButton.setMinimumSize(QSize(0, 31))

        self.gridLayout_5.addWidget(self.exportReloadButton, 0, 0, 1, 1)

        self.exportTreeView = QTreeView(self.gridLayoutWidget_4)
        self.exportTreeView.setObjectName(u"exportTreeView")

        self.gridLayout_5.addWidget(self.exportTreeView, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.exportSelectAllButton = QPushButton(self.gridLayoutWidget_4)
        self.exportSelectAllButton.setObjectName(u"exportSelectAllButton")
        self.exportSelectAllButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.exportSelectAllButton)

        self.exportSelectionClearButton = QPushButton(self.gridLayoutWidget_4)
        self.exportSelectionClearButton.setObjectName(u"exportSelectionClearButton")
        self.exportSelectionClearButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.exportSelectionClearButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.exportSortBox = QComboBox(self.gridLayoutWidget_4)
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.addItem("")
        self.exportSortBox.setObjectName(u"exportSortBox")
        self.exportSortBox.setMaxVisibleItems(10)

        self.gridLayout_5.addWidget(self.exportSortBox, 2, 0, 1, 1)

        self.exportRunButton = QPushButton(self.gridLayoutWidget_4)
        self.exportRunButton.setObjectName(u"exportRunButton")
        self.exportRunButton.setMinimumSize(QSize(0, 31))

        self.gridLayout_5.addWidget(self.exportRunButton, 5, 0, 1, 1)

        self.tabWidget.addTab(self.exportTab, "")
        self.importTab = QWidget()
        self.importTab.setObjectName(u"importTab")
        self.gridLayoutWidget_3 = QWidget(self.importTab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 271, 541))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setContentsMargins(7, 7, 5, 9)
        self.importRunButton = QPushButton(self.gridLayoutWidget_3)
        self.importRunButton.setObjectName(u"importRunButton")
        self.importRunButton.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.importRunButton, 5, 0, 1, 1)

        self.importSearchBox = QLineEdit(self.gridLayoutWidget_3)
        self.importSearchBox.setObjectName(u"importSearchBox")
        self.importSearchBox.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.importSearchBox, 3, 0, 1, 1)

        self.importLoadFileButton = QPushButton(self.gridLayoutWidget_3)
        self.importLoadFileButton.setObjectName(u"importLoadFileButton")
        sizePolicy.setHeightForWidth(self.importLoadFileButton.sizePolicy().hasHeightForWidth())
        self.importLoadFileButton.setSizePolicy(sizePolicy)
        self.importLoadFileButton.setMinimumSize(QSize(0, 31))

        self.gridLayout_3.addWidget(self.importLoadFileButton, 0, 0, 1, 1)

        self.importSortBox = QComboBox(self.gridLayoutWidget_3)
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.addItem("")
        self.importSortBox.setObjectName(u"importSortBox")
        self.importSortBox.setMaxVisibleItems(10)

        self.gridLayout_3.addWidget(self.importSortBox, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.inportSelectAllButton = QPushButton(self.gridLayoutWidget_3)
        self.inportSelectAllButton.setObjectName(u"inportSelectAllButton")
        self.inportSelectAllButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.inportSelectAllButton)

        self.importSelectionClearButton = QPushButton(self.gridLayoutWidget_3)
        self.importSelectionClearButton.setObjectName(u"importSelectionClearButton")
        self.importSelectionClearButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.importSelectionClearButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.importTreeView = QTreeView(self.gridLayoutWidget_3)
        self.importTreeView.setObjectName(u"importTreeView")

        self.gridLayout_3.addWidget(self.importTreeView, 4, 0, 1, 1)

        self.tabWidget.addTab(self.importTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thundercloud Lights", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.exportSearchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.exportReloadButton.setText(QCoreApplication.translate("MainWindow", u"Reload Lights", None))
        self.exportSelectAllButton.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.exportSelectionClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.exportSortBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sorting: Name (Descending)", None))
        self.exportSortBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sorting: Name (Ascending)", None))
        self.exportSortBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Sorting: Light Type (Descending)", None))
        self.exportSortBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Sorting: Light Type (Ascending)", None))
        self.exportSortBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Only Show: Ambient Lights", None))
        self.exportSortBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Only Show: Directional Light", None))
        self.exportSortBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Only Show: Point Lights", None))
        self.exportSortBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Only Show: Spot Lights", None))
        self.exportSortBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Only Show: Area Light", None))
        self.exportSortBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Only Show: Volume Light", None))

        self.exportSortBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Sorting: Name (Descending)", None))
        self.exportRunButton.setText(QCoreApplication.translate("MainWindow", u"Export Selected to JSON", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.exportTab), QCoreApplication.translate("MainWindow", u"Export", None))
        self.importRunButton.setText(QCoreApplication.translate("MainWindow", u"Export Selected Lights to Scene", None))
        self.importSearchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.importLoadFileButton.setText(QCoreApplication.translate("MainWindow", u"Load Json File", None))
        self.importSortBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sorting: Name (Descending)", None))
        self.importSortBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sorting: Name (Ascending)", None))
        self.importSortBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Sorting: Light Type (Descending)", None))
        self.importSortBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Sorting: Light Type (Ascending)", None))
        self.importSortBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Only Show: Ambient Lights", None))
        self.importSortBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Only Show: Directional Light", None))
        self.importSortBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Only Show: Point Lights", None))
        self.importSortBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Only Show: Spot Lights", None))
        self.importSortBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Only Show: Area Light", None))
        self.importSortBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Only Show: Volume Light", None))

        self.importSortBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Sorting: Name (Descending)", None))
        self.inportSelectAllButton.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.importSelectionClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.importTab), QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi

