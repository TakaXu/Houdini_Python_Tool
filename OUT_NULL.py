selectNodes = list(hou.selectedNodes())
path = []

def outNodePath(node):
    nodePath = node.path()
    path.append(nodePath)
    fl.write(nodePath)
    fl.write("\n")

fl = open("outNodePath.txt","w")

for selectNode in selectNodes:
    outNodePath(selectNode)
                  
fl.close()    
