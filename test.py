from qgis.core import QgsProject
project_path = QgsProject.instance().readPath("./")
root = QgsProject.instance().layerTreeRoot()
# les groupes dans le projet
g_projet = ['Reseau', 'Fond-Plan', 'Impression']
sg_reseau = ['RSX', 'TIF', 'BUF']
# create a groupe if it's not exist
# converte Liste groupe to array

def childrenToArray(chl):
    for item in chl.children():
        out.append(item.name())
    return out

for g_i in g_projet:
    if g_i not in childrenToArray(root):
        root.addGroup(g_i)
    
    

        
        

    

        

    

    
    
    


