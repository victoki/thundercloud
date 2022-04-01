#Thundercloud UI Functionality

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import sys
import tc_ui_mainWindow as tcMainUi
import tcExport as tcExport
from pprint import pprint

# -------------------------------------------------------------------------------------------------
# get maya's main window, because python garbage collection things need it as a parent asdfdfgfghfh
def getMayaMainWindow():
    
    qtApp = QtWidgets.QApplication.instance() # get the qApp instance if it exists.
    if not qtApp:
        qtApp = QtWidgets.QApplication(sys.argv)
    
    mayaMainWindow = next(w for w in qtApp.topLevelWidgets() if w.objectName()=="MayaWindow")

    return mayaMainWindow
# -------------------------------------------------------------------------------------------------

# init main dialogue window
class tcMainDialog(QtWidgets.QMainWindow):
        
    def __init__(self, parent=getMayaMainWindow()):
        super(tcMainDialog, self).__init__(parent)
        
        # create from the generated qt designer ui
        self.ui = tcMainUi.Ui_MainWindow(self)
        self.ui.setupUi(self)
        
        self.tree = self.ui.exportTreeView
        self.treeModel = QtGui.QStandardItemModel()
        self.tree.setModel(self.treeModel)
        self.rootItem = self.tree.model().invisibleRootItem()
        
        self.buildExportTreeView()
        
        #Ui elements
        self.createConnections()
       
    def buildExportTreeView(self):
        sceneLightData = tcExport.buildSceneLightData()
        
        if sceneLightData == {}:
            self.treeModel.setHorizontalHeaderLabels(['No Lights Found in Current Scene'])
        else:
            self.treeModel.setHorizontalHeaderLabels(['Current Scene Lights'])   
            
        for lightName in sceneLightData:
            
            self.lightEntry = self.buildRow(self.rootItem, lightName + " (" + sceneLightData[lightName]['lightType'] + ")")
            self.transNode = self.buildRow(self.lightEntry, sceneLightData[lightName]["transform"]["name"] + " (Transform)")
            self.shapeNode = self.buildRow(self.lightEntry, sceneLightData[lightName]["shape"]["name"] + " (Shape)")
             
            for attr in sceneLightData[lightName]["transform"]:
                if attr != "name":
                    self.transAttr = self.buildRow(self.transNode, attr + " (" + str(sceneLightData[lightName]["transform"][attr]) + ")")
                        
            for attr in sceneLightData[lightName]["shape"]:
                if attr != "name":
                    self.shapeAttr = self.buildRow(self.shapeNode, attr + " (" + str(sceneLightData[lightName]["shape"][attr]) + ")")
          
    
    def buildRow(self, parentName, itemLabel):
        nodeName = QtGui.QStandardItem(itemLabel)
        nodeName.setCheckable(True)
        nodeName.setCheckState(QtCore.Qt.Checked)
        parentName.appendRow(nodeName)
            
        return nodeName
        
    def reloadExportTreeView(self, inputDict):
        self.treeModel.removeRows(0, self.treeModel.rowCount())
        self.buildExportTreeView()
    
    def toggleTree(self, operation):
        treeRows = self.rootItem.rowCount()
        treeCols = self.rootItem.columnCount()
        
        for i in range(0, treeRows):
            lightName = self.rootItem.child(i)
            
            if operation == "deselect":
                lightName.setCheckState(QtCore.Qt.Unchecked)
            elif operation == "select":
                lightName.setCheckState(QtCore.Qt.Checked)
                
            shapeTransNodes = lightName.rowCount()
            
            for row in range(0, shapeTransNodes):
                for col in range(0, treeCols):
                    currentRow = lightName.child(row, col)
                    
                    if operation == "deselect":
                        currentRow.setCheckState(QtCore.Qt.Unchecked)
                    elif operation == "select":
                        currentRow.setCheckState(QtCore.Qt.Checked)
                        
                    attrNodes = currentRow.rowCount()
                    
                    for subrow in range(0, attrNodes):
                        for subcol in range(0, treeCols):
                            currentAttr = currentRow.child(subrow, subcol)
                            
                            if operation == "deselect":
                                currentAttr.setCheckState(QtCore.Qt.Unchecked)
                            elif operation == "select":
                                currentAttr.setCheckState(QtCore.Qt.Checked)
                    
  
    def createConnections(self):
        #hook up the ui
        self.ui.exportSelectAllButton.clicked.connect(self.select_all)
        self.ui.exportSelectionClearButton.clicked.connect(self.select_none)
        self.ui.exportRunButton.clicked.connect(self.exportCheckedLights)
        self.ui.exportReloadButton.clicked.connect(self.reloadExportTreeView)
        #self.ui.tree.itemChanged.connect(self.getIndex)
        
    def select_all(self):
        self.toggleTree("select")
        
    def select_none(self):
        self.toggleTree("deselect")
        
    def toggleChildren(self, row, col):
        print('got click')
        
    def getParentIndex(self, item):
        itemRow = item.row()
        itemCol = item.column()
        print(itemRow + " " + itemColumn)
        
    def exportCheckedLights(self):
        exportData = {}
        treeRows = self.rootItem.rowCount()
        treeCols = self.rootItem.columnCount()
        
        #Welcome to tree iteration hell (press f to pay respects - RIP)
        for i in range(0, treeRows):
            lightName = self.rootItem.child(i)
            shapeTransNodes = lightName.rowCount()
            if lightName.checkState() == QtCore.Qt.Checked:
                explode = lightName.text().split()
                itemName = explode[0]
                type = explode[1].replace("(", "").replace(")", "")
                
                exportData[itemName] = {}
                exportData[itemName]["lightType"] = type
                
                for row in range(0, shapeTransNodes):
                    for col in range(0, treeCols):
                        currentRow = lightName.child(row, col)
                        attrNodes = currentRow.rowCount()
                        
                        if currentRow.checkState() == QtCore.Qt.Checked:
                            explode = currentRow.text().split()
                            subNodeName = explode[0]
                            subNodeType = explode[1].replace("(", "").replace(")", "").lower()
                            exportData[itemName][subNodeType] = {}
                            exportData[itemName][subNodeType]["name"] = subNodeName
                            
                            for subrow in range(0, attrNodes):
                                for subcol in range(0, treeCols):
                                    currentAttr = currentRow.child(subrow, subcol)
                                    if currentAttr.checkState() == QtCore.Qt.Checked:
                                        explode = currentAttr.text().split()
                                        attrName = explode[0]
                                        value = explode[1].replace("(", "").replace(")", "")
                                        exportData[itemName][subNodeType][attrName] = value
        tcExport.exportJson(exportData)
        
                   
# show the main window dialogue
if __name__ == "__main__":
        tcDialog = tcMainDialog()
        tcDialog.show()