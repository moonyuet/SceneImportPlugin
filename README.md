# SceneImportPlugin
Sample scripts for importing(and referencing) scenes in Maya/Blender
# Maya
I have wrote two scripts with Maya UI and PySide2 respectively.
1. Maya UI

![alt text](https://raw.githubusercontent.com/moonyuet/SceneImportPlugin/main/scene_import_dialog/screenshot/maya_screenshot_1.jpg)

Users can choose either open, import or reference their scenes after selecting the ma/mb files.
2. PySide2

![alt text](https://raw.githubusercontent.com/moonyuet/SceneImportPlugin/main/scene_import_dialog/screenshot/maya_screenshot_2.jpg)

Unlike Maya UI, users can only import or reference scenes after selecting the ma/mb files.
# Blender

![alt text](https://raw.githubusercontent.com/moonyuet/SceneImportPlugin/main/scene_import_dialog/screenshot/blender_screenshot.jpg)

The Blender Plugin is a bit different from Maya. Instead of including referencing/opening scene feature, I added some feature such as importing obj files and importing blend files. There are two options for importing blend files. One for camera (with the fixed square resolution setup in the script) and other for just purely importing blender scene. 

1. Delete Template Scene : Delete the starter scene in Blender
2. Fix Scene Size: To fix the size of the geometry imported from some software (such as VStitcher.), knowing that metric of blender is metre.
3. Import Asset: import obj file by file dialog
4. Import Camera Scene : Import blend file by file dialog. This would set up the fixed 2k square resolutions and render in cycle engine for you.
5. Import Scene: Import blend file by file dialog
