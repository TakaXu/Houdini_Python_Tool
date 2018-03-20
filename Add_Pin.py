color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))

def input_Name():
    inputName = hou.ui.readInput("constraint_pin_name",buttons = ["OK","Cancle"])[1]
    return inputName

selectNode = list(hou.selectedNodes())[0]

pinNode = selectNode.createOutputNode("connectadjacentpieces")

pinNode.parm("connecttype").set(0)

attWrangle = pinNode.createOutputNode("attribwrangle")
attWrangle.parm("class").set(1)
attWrangle.parm("snippet").set("s@constraint_name = 'pin';\ns@constraint_type = 'all';")

cacheNode = attWrangle.createOutputNode("catche_tool_1.0.1")
cacheNode.setColor(color1)

nullNode = cacheNode.createOutputNode("null")

nullNode.setName("OUT_Pin_"+input_Name())

nullNode.setColor(color3)