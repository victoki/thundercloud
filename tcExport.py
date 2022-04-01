# Thundercloud: 'Lightening' for your scenes.
# Exports/Imports your scene lights to/from JSON
# v1.0
# Author: Victoria King

import maya.cmds as cmds
import json

filePath = "D:\\"
fileName = "tcLightData"

#capture lights in scene
def captureSceneLights():
    sceneLights = cmds.ls(lights=True)
    return sceneLights

#retrieve transform node from light shape node
def getParentNode(shapeNode):
    parentTrans = cmds.listRelatives(shapeNode, parent=True)
    return parentTrans[0]
       
        
#get light type (from light in a scene)
def getLightTypeFromScene(lightName):
    lightType = cmds.nodeType(lightName)
    return lightType
    
    
def getLightDefaultValue(attr):
    lightDefaults = {
        "translateX": 0,
        "translateY": 0,
        "translateZ": 0,
        "rotateX": 0,
        "rotateY": 0,
        "rotateZ": 0,
        "scaleX": 1,
        "scaleY": 1,
        "scaleZ": 1,
        "visibility": "true",
        "colorR": 1,
        "colorG": 1,
        "colorB": 1,
        "intensity": 1,
        "useRayTraceShadows": "true",
        "shadColorR": 0,
        "shadColorG": 0,
        "shadColorB": 0,
        "useDepthMapShadows": "false",
        "dmapBias": 0.001,
        "coneAngle": 40,
        "penumbraAngle": 0,
        "dropoff": 0,
        "aiExposure": 0,
        "aiSpread": 0,
        "aiRoundness": 0,
        "aiSoftEdge": 0,
        "aiAngle": 0,
        "aiRadius": 0   
    }
    
    return lightDefaults[attr]
      
    
#build dictionary entries for a light    
def getAttributes(nodeName, isShapeNode):
    attrList = {}
    attrWorkList = cmds.listAttr(nodeName, keyable=True)
    
    if isShapeNode == True:
        fixList(attrWorkList, nodeName)
    
    for item in attrWorkList:
        attrList[item] = cmds.getAttr(nodeName + "." + item)
          
    return attrList   
    
    
#Fixes a script-breaking error    
def fixList(listName, nodeName):
    if "aiFilters" in listName:
        listName.remove("aiFilters")
               
    #add parameters specific to light types
    lightType = getLightTypeFromScene(nodeName)
    
    if lightType == "directionalLight":
        listName.append("aiExposure")
        listName.append("aiAngle")
    elif lightType == "areaLight":
        listName.append("aiExposure")
        listName.append("aiSpread")
        listName.append("aiRoundness")
        listName.append("aiSoftEdge")
    elif lightType in ["pointLight", "spotLight", "volumeLight"]:
        listName.append("aiExposure")
        listName.append("aiRadius")


def buildSceneLightData():
    # This loop builds a dictionary of attribute keys for a light, then appends
    # to a different dictionary under the light's transform node name (not shape)
    
    allAvailableLights = captureSceneLights()
    sceneLights = {}
    
    for light in allAvailableLights:
        
        lightAttr = {}
        shapeNode = light
        transNode = getParentNode(shapeNode)
        
        #create some organizational entries for easier access later
        lightAttr["lightType"] = getLightTypeFromScene(light)
        lightAttr["shape"] = {}
        lightAttr["transform"] = {}
        
        #start building entries for light into dictionary
        lightAttr["transform"] = getAttributes(transNode, False)
        lightAttr["transform"]["name"] = transNode
        
        lightAttr["shape"] = getAttributes(shapeNode, True)
        lightAttr["shape"]["name"] = shapeNode
    
        #append constructed dict to sceneLights dict
        sceneLights[transNode] = lightAttr
    
    #return the completed dictionary of all lights    
    return sceneLights
    
    
def exportJson(inputDictionary):
    exportName = cmds.fileDialog2(fileMode=0, fileFilter="JSON Files (*.json)")
    if exportName:
        with open(exportName[0], 'w') as jsonfile:
        json.dump(inputDictionary, jsonfile)
        
#make a list of the light names
def extractLightNames(inputDict):
    return inputDict.keys()
    

#extract stuff from a category of attributes in dictionary and return list
def extractDataAttrNames(inputDict, lightName, dataType):
    return inputDict[lightName][dataType].keys()
