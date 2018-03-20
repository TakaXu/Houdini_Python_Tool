fbxNodes = list(hou.selectedNodes())
path = []

def serach_node(node):
    if node.children():
        for childrenNode in node.children():
            if childrenNode.type().name() == 'file' or childrenNode.type().name() == 'alembic':
                nodePath =  childrenNode.path()
                path.append(nodePath)
            else:
                serach_node(childrenNode)
                
fl = open("www.txt","w")              
                
for fbxNode in fbxNodes:
    serach_node(fbxNode)
    nodePaths = path
    
    for nodePath in nodePaths:
        fl.write(nodePath)
        fl.write("\n")
        
fl.close()