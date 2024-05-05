import pygame
from pygame.locals import *

class AudioPlayer:
    endEvent = USEREVENT + 1
    def __init__(self, files):
        if(not pygame.get_init()):
            pygame.init()
        if(not pygame.mixer.get_init()):
            pygame.mixer.init()
        self.files = files
        self.currentIndex = 0
        self.paused = True
        self.channel = pygame.mixer.Channel(0)
        self.sound = pygame.mixer.Sound(self.files[self.currentIndex])

    def isPlaying(self):
        if self.paused:
            return False
        # Sound is playing: check if the sound has finished playing
        if pygame.event.peek(AudioPlayer.endEvent):
            self.paused = True
            return False
            
        return True
    
    def play(self):
        self.paused = False
        AudioPlayer.endEvent += 1
        self.channel.set_endevent(AudioPlayer.endEvent)
        self.channel.play(self.sound)
        
    def pause(self):
        self.paused = True
        self.channel.stop()
    
    @property
    def duration (self):
        if self.paused:
            return 0
        return self.sound.get_length()
        

if __name__ == "__main__":
    pygame.init()
    
    files = ['./src/Input/vox_plr_0_1st_staff_found_d_0.SN40.pc.snd.flac']
    player = AudioPlayer(files)
    player.sound.set_volume(0.5)
    player.play()
    print(player.duration)
    while player.isPlaying():
        continue
    player.play()
    while player.isPlaying():
        continue