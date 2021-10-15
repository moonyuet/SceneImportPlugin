import sys

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def maya_main_window():

    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class FileManagementDialog(QtWidgets.QDialog):
    FILE_FILTERS = "Maya(*.ma *.mb);;Maya ASCII(*.ma);;Maya Binary(*mb);; All Files(*.*)"
    
    selected_filter = "Maya(*.ma *.mb)" 
    
    dig_instance = None
    
    @classmethod
    def show_dialog(cls):
        if not cls.dig_instance:
            cls.dig_instance = FileManagementDialog()
        
        if cls.dig_instance.isHidden():
            cls.dig_instance.show()
        else:
            cls.dig_insatnce.raise_()
            cls.dig_instance.activateWindow()
    
    def __init__(self, parent=maya_main_window()):
        super(FileManagementDialog, self).__init__(parent)

        self.setWindowTitle("Import/Reference File Tool")
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.imported_caption = QtWidgets.QLabel("Import Scene")

        self.reference_caption = QtWidgets.QLabel("Reference Scene")

        self.filepath_import = QtWidgets.QLineEdit()
        self.imported_filepath_btn = QtWidgets.QPushButton()
        self.imported_filepath_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        self.imported_filepath_btn.setToolTip("Select File")

        self.filepath_reference = QtWidgets.QLineEdit()
        self.ref_filepath_btn = QtWidgets.QPushButton()
        self.ref_filepath_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        self.ref_filepath_btn.setToolTip("Select File")

        self.help_caption = QtWidgets.QLabel()
        self.help_caption.setText('''<a href='https://github.com/moonyuet/SceneImportPlugin'>Help</a>''')
        self.help_caption.setOpenExternalLinks(True)

        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        imported_caption_layout = QtWidgets.QHBoxLayout()
        imported_caption_layout.addWidget(self.imported_caption)

        file_import_layout = QtWidgets.QHBoxLayout()
        file_import_layout.addWidget(self.filepath_import)
        file_import_layout.addWidget(self.imported_filepath_btn)

        ref_caption_layout = QtWidgets.QHBoxLayout()
        ref_caption_layout.addWidget(self.reference_caption)

        file_reference_layout = QtWidgets.QHBoxLayout()
        file_reference_layout.addWidget(self.filepath_reference)
        file_reference_layout.addWidget(self.ref_filepath_btn)
        
        help_layout = QtWidgets.QHBoxLayout()
        help_layout.addWidget(self.help_caption)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(imported_caption_layout)
        form_layout.addRow("File:",file_import_layout)
        form_layout.addRow(ref_caption_layout)
        form_layout.addRow("File:", file_reference_layout)
        form_layout.addRow(help_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.imported_filepath_btn.clicked.connect(self.show_file_imported_dialog)
        self.ref_filepath_btn.clicked.connect(self.show_file_ref_dialog)
        self.apply_btn.clicked.connect(self.load_file)
        self.close_btn.clicked.connect(self.close)

    def show_file_imported_dialog(self):
        import_filepath, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "", self.FILE_FILTERS, self.selected_filter)
        if import_filepath:
            self.filepath_import.setText(import_filepath)
    
    def show_file_ref_dialog(self):
        ref_filepath, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", "", self.FILE_FILTERS, self.selected_filter)
        if ref_filepath:
            self.filepath_reference.setText(ref_filepath)
    
    def load_file(self):
        import_filepath = self.filepath_import.text()
        ref_filepath = self.filepath_reference.text()
        if import_filepath == "" and ref_filepath == "":
            return
        imported_file_info = QtCore.QFileInfo(import_filepath)
        ref_file_info = QtCore.QFileInfo(ref_filepath)
        if not imported_file_info.exists() and not ref_file_info.exists():
            om.MGlobal.displayError("File does not exist: {0} {1}.format(import_filepath, ref_filepath)")
        if imported_file_info.exists():
            self.import_file(import_filepath)
        elif ref_file_info.exists():
            self.reference_file(ref_filepath)
    
    def import_file(self, file_path):
        cmds.file(file_path, i = True, ignoreVersion = True)
    def reference_file(self, file_path):
        cmds.file(file_path, reference = True, ignoreVersion = True)

if __name__ == "__main__":
    try:
        file_management_dialog.close()
        file_management_dialog.deleteLater()
    except:
        pass

    file_management_dialog = FileManagementDialog()
    file_management_dialog.show()

