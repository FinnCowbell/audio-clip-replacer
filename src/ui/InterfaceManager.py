
class InterfaceManager: 
    def __init__(self):
        self._windowClasses = {}
        self._windows = {}
        self._navigateCalled = False
        self._navigateCalled = False
    
    def addWindowClass(self, windowName, windowClass):
        curr = self._windowClasses.get(windowName)
        if curr is not None and curr is not windowClass:
            raise ValueError(f'Window {windowName} already exists')
        self._windowClasses[windowName] = windowClass
        
    def navigate(self, windowName):
        if not self._navigateCalled:
            if windowName not in self._windows:
                self._windows[windowName] = self._windowClasses[windowName](self)
            self._currentWindow = self._windows[windowName]
            self.render()
    
    def render(self):
        while True:
            self._navigateCalled = False
            self._currentWindow.render(self)
        
    def getCurrentWindow(self):
        return self._currentWindow
    
    def getWindow(self, windowName):
        try:
            return self._windowFunctions[windowName]
        except KeyError:
            raise KeyError(f'Window {windowName} not found')
        