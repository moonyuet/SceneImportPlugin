import sys
import maya.cmds as cmds
import mtoa.utils as utils

path = r"C:\Users\Kayla\Desktop\scene_import_dialog\Maya"
sys.path.append(path)
scene_path = [""]


        
def scene_import_UI():
    if cmds.window("ImportSceneUI", exists = True):
        cmds.deleteUI("ImportSceneUI")
    window = cmds.window("ImportSceneUI",title= "Import Scene UI", widthHeight = (150,200))
    cmds.columnLayout(adjustableColumn=True, width = 200)
    cmds.button(label= "Select File", width= 40, 
    command = ("scene_import()"))
    cmds.separator()
    cmds.columnLayout(adjustableColumn=True)
    cmds.radioCollection()
    open_button = cmds.radioButton( label='Open', sl =True)
    import_button = cmds.radioButton( label='Import' )
    reference_button = cmds.radioButton( label='Reference' )
    cmds.separator()
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowColumnLayout( numberOfColumns=2, columnSpacing = [(2,5)], columnWidth=[(1, 100), (2, 100)] )
    cmds.button(label = "Apply", command = lambda x:apply(open_button, import_button, reference_button), width = 80)
    cmds.button(label = "Close",command = "close()",  width = 80)  
    cmds.showWindow(window)
def close():
   cmds.deleteUI("ImportSceneUI")
    
def scene_import():

    file_path = cmds.fileDialog(m = 0, dm="*.ma;*.mb")
    scene_path.append(file_path)
    if len(scene_path) > 0:
        scene_path.pop(0)
    print(scene_path[0])
    
def apply(open_button, import_button, reference_button):
    if cmds.radioButton(open_button, query = True, select = True):
        cmds.file(scene_path, open = True, ignoreVersion = True, force = True)
        print("Finish opening scene")
    elif cmds.radioButton(import_button, query = True, select = True):
        cmds.file(scene_path, i = True, ignoreVersion = True)
        print("Finish importing scene")
    elif cmds.radioButton(reference_button, query = True, select = True):
        cmds.file(scene_path, reference = True, ignoreVersion = True)
        print("Finish referencing scene")
if __name__ == "__main__":
    scene_import_UI()
    
    