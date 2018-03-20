color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))

selectNodes = list(hou.selectedNodes())

for selectNode in selectNodes:
    posx = selectNode.position()[0]
    posy = selectNode.position()[1]
    
    vorNode = selectNode.createOutputNode('voronoifracture')
    vorNode.setPosition([posx,posy-3])
    
    isoNode = selectNode.createOutputNode('isooffset')
    isoNode.parm("samplediv").set(100)
    isoNode.setPosition([posx+1,posy-1])
    
    scNode = isoNode.createOutputNode('scatter')
    scNode.parm("npts").set(100)
    scNode.parm("useemergencylimit").set(0)
    scNode.parm("randomizeorder").set(0)
    
    vorNode.setInput(1,scNode,0)
    
    cacheNode = vorNode.createOutputNode('catche_tool_1.0.1')
    cacheNode.setColor(color1)
    cacheButton = cacheNode.parm("execute")
    reloadButton = cacheNode.parm("reload")
#    cacheButton.pressButton()
#    reloadButton.pressButton()
    
    nullNode = cacheNode.createOutputNode("null")
    nullNode.setDisplayFlag(1)
    nullNode.setRenderFlag(1)
    