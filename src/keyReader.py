from getch import getch

class _KeyReader:
    def __init__(self):
        self.currentKey = None
        
    def wait(self):
        self.currentKey = getch().decode('utf-8')
        return
    
    @property
    def key(self):
        return self.currentKey
    
keyReader = _KeyReader()