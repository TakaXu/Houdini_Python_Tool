plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

pos = plane.selectPosition()

currentNode = plane.currentNode()

fl = open("www.txt","r")

lineList = fl.readlines()
numLine = len(lineList)

fl.close()

for oneLine in range(numLine):
    pos[0] += 1
    try:
        objMergeNode = currentNode.createNode("object_merge")
    except:
        a = currentNode.parent()
        objMergeNode = a.createNode("object_merge")
        
    objMergeNode.setPosition(pos)
    objMergeNode.parm("objpath1").set(lineList[oneLine][0:-1])