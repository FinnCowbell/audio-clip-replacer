
from ui.Window import Window
from ui.parts.Button import Button
from ui.parts.ButtonRow import ButtonRow
from keyReader import keyReader

class RunWindow (Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.lines = [ButtonRow([
            Button('exit', self.exit, 'q'),
            Button('menu', lambda: self.manager.navigate('default'), 'm')
        ])]
    def draw(self):
        super().draw()
        keyReader.wait()