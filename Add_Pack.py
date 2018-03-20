color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))

def input_Name():
    inputName = hou.ui.readInput("pack_name",buttons = ["OK","Cancle"])[1]
    return inputName

selectNode = list(hou.selectedNodes())[0]

assNode = selectNode.createOutputNode("assemble")

assNode.parm("pack_geo").set(1)

assNode.parm("outside_group").set(input_Name())

nullNode = assNode.createOutputNode("null")

nullNode.setName("OUT_Pack")

nullNode.setColor(color3)
