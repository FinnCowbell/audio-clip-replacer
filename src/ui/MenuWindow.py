from .PlayWindow import PlayWindow
from .Window import Window
from .parts.ButtonRow import ButtonRow
from .parts.Button import Button
from keyReader import keyReader
from const import WINDOW


class TextLine: 
    def __init__(self, text):
        self.text = text
        
    def draw(self):
        print(self.text)
        
    def process(self):
        pass

class MenuWindow (Window):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.name = WINDOW.MAINWINDOW
        self.state = 0
        self.manager = manager
        manager.addWindowClass(WINDOW.PLAYWINDOW, PlayWindow)
        self.lines = [
            TextLine('Welcome to the main menu'),
            TextLine('Please select an option'),
            ButtonRow([
            Button('exit', self.exit, 'q'),
            Button('run', self.run, 'x')
            ])]

        
    def run(self):
        self.manager.navigate(WINDOW.PLAYWINDOW)
        
    def options(self):
        self.manager.navigate('options')
    
    def draw(self):
        super().draw()
        keyReader.wait()

    @property
    def navigationButton(self):
        return Button('Menu', self.back, 'm')
        