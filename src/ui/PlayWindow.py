
from ui.Window import Window
from ui.parts.Button import Button
from ui.parts.ButtonRow import ButtonRow
from keyReader import keyReader
from ui.consts import window_names

class PlayWindow (Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.name = window_names['PlayWindow']
        self.lines = [ButtonRow([
            Button('exit', self.exit, 'q'),
            Button('menu', lambda: self.manager.navigate(window_names['MenuWindow']), 'm')
        ])]
    def draw(self):
        super().draw()
        keyReader.wait()