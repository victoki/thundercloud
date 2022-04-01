#Thundercloud light importer

import maya.cmds as cmds
import json
import math

#get json data and unpack into a dictionary
filePath = "D:\\"
fileName = "tcLightData"                    
lightData = { }

with open(filePath + fileName + ".json") as json_file:
    lightData = json.load(json_file)
    
#TODO: Validate data in the json file for stuff that won't work, because you can edit json files outside Maya
for item in lightData:
    #Transform node name = Shape node name in json - add "shape Node" to end
    if lightData[item]["transNodeName"] == lightData[item]["shapeNodeName"]:
        lightData[item]["shapeNodeName"] == lightData[item]["transNodeName"] + "ShapeNode"
    
    #invalid light type
    

#Use validated lightData dictionary to recreate the lights imported in json in current scene
for lightObject in lightData:
    
    #first, I need the unique name of the item and what type of light to make it
    transNodeName = lightData[lightObject]["transNodeName"]
    lightType = lightData[lightObject]["lightType"]
    attrWorkList = { }
    
    #create the light
    if lightType == "ambientLight":
        cmds.ambientLight(name=transNodeName)
    elif lightType == "directionalLight":
        cmds.directionalLight(name=transNodeName) 
    elif lightType == "pointLight":
        cmds.pointLight(name=transNodeName)
    elif lightType == "spotLight":
        cmds.spotLight(name=transNodeName)
    elif lightType == "areaLight":
        cmds.CreateAreaLight(name=transNodeName)
    elif lightType == "volumeLight":
        cmds.CreateVolumeLight(name=transNodeName)
    
    #start assigning transform node values
    attrWorkList = cmds.listAttr(transNodeName, keyable=True)
    
    for item in attrWorkList:
        lightAttr[item] = cmds.setAttr(transNodeName + "." + item, lightData[lightObject][item])
        
    attrWorkList.clear()
    
    #start assigning data to shape node
    getChildShape = cmds.listRelatives(transNodeName, shapes=True)
    childShape = getChildShape[0]
    attrWorkList = cmds.listAttr(childShape, keyable=True)
    
    #if aiFilters is in the list, it produces an error - remove it.
    if "aiFilters" in attrWorkList:
        attrWorkList.remove("aiFilters")
        
    #accounting for differences in light settings
    if lightType == "directionalLight":
        attrWorkList.append("aiExposure")
        attrWorkList.append("aiAngle")
    elif lightType == "areaLight":
        attrWorkList.append("aiExposure")
        attrWorkList.append("aiSpread")
        attrWorkList.append("aiRoundness")
        attrWorkList.append("aiSoftEdge")
    elif lightType in ["pointLight", "spotLight", "volumeLight"]:
        attrWorkList.append("aiExposure")
        attrWorkList.append("aiRadius")
    
    for item in attrWorkList:
        lightAttr[item] = cmds.setAttr(childShape + "." + item, lightData[lightObject][item])
    
    attrWorkList.clear()
    
    
print("Lights have been set up.")