import os
from const import WINDOW
from audio.AudioPlayer import AudioPlayer
from .Window import Window
from .parts.Button import Button
from .parts.ButtonLine import ButtonLine
from .parts.TextLine import TextLine
from keyReader import keyReader

# Given a path, return a list of all the files in that path
def getFilePaths(path):
    return [path+f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    

class PlayWindow (Window):
    def __init__(self, manager):
        super().__init__(manager)
        self.filePaths = getFilePaths('../Input/')
        self.player = AudioPlayer(self.filePaths)
        self.name = WINDOW.PLAYWINDOW
    
    @property
    def lines(self):
        return [
            TextLine(f'Current file: {self.filePaths[self.player.currentIndex]}'),
            TextLine(f'Up Next: {self.filePaths[self.player.currentIndex + 1]}'),
            ButtonLine([
            Button('exit', self.exit, 'q'),
            self.audioButton(),
            Button('menu', lambda: self.manager.navigate(WINDOW.MAINWINDOW), 'm')
        ])]
        
    def draw(self):
        super().draw()
        
    def listen(self):
        keyReader.wait()
        
    def process(self):
        for line in self.lines:
            line.process()
    
    def audioButton(self):
        return Button('replay', self.player.play, ' ')