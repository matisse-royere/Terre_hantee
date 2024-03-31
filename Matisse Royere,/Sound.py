import pygame
"""
class SoundManager:

    def __init__(self):
        self.sounds = {
            'Hadouken' : pygame.mixer.Sound("Hadouken.wav"),
            'Feu' : pygame.mixer.Sound("Boule_de_feu.wav"),

        }

    def play(self,name):
        self.sounds[name].play()




#'Hadouken' : pygame.mixer.Sound("nsi jeux video/Hadouken.wav"),
"""




"""
    def __init__(self):
        self.music = pygame.mixer_music.load("musique1.mp3")
        self.musique_voulume = pygame.mixer.music.set_volume(0.25)
        self.musique_play = pygame.mixer.music.play(loops-1)
        # mixer.music.play() ou self.music.play()
        self.boule_de_feu = pygame.mixer.Sound("hadouken.mp3")
"""
pygame.init()

class SoundManager:

    def __init__(self):
        self.sounds = {
            'Hadouken' : pygame.mixer.Sound("Hadouken.wav"),
            'Feu' : pygame.mixer.Sound("Boule_de_feu.wav"),

        }

    def play(self,name):
        self.sounds[name].play()



#crée une fenê tre de la taille demand ée
ecran = pygame . display . set_mode ((600 ,400) )

# boucle principale
continuer = True
while continuer :
    # gestion des évé nements
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            SoundManager("hadouken.wav")
            SoundManager.play()
 #Le joueur a ferm é la fenêtre
            continuer = False

pygame . quit ()