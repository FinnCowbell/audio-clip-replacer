import os
from ui.MenuWindow import MenuWindow
from ui.InterfaceManager import InterfaceManager
from ui.RunWindow import RunWindow

DEFAULT_DIR = "./Input/"
DEFAULT_OUTPUT_DIR = "./Output/"

class AudioRecorder:
    def __init__(self):
        self.initDirectories()
        windows = self.initWindows()
        self._interfaceManager = InterfaceManager(windows)
    
    def initDirectories(self): 
        if not os.path.exists(DEFAULT_DIR):
            os.makedirs(DEFAULT_DIR)
        if not os.path.exists(DEFAULT_OUTPUT_DIR):
            os.makedirs(DEFAULT_OUTPUT_DIR)
            
    def initWindows(self): 
        return {
            "default": MenuWindow,
            "run": RunWindow
        }

    def run(self):
        self._interfaceManager.render()
        
if __name__ == "__main__":
    app = AudioRecorder()
    app.run()