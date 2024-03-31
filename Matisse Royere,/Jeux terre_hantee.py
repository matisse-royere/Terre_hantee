#bien venue dans le code de terre hantee
    #lancer le programme si vous voulez jouer
import pygame
import random
import math




from pygame import mixer
from Sounds import Sound      # on importe la classe du son



pygame.init()
mixer.init()

mixer.music.load("musique1.mp3")
mixer.music.play()


##hadouken.mp3


ecran = pygame.display.set_mode((1880, 1000))


def afficher_menu(ecran, fond_menu): ##menue
    ecran.blit(fond_menu, (0, 0))  # Afficher l'image de fond

    font = pygame.font.Font(None, 36)

    bouton_foret = font.render("Choisir la prairie", True, (255, 255, 255))
    rect_foret = bouton_foret.get_rect(topleft=(500, 550))
    ecran.blit(bouton_foret, rect_foret.topleft)

    bouton_cave = font.render("Choisir la grotte de lave", True, (255, 255, 255))
    rect_cave = bouton_cave.get_rect(topleft=(500, 600))
    ecran.blit(bouton_cave, rect_cave.topleft)

    bouton_quitter = font.render("Quitter", True, (255, 255, 255))
    rect_quitter = bouton_quitter.get_rect(topleft=(500, 650))
    ecran.blit(bouton_quitter, rect_quitter.topleft)

    pygame.draw.rect(ecran, (255, 255, 255), rect_foret, 2)
    pygame.draw.rect(ecran, (255, 255, 255), rect_cave, 2)
    pygame.draw.rect(ecran, (255, 255, 255), rect_quitter, 2)

fond_menu = pygame.image.load("terre_hantee.jpg")
fond_menu = pygame.transform.scale(fond_menu, (1880, 1000))

en_menu = True
choix_carte = None

while en_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_menu = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            en_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 500 <= x <= 700 and 550 <= y <= 575:
                choix_carte = "Mapsforet1.png"
                en_menu = False
            elif 500 <= x <= 800 and 600 <= y <= 625:
                choix_carte = "Mapslave2.png"
                en_menu = False
            elif 500 <= x <= 600 and 650 <= y <= 675:
                pygame.quit()
                exit()

    ecran.fill((0, 0, 0))
    afficher_menu(ecran, fond_menu)
    pygame.display.flip()

# Initialisation du jeu
pygame.init()
ecran = pygame.display.set_mode((1880, 1000))  #1920, 1080

