from .PlayWindow import PlayWindow
from .Window import Window
from .parts.ButtonLine import ButtonLine
from .parts.TextLine import TextLine
from .parts.Button import Button
from keyReader import keyReader
from const import WINDOW

class MenuWindow (Window):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.name = WINDOW.MAINWINDOW
        self.state = 0
        self.manager = manager
        manager.addWindowClass(WINDOW.PLAYWINDOW, PlayWindow)
    
    @property
    def lines(self):
        return [
            TextLine('Welcome to the main menu'),
            TextLine('Please select an option'),
            ButtonLine([
            Button('exit', self.exit, 'q'),
            Button('run', self.run, 'x')
            ])]
        
    def run(self):
        self.manager.navigate(WINDOW.PLAYWINDOW)
        
    def options(self):
        self.manager.navigate('options')
    
    def draw(self):
        super().draw()
        
    def listen(self):
        keyReader.wait()
        
    def process(self):
        for line in self.lines:
            line.process()

    @property
    def navigationButton(self):
        return Button('Menu', self.back, 'm')
        