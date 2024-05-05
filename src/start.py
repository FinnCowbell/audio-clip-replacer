import os
from ui.MenuWindow import MenuWindow
from ui.InterfaceManager import InterfaceManager
from ui.PlayWindow import PlayWindow
from const import WINDOW

DEFAULT_DIR = "../Input/"
DEFAULT_OUTPUT_DIR = "../Output/"

class AudioClipReplacer:
    def __init__(self):
        self.initDirectories()
        self._interfaceManager = InterfaceManager()
        self.initWindows()
    
    def initDirectories(self): 
        if not os.path.exists(DEFAULT_DIR):
            os.makedirs(DEFAULT_DIR)
        if not os.path.exists(DEFAULT_OUTPUT_DIR):
            os.makedirs(DEFAULT_OUTPUT_DIR)
            
    def initWindows(self): 
        self._interfaceManager.addWindowClass(WINDOW.MAINWINDOW, MenuWindow)
        self._interfaceManager.addWindowClass(WINDOW.PLAYWINDOW, PlayWindow)

    def run(self):
        self._interfaceManager.navigate(WINDOW.MAINWINDOW)
        self._interfaceManager.render()
        
if __name__ == "__main__":
    app = AudioClipReplacer()
    app.run()