if choix_carte:
    paysage = pygame.image.load(choix_carte)
    paysage = pygame.transform.scale(paysage, (1880, 1000))




    class Attaque1:
        def __init__(self, x, y, direction, degats, images):
            self.x = x
            self.y = y

            sound = Sound("hadouken.wav") #implément un son en .wav
            sound.play() # le jouer
            self.direction = direction
            self.degats = degats
            self.images = images
            self.image_index = 0
            self.current_image = self.images[self.image_index]
            self.lifetime = 50                            ## distance de l'image des dégat


        def update(self):
            if self.direction == 'right':
                self.x += 5
            elif self.direction == 'left':
                self.x -= 5
            elif self.direction == 'up':
                self.y -= 5
            elif self.direction == 'down':
                self.y += 5

            self.image_index = (self.image_index + 1) % len(self.images)
            self.current_image = self.images[self.image_index]


            self.lifetime -= 1

        def is_alive(self):
            return self.lifetime > 0

        def render(self, ecran):
            ecran.blit(self.current_image, (self.x, self.y))


    class Attaque_2:
        def __init__(self, x, y, direction, degats, images):
            self.x = x
            self.y = y

            #sound = Sound("feu.wav") #implément un son en .wav
            #sound.play() # le jouer
            self.direction = direction
            self.degats = degats
            self.images = images
            self.image_index = 0
            self.current_image = self.images[self.image_index]
            self.lifetime = 30                            ## distance de l'image des dégat


        def update(self):
            if self.direction == 'right':
                self.x += 5
            elif self.direction == 'left':
                self.x -= 5
            elif self.direction == 'up':
                self.y -= 5
            elif self.direction == 'down':
                self.y += 5

            self.image_index = (self.image_index + 1) % len(self.images)
            self.current_image = self.images[self.image_index]


            self.lifetime -= 1

        def is_alive(self):
            return self.lifetime > 0

        def render(self, ecran):
            ecran.blit(self.current_image, (self.x, self.y))


    class Attaque_2SP:         #pour l'attaque spéciale
        def __init__(self, x, y, direction, degats, images):
            self.x = x
            self.y = y

            #sound = Sound("feu.wav") #implément un son en .wav
            #sound.play() # le jouer
            self.direction = direction
            self.degats = degats
            self.images = images
            self.image_index = 0
            self.current_image = self.images[self.image_index]
            self.lifetime = 70                            ## distance de l'image des dégat


        def update(self):
            if self.direction == 'right':
                self.x += 5
            elif self.direction == 'left':
                self.x -= 5
            elif self.direction == 'up':
                self.y -= 5
            elif self.direction == 'down':
                self.y += 5

            self.image_index = (self.image_index + 1) % len(self.images)
            self.current_image = self.images[self.image_index]


            self.lifetime -= 1

        def is_alive(self):
            return self.lifetime > 0

        def render(self, ecran):
            ecran.blit(self.current_image, (self.x, self.y))




    ##import ennemi #####

    class Ennemi:
        def __init__(self, x, y, taille, points_de_vie, degats):
            self.x = x
            self.y = y
            self.vitesse = 2        ## vitesse
            self.taille = taille
            self.image1 = pygame.image.load("fantome.png")
            self.image2 = pygame.image.load("fantome.png")
            self.image3 = pygame.image.load("fantome.png")
            self.image4 = pygame.image.load("fantome.png")
            self.animation_timer = 0
            self.image_index = 0
            self.images = [self.image1, self.image2]
            self.image = pygame.transform.scale(self.images[self.image_index], (taille, taille))
            self.points_de_vie = points_de_vie
            self.degats = degats
            self.visible = True
            self.attack_cooldown = 60
            self.attack_timer = 0

        def attaquer_joueur(self, joueur):
            if self.attack_timer <= 0:
                distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
                if distance < self.taille:
                    joueur.subir_degats(self.degats)
                    self.attack_timer = self.attack_cooldown

        def update(self):
            if self.attack_timer > 0:
                self.attack_timer -= 1

        def render(self, ecran):
            if self.visible:
                ecran.blit(self.image, (self.x, self.y))
    class Ennemi2:
            def __init__(self, x, y, taille, points_de_vie, degats):
                self.x = x
                self.y = y
                self.vitesse = 0.5
                self.taille = taille
                self.image1 = pygame.image.load("fantome.png")
                self.image2 = pygame.image.load("fantome1.png")
                self.image3 = pygame.image.load("fantome3.png")
                self.image4 = pygame.image.load("fantome.png")
                self.animation_timer = 0
                self.image_index = 0
                self.images = [self.image1, self.image2]
                self.image = pygame.transform.scale(self.images[self.image_index], (taille, taille))
                self.points_de_vie = points_de_vie
                self.degats = degats
                self.visible = True
                self.attack_cooldown = 60
                self.attack_timer = 0

            def attaquer_joueur(self, joueur):
                if self.attack_timer <= 0:
                    distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
                    if distance < self.taille:
                        joueur.subir_degats(self.degats)
                        self.attack_timer = self.attack_cooldown

            def update(self):
                if self.attack_timer > 0:
                    self.attack_timer -= 1

            def render(self, ecran):
                if self.visible:
                    ecran.blit(self.image, (self.x, self.y))


    class EnnemiSlime(Ennemi):  #ennemi fantome
        def __init__(self, x, y):
            super().__init__(x, y, taille=40, points_de_vie=1, degats=15)
            self.image1 = pygame.image.load("fantome.png")
            self.image2 = pygame.image.load("fantome3.png")
            self.images = [self.image1, self.image2]

        def attaquer_joueur(self, joueur):
            distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
            if distance < self.taille:
                joueur.subir_degats(15)
                self.points_de_vie = 0

        def deplacer_vers_joueur(self, joueurs):
            closest_player = None
            min_distance = float('inf')

            for joueur in joueurs:
                if joueur.vie > 0:
                    distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
                    if distance < min_distance:
                        min_distance = distance
                        closest_player = joueur

            if closest_player:
                dx = closest_player.x - self.x
                dy = closest_player.y - self.y
                distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
                dx /= distance
                dy /= distance
                self.x += dx * self.vitesse
                self.y += dy * self.vitesse
                self.animation_timer += 1

                if self.animation_timer >= 40:
                    self.image_index = (self.image_index + 1) % len(self.images)
                    self.image = pygame.transform.scale(self.images[self.image_index], (self.taille, self.taille))
                    self.animation_timer = 0

        class EnnemiCsr(Ennemi):  # chauve-souris
            def __init__(self, x, y):
                super().__init__(x, y, taille=40, points_de_vie=1, degats=15)
                self.image1 = pygame.image.load("gauche2_chauve_souris.png")
                self.image2 = pygame.image.load("gauche2_chauve_souris.png")
                self.images = [self.image1, self.image2]

            def attaquer_joueur(self, joueur):
                distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
                if distance < self.taille:
                    joueur.subir_degats()
                    self.points_de_vie = 0

            def deplacer_vers_joueur(self, joueurs):
                closest_player = None
                min_distance = float('inf')

                for joueur in joueurs:
                    if joueur.vie > 0:
                        distance = math.sqrt((joueur.x - self.x) ** 2 + (joueur.y - self.y) ** 2)
                        if distance < min_distance:
                            min_distance = distance
                            closest_player = joueur

                if closest_player:
                    dx = closest_player.x - self.x
                    dy = closest_player.y - self.y
                    distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
                    dx /= distance
                    dy /= distance
                    self.x += dx * self.vitesse
                    self.y += dy * self.vitesse
                    self.animation_timer += 1

                    if self.animation_timer >= 40:
                        self.image_index = (self.image_index + 1) % len(self.images)
                        self.image = pygame.transform.scale(self.images[self.image_index], (self.taille, self.taille))
                        self.animation_timer = 0



    ######## J 1

    class Joueur:
        def __init__(self, x, y, touches, vie_max, vitesse, degats):
            self.x = x
            self.y = y
            self.vie = vie_max
            self.vie_max = vie_max
            self.vitesse = vitesse ## plus bas parametre de vitesse
            self.degats = degats
            self.images = {
                'up': [
                    pygame.transform.scale(pygame.image.load("perso 1 dos 2 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 dos 3 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 dos deplacement.png"), (80, 80)),
                ],
                'down': [
                    pygame.transform.scale(pygame.image.load("perso 1 face deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 face 2 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 face 3 deplacement.png"), (80, 80)),
                ],
                'left': [
                    pygame.transform.scale(pygame.image.load("perso 1 gauche 2 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 gauche 3 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 gauche deplacement.png"), (80, 80)),

                ],
                'right': [
                    pygame.transform.scale(pygame.image.load("perso 1 droite 2 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 droite 3 deplacement.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 1 droite deplacement.png"), (80, 80)),
                ]
            }
            self.direction = 'down'
            self.animation_index = 0
            self.en_deplacement = False
            self.touches = touches
            self.jouable = True
            self.hit_timer = 0
            self.hit_cooldown = 60

        def subir_degats(self, degats):
            if self.jouable:
                self.vie -= degats
                self.vie = min(max(0, self.vie), self.vie_max)

        def update(self):
            if self.hit_timer > 0:
                self.hit_timer -= 2
                if self.hit_timer % 20 < 10:
                    animation_list = self.images[self.direction]
                    self.animation_index = (self.animation_index + 1) % len(animation_list)
                    self.image = pygame.transform.scale(animation_list[self.animation_index], (80, 80))
                else:
                    self.image = pygame.transform.scale(self.images[self.direction][self.animation_index], (80, 80))
            else:
                animation_list = self.images[self.direction]
                self.animation_index = (self.animation_index + 1) % len(animation_list)
                self.image = pygame.transform.scale(animation_list[self.animation_index], (80, 80))

            keys = pygame.key.get_pressed()
            if keys[self.touches['droite']]:
                self.direction = 'right'
            elif keys[self.touches['gauche']]:
                self.direction = 'left'
            elif keys[self.touches['haut']]:
                self.direction = 'up'
            elif keys[self.touches['bas']]:
                self.direction = 'down'

        def render(self, ecran):
            ecran.blit(self.image, (self.x, self.y))
            barre_vie_longueur = self.vie / self.vie_max * 100
            pygame.draw.rect(ecran, (0, 128, 0), (self.x, self.y - 10, barre_vie_longueur, 10))

    ##### fin joueur 1

    #joueur 2 ###################

    class Joueur2:
        def __init__(self, x, y, touches, vie_max, vitesse, degats):
            self.x = x
            self.y = y
            self.vie = vie_max
            self.vie_max = vie_max
            self.vitesse = vitesse
            self.degats = degats
            self.images = {
                'up': [
                    pygame.transform.scale(pygame.image.load("perso 2 dos 2 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 dos 2 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 dos 3 marche.png"), (80, 80)),
                ],
                'down': [
                    pygame.transform.scale(pygame.image.load("perso 2 face marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 face 2 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 face 3 marche.png"), (80, 80)),
                ],
                'left': [
                    pygame.transform.scale(pygame.image.load("perso 2 gauche 2 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 gauche 3 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 gauche marche.png"), (80, 80)),

                ],
                'right': [
                    pygame.transform.scale(pygame.image.load("perso 2 droite 2 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 droite 3 marche.png"), (80, 80)),
                    pygame.transform.scale(pygame.image.load("perso 2 droite marche.png"), (80, 80)),
                ]
            }
            self.direction = 'down'
            self.animation_index = 0
            self.en_deplacement = False
            self.touches = touches
            self.jouable = True
            self.hit_timer = 0
            self.hit_cooldown = 60

        def subir_degats(self, degats):
            if self.jouable:
                self.vie -= degats
                self.vie = min(max(0, self.vie), self.vie_max)

        def update(self):           #barre de vie  debut
            if self.hit_timer > 0:
                self.hit_timer -= 2
                if self.hit_timer % 20 < 10:
                    animation_list = self.images[self.direction]
                    self.animation_index = (self.animation_index + 1) % len(animation_list)
                    self.image = pygame.transform.scale(animation_list[self.animation_index], (80, 80))
                else:
                    self.image = pygame.transform.scale(self.images[self.direction][self.animation_index], (80, 80))
            else:
                animation_list = self.images[self.direction]
                self.animation_index = (self.animation_index + 1) % len(animation_list)
                self.image = pygame.transform.scale(animation_list[self.animation_index], (80, 80))

            keys = pygame.key.get_pressed()
            if keys[self.touches['droite']]:
                self.direction = 'right'
            elif keys[self.touches['gauche']]:
                self.direction = 'left'
            elif keys[self.touches['haut']]:
                self.direction = 'up'
            elif keys[self.touches['bas']]:
                self.direction = 'down'

        def render(self, ecran):
            ecran.blit(self.image, (self.x, self.y))
            barre_vie_longueur = self.vie / self.vie_max * 100
            pygame.draw.rect(ecran, (0, 128, 0), (self.x, self.y - 10, barre_vie_longueur, 10))  #barre de vie fin


    #fin joueur 2 ###################################################


    class Paladin(Joueur):
        def __init__(self, x, y, touches):
            super().__init__(x, y, touches, vie_max=300, vitesse=2.5, degats=40)
            self.attaque_timer = 0
            self.attaque_cooldown = 30
            self.attaque_images = {
                'right': [pygame.image.load("explosion1.png"), pygame.image.load("explosion2.png"), pygame.image.load("explosion3.png"), pygame.image.load("explosion4.png"), pygame.image.load("explosion5.png")],
                'left': [pygame.image.load("explosion1.png"), pygame.image.load("explosion2.png"), pygame.image.load("explosion3.png"), pygame.image.load("explosion4.png"), pygame.image.load("explosion5.png")],
                'up': [pygame.image.load("explosion1.png"), pygame.image.load("explosion2.png"), pygame.image.load("explosion3.png"), pygame.image.load("explosion4.png"), pygame.image.load("explosion5.png")],
                'down': [pygame.image.load("explosion1.png"), pygame.image.load("explosion2.png"), pygame.image.load("explosion3.png"), pygame.image.load("explosion4.png"), pygame.image.load("explosion5.png")]
            }

        def attaquer(self, attaques):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e] and self.attaque_timer <= 0: # touche pour l'attaque et ...
                self.attaque_timer = self.attaque_cooldown
                attaque_direction = self.direction
                if attaque_direction in self.attaque_images:
                    attaque_images = self.attaque_images[attaque_direction]
                    attaque = Attaque1(self.x, self.y, attaque_direction, self.degats, attaque_images)
                    attaques.append(attaque)




        def update(self):
            super().update()
            if self.attaque_timer > 0:
                self.attaque_timer -= 1

        def render(self, ecran):
            super().render(ecran)

    ##"

    class Soigneuse(Joueur2): ##################################################
        def __init__(self, x, y, touches):
            super().__init__(x, y, touches, vie_max=125, vitesse=0, degats=40)
            self.attaque_timer = 0
            self.attaque_cooldown = 30
            self.soins_cooldown = 60
            self.soins_timer = 0
            self.attaque_images_2 = {
                'right': [pygame.image.load("sante1.png"), pygame.image.load("sante2.png"), pygame.image.load("sante3.png"), pygame.image.load("sante4.png"), pygame.image.load("sante5.png"),pygame.image.load("sante6.png"), pygame.image.load("sante7.png"), pygame.image.load("sante8.png"), pygame.image.load("sante9.png"), pygame.image.load("sante10.png")],
                'left': [pygame.image.load("sante1.png"), pygame.image.load("sante2.png"), pygame.image.load("sante3.png"), pygame.image.load("sante4.png"), pygame.image.load("sante5.png"),pygame.image.load("sante6.png"), pygame.image.load("sante7.png"), pygame.image.load("sante8.png"), pygame.image.load("sante9.png"), pygame.image.load("sante10.png")],
                'up': [pygame.image.load("sante1.png"), pygame.image.load("sante2.png"), pygame.image.load("sante3.png"), pygame.image.load("sante4.png"), pygame.image.load("sante5.png"),pygame.image.load("sante6.png"), pygame.image.load("sante7.png"), pygame.image.load("sante8.png"), pygame.image.load("sante9.png"), pygame.image.load("sante10.png")],
                'down': [pygame.image.load("sante1.png"), pygame.image.load("sante2.png"), pygame.image.load("sante3.png"), pygame.image.load("sante4.png"), pygame.image.load("sante5.png"),pygame.image.load("sante6.png"), pygame.image.load("sante7.png"), pygame.image.load("sante8.png"), pygame.image.load("sante9.png"), pygame.image.load("sante10.png")],
            }
        def soigner(self, joueur, joueurs):
            if self.soins_timer <= 0:
                if joueur.vie < joueur.vie_max:
                    joueur.vie += 60
                for j in joueurs:
                    if j.vie < j.vie_max:
                        j.vie += 60
                self.soins_timer = self.soins_cooldown

                # Ajoutez ces lignes pour l'animation lors du soin
                self.soins_animation(self.x, self.y)

        def soins_animation(self, x, y):
            # Images de l'animation de soin
            soins_images = [
                pygame.image.load("soins1.png"),
                pygame.image.load("soins2.png"),
                pygame.image.load("soins1.png"),
                pygame.image.load("soins2.png"),
                pygame.image.load("soins3.png"),
                pygame.image.load("soins4.png"),
                pygame.image.load("soins5.png"),
                pygame.image.load("soins6.png"),
                pygame.image.load("soins7.png"),
                pygame.image.load("soins8.png"),
                pygame.image.load("soins9.png"),
                pygame.image.load("soins9.png"),
                pygame.image.load("soins9.png"),
                pygame.image.load("soins1.png"),
                pygame.image.load("soins8.png"),
                pygame.image.load("soins9.png"),
                pygame.image.load("soins1.png"),
                pygame.image.load("soins1.png"),
            ]

            # Durée de chaque image de l'animation
            animation_duration = 30

            # Exécutez l'animation
            for img in soins_images:

                ecran.blit(img, (x-100, y-100)) # Affiche l'image de l'animation à la position (x, y) car elle était mal placer

                pygame.display.flip()
                pygame.time.delay(animation_duration)

        def attaquer(self, attaques):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.attaque_timer <= 0:      # Touche pour la premiere attaque
                self.attaque_timer = self.attaque_cooldown
                attaque_direction = self.direction
                if attaque_direction in self.attaque_images_2:
                    attaque_images_2 = self.attaque_images_2[attaque_direction]
                    attaque = Attaque_2(self.x, self.y, attaque_direction, self.degats, attaque_images_2)
                    attaques.append(attaque)
            elif keys[pygame.K_n]:   # Touche pour le soin
                        self.soigner(joueur1, joueurs)



        def update(self):
            super().update()
            if self.attaque_timer > 0:
                self.attaque_timer -= 1

        def render(self, ecran):
            super().render(ecran)



    joueur1 = Paladin(180, 540, {'droite': pygame.K_d, 'gauche': pygame.K_a, 'haut': pygame.K_w, 'bas': pygame.K_s})
    ###
    joueur2 = Soigneuse(580, 540, {'droite': pygame.K_RIGHT, 'gauche': pygame.K_LEFT, 'haut': pygame.K_UP, 'bas': pygame.K_DOWN})
    joueurs = [joueur1, joueur2]

    ennemis = []
    max_enemy_count = 6
    enemy_spawn_timer = 0

    def creer_ennemi():
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        taille = 40
        ennemis.append(EnnemiSlime(x, y))

    def creer_ennemi2():                    #pour crée la chauve-souris
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        taille = 40
        ennemis.append(EnnemiCsr(x, y))

    attaques = []

    en_cours = True
    horloge = pygame.time.Clock()

    font = pygame.font.Font(None, 100)
    perdu_text = None

    while en_cours:
        horloge.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False


        ecran.fill((0, 0, 0))
        ecran.blit(paysage, (0, 0))

        joueurs_jouables = 0

        for joueur in joueurs:
            if joueur.jouable:
                joueurs_jouables += 1
                touches = pygame.key.get_pressed()
                x, y, vitesse, animation_index, en_deplacement = joueur.x, joueur.y, 2, joueur.animation_index, joueur.en_deplacement
                touches_joueur = joueur.touches

                if touches[touches_joueur['droite']]:
                    x += vitesse +2                           ## vitesse perso
                    en_deplacement = True
                    joueur.direction = 'right'
                elif touches[touches_joueur['gauche']]:
                    x -= vitesse+2
                    en_deplacement = True
                    joueur.direction = 'left'
                elif touches[touches_joueur['haut']]:
                    y -= vitesse+2
                    en_deplacement = True
                    joueur.direction = 'up'
                elif touches[touches_joueur['bas']]:
                    y += vitesse+2
                    en_deplacement = True
                    joueur.direction = 'down'

                x = max(0, min(x, 1920 - 80))
                y = max(0, min(y, 1080 - 80))

                if en_deplacement:
                    animation_index = (animation_index + 1) % 3
                else:
                    animation_index = 0

                joueur.x, joueur.y, joueur.animation_index, joueur.en_deplacement = x, y, animation_index, en_deplacement
                joueur.update()

                for ennemi in ennemis:
                    ennemi.attaquer_joueur(joueur)

                pygame.draw.rect(ecran, (255, 0, 0), (joueur.x, joueur.y - 10, 100, 10))
                barre_vie_longueur = joueur.vie / joueur.vie_max * 100
                pygame.draw.rect(ecran, (0, 128, 0), (joueur.x, joueur.y - 10, barre_vie_longueur, 10))
                ecran.blit(joueur.image, (joueur.x, joueur.y))

                joueur.attaquer(attaques)

        for ennemi in ennemis.copy():
            ennemi.deplacer_vers_joueur(joueurs)
            for joueur in joueurs:
                if joueur.jouable:
                    ennemi.attaquer_joueur(joueur)
                    if joueur.vie <= 0:
                        joueur.jouable = False
                        joueurs_jouables -= 1

            if ennemi.points_de_vie <= 0:
                ennemis.remove(ennemi)

        for attaque in attaques.copy():
            attaque.update()
            if not attaque.is_alive():
                attaques.remove(attaque)
            attaque.render(ecran)

            for ennemi in ennemis.copy():
                if attaque.x < ennemi.x + ennemi.taille and attaque.x + attaque.degats > ennemi.x and attaque.y < ennemi.y + ennemi.taille and attaque.y + attaque.degats > ennemi.y:
                    ennemi.points_de_vie -= attaque.degats
                    attaques.remove(attaque)


        if joueurs_jouables == 0:
            perdu_text = font.render("Vous avez perdu !", True, (255, 255, 255))   #si tous mort alors fin

        if enemy_spawn_timer <= 0 and len(ennemis) < max_enemy_count:
            creer_ennemi()
            enemy_spawn_timer = 60

        enemy_spawn_timer -= 1

        for ennemi in ennemis:
            ennemi.render(ecran)

        if perdu_text:
            ecran.blit(perdu_text, (400, 500))

        pygame.display.flip()

    pygame.quit()  # quiter en appuyent sur la croi pendant le jeu
pygame.quit()  # quiter en appuyent sur la croi dans le menu


