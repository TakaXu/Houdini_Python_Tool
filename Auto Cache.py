color = hou.Color()
color.setRGB((0.9,0,0))

def catche(node):
    selectNode.parm("execute").pressButton()
    selectNode.parm("reload").pressButton()
    selectNode.setColor(color)

def cache(node):
    selectNode.parm("execute").pressButton()
    selectNode.parm("loadfromdisk").set(1)
    selectNode.parm("reload").pressButton()
    selectNode.setRenderFlag(1)
    selectNode.setDisplayFlag(1)

def rop(node):
    selectNode.parm("execute").pressButton()
    
selectNodes = list(hou.selectedNodes())

for selectNode in selectNodes:
    name = selectNode.type().name()
    print name
    if name == "catche_tool_1.0.1":
        catche(selectNode)
    if name == "filecache":
        cache(selectNode)
    if name == "rop_geometry":
        rop(selectNode)
