from const import WINDOW
from .Window import Window
from .parts.Button import Button
from .parts.ButtonRow import ButtonRow
from keyReader import keyReader

class PlayWindow (Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.name = WINDOW.PLAYWINDOW
        self.lines = [ButtonRow([
            Button('exit', self.exit, 'q'),
            Button('menu', lambda: self.manager.navigate(WINDOW.MAINWINDOW), 'm')
        ])]
    def draw(self):
        super().draw()
        keyReader.wait()