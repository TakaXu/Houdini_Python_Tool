selectNodes = list(hou.selectedNodes())

grplist = list()
grpnames = list()


def primGroupNames(geometry):
    groupnames = geometry.primGroups()
    for grp in groupnames:
        grplist.append(grp.name())
        grp_names = grplist[-1]
        grpnames.append(grp_names)
        print grpnames
    return grpnames
        
for selectNode in selectNodes:
    primGroupNames(selectNode.geometry())
    for grpname in grpnames:
        blastNode = selectNode.createOutputNode("blast")
        blastNode.parm("group").set(grpname)
        blastNode.parm("negate").set(1)
        blastNode.setName(grpname)
