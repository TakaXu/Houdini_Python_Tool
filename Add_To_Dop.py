selNodes = list(hou.selectedNodes())

def checkPrmType(node):
    geo = node.geometry()
    pr = geo.prims()[0]
    typeName = pr.type().name()
    
    if typeName == "Polygon":
        constraintName = pr.attribValue("constraint_name")
        if constraintName == "glue":
            return 1
        else:
            return 2
    else: 
        if typeName == "PackedFragment":
            return 0

def addrbd(node,selNode):
    path = "../../" + selNode.name()
    rbdpackobjectNode = node.createInputNode(100,"rbdpackedobject")
    rbdpackobjectNode.parm("soppath").set(path)
    
def addglue(node,selNode):
    path = "../../" + selNode.name()
    inputNode = node.inputs()[0]
    constraintNode = node.createInputNode(0,"constraintnetwork")
    constraintNode.setInput(0,inputNode,0)
    glueNode = constraintNode.createInputNode(1,"glueconrel")
    glueNode.parm("dataname").set("glue")
    constraintNode.parm("soppath").set(path)
    
def addpin(node,selNode):
    path = "../../" + selNode.name()
    inputNode = node.inputs()[0]
    constraintNode = node.createInputNode(0,"constraintnetwork")
    constraintNode.setInput(0,inputNode,0)
    pinNode = constraintNode.createInputNode(1,"hardconrel")
    pinNode.parm("dataname").set("pin")
    constraintNode.parm("soppath").set(path)
    
for selNode in selNodes:       
    for dopNode in selNodes[0].parent().children():
        if dopNode.name() == "dopNode_rbd":
            for node in dopNode.children():
                if node.name() == "output" and checkPrmType(selNode) == 1:
                    addglue(node,selNode)
                if node.name() == "output" and checkPrmType(selNode) == 2:
                    addpin(node,selNode)
                if node.name() == "merge_rbd" and checkPrmType(selNode) == 0:
                    addrbd(node,selNode)
