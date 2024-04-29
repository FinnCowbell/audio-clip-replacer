from ui.Window import Window
from ui.parts.ButtonRow import ButtonRow
from ui.parts.Button import Button
from getch import getch
from keyReader import keyReader

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
        self.state = 0
        self.manager = manager
        self.lines = [
            TextLine('Welcome to the main menu'),
            TextLine('Please select an option'),
            ButtonRow([
            Button('exit', self.exit, 'q'),
            Button('run', self.run, 'x')
            ])]

        
    def run(self):
        self.manager.navigate('run')
        
    def options(self):
        self.manager.navigate('options')
    
    def draw(self):
        super().draw()
        keyReader.wait()

    @property
    def navigationButton(self):
        return Button('Menu', self.back, 'm')
        