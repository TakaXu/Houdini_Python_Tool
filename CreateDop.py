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
except:
    temNode = node.parent()
    dopNode = temNode.createNode("dopnet")
   
dopNode.setPosition(pos)
dopNode.setColor(color2)

try:
    dopNode.setName("dopNode_rbd")
except:
    pass
    
for node in dopNode.children():
    if node.name() == "output":
        graNode = node.createInputNode(0,"gravity")
        bltSolverNode = graNode.createInputNode(0,"bulletrbdsolver")
        mergeNode = bltSolverNode.createInputNode(0,"merge")
        mergeNode.setName("merge_rbd")