import pygame

class Sound:

    def __init__(self):
        self.music = pygame.mixer_music.load("musique1.mp3")
        self.musique_voulume = pygame.mixer.music.set_volume(0.25)
        self.musique_play = pygame.mixer.music.play(loops-1)
        # mixer.music.play() ou self.music.play()
        self.boule_de_feu = pygame.mixer.Sound("hadouken.mp3")

