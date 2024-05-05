import os

class Window: 
    def __init__(self, manager) -> None:
        self.name = 'DEFAULT_NAME'
        self.manager = manager
        
    @property
    def lines(self):
        return []
    
    @property
    def width(self):
        return os.get_terminal_size().columns
    
    @property
    def height(self):
        return os.get_terminal_size().lines
    
    def clear(self):
        os.system('cls')
        
    def exit(self):
        raise SystemExit
        
    def render(self, manager):
        while(manager.getCurrentWindow() == self):
            self.clear()
            self.draw()
            self.listen()
            self.process()
    
    def draw(self):
        for line in range(max(0,self.height - len(self.lines))):
            print()
        for line in range(min(len(self.lines), self.height)):
            self.lines[line].draw()
    
    def process(self):
        raise NotImplementedError
            
    def listen(self):
        raise NotImplementedError
    
    @property
    def navigationButton(self):
        return None #virtual