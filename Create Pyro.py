color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))

plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

pos = plane.selectPosition()

node = plane.currentNode()

try:
    dopNode = node.createNode("dopnet")
    boxNode = dopNode.createInputNode(0,"box")
except:
    temNode = node.parent()
    dopNode = temNode.createNode("dopnet")
    boxNode = dopNode.createInputNode(0,"box")
   
dopNode.setPosition(pos)
dopNode.setColor(color2)

try:
    dopNode.setName("dopNode_pyro")
except:
    pass
    
for node in dopNode.children():
    if node.name() == "output":
        pyroNode = node.createInputNode(0,"pyrosolver")
        sobjNode = pyroNode.createInputNode(0,"smokeobject")
        reSizeNode = pyroNode.createInputNode(1,"gasresizefluiddynamic")
        svNode = pyroNode.createInputNode(4,"sourcevolume")
        
