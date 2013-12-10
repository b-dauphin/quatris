# -*- coding:Utf-8 -*
try:
    import pygame
    from pygame.locals import *
    from classes import *
    from random import randrange
except:
    print("""This program needs Pygame and classes.py.""")

#Initialisation de Pygame.
pygame.init()

#QWERTY->AZERTY
K_q, K_a = K_a, K_q
K_w, K_z = K_z, K_w

#Définition de la taille de la fenêtre.
fenetre = pygame.display.set_mode((16*(colonnes+7), 16*(lignes+2)))

#Importation des images
img0 = pygame.image.load("img/0.png").convert()
img1 = pygame.image.load("img/1.png").convert()
img2 = pygame.image.load("img/2.png").convert()
img3 = pygame.image.load("img/3.png").convert()
img4 = pygame.image.load("img/4.png").convert()
img5 = pygame.image.load("img/5.png").convert()
img6 = pygame.image.load("img/6.png").convert()
img7 = pygame.image.load("img/7.png").convert()
imgBord = pygame.image.load("img/bord.png").convert()

miniat0 = pygame.image.load("img/m0.png").convert()
miniat1 = pygame.image.load("img/m1.png").convert()
miniat2 = pygame.image.load("img/m2.png").convert()
miniat3 = pygame.image.load("img/m3.png").convert()
miniat4 = pygame.image.load("img/m4.png").convert()
miniat5 = pygame.image.load("img/m5.png").convert()
miniat6 = pygame.image.load("img/m6.png").convert()
miniat7 = pygame.image.load("img/m7.png").convert()

fin = pygame.image.load("img/fin.png").convert_alpha()

#Mise des images en fond et rafraichissement de l'écran.
for i in range(colonnes+7):
    if i == 0 or i > colonnes:
        for j in range(lignes+2):
            fenetre.blit(imgBord, (i*16, j*16))
    else:
        for j in range(lignes+2):
            if j == 0 or j == lignes+1:
                fenetre.blit(imgBord, (i*16, j*16))
            else:
                fenetre.blit(img0, (i*16, j*16))
fenetre.blit(miniat0, ((colonnes+2)*16, 16))
pygame.display.flip()

def apparition(pce):
    if not(table[pce.x + pce.ocp[0][0]][pce.y + pce.ocp[0][1]]\
       or table[pce.x + pce.ocp[1][0]][pce.y + pce.ocp[1][1]]\
       or table[pce.x + pce.ocp[2][0]][pce.y + pce.ocp[2][1]]\
       or table[pce.x + pce.ocp[3][0]][pce.y + pce.ocp[3][1]]):
        
        table[pce.x + pce.ocp[0][0]][pce.y + pce.ocp[0][1]] = pce.num
        table[pce.x + pce.ocp[1][0]][pce.y + pce.ocp[1][1]] = pce.num
        table[pce.x + pce.ocp[2][0]][pce.y + pce.ocp[2][1]] = pce.num
        table[pce.x + pce.ocp[3][0]][pce.y + pce.ocp[3][1]] = pce.num
    else:
        perdu = True
        print(perdu)

def affiche():
    for i in range(colonnes):
        for j in range(lignes):
            if table[i][j]%10 == 0:
                fenetre.blit(img0, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 1:
                fenetre.blit(img1, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 2:
                fenetre.blit(img2, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 3:
                fenetre.blit(img3, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 4:
                fenetre.blit(img4, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 5:
                fenetre.blit(img5, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 6:
                fenetre.blit(img6, (16*(i+1), 16*(j+1)))
            elif table[i][j]%10 == 7:
                fenetre.blit(img7, (16*(i+1), 16*(j+1)))
    if piece2.num == 1:
        fenetre.blit(miniat1, ((colonnes+2)*16, 16))
    elif piece2.num == 2:
        fenetre.blit(miniat2, ((colonnes+2)*16, 16))
    elif piece2.num == 3:
        fenetre.blit(miniat3, ((colonnes+2)*16, 16))
    elif piece2.num == 4:
        fenetre.blit(miniat4, ((colonnes+2)*16, 16))
    elif piece2.num == 5:
        fenetre.blit(miniat5, ((colonnes+2)*16, 16))
    elif piece2.num == 6:
        fenetre.blit(miniat6, ((colonnes+2)*16, 16))
    elif piece2.num == 7:
        fenetre.blit(miniat7, ((colonnes+2)*16, 16))
    else:
        fenetre.blit(miniat0, ((colonnes+2)*16, 16))
    pygame.display.flip()

def genere():
    numero = randrange(7)+1
    if numero == 1:
        piece = I()
    elif numero == 2:
        piece = O()
    elif numero == 3:
        piece = T()
    elif numero == 4:
        piece = L()
    elif numero == 5:
        piece = J()
    elif numero == 6:
        piece = Z()
    elif numero == 7:
        piece = S()
    return piece

piece = genere()
piece2 = genere()
apparition(piece)
affiche()

def fixe():
    for i in range(colonnes):
        for j in range(lignes):
            if not table[i][j] // 10 and table[i][j] % 10:
                table[i][j] += 10

continuer = True
gravit = True
perdu = False
delai = 2000
pygame.time.set_timer(USEREVENT + 1, delai)

def effLigne(pos):
    for j in range(pos, -1, -1):
        for i in range(colonnes):
            if j:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = 0
    piece.y += 1
    piece.remonte()


while continuer:
    #Limitation du nombre de cycles.
    pygame.time.Clock().tick(30)
    
    #On parcours la liste de tous les événements reçus...
    for event in pygame.event.get():
        #Si un des événements est de type QUIT...
        if event.type == QUIT:
            #Arrêt de la boucle.
            continuer = False
        
        #Touche du clavier
        if event.type == KEYDOWN:
            if event.key == K_e or event.key == K_UP:
                piece.tourneHoraire()
                affiche()
            elif event.key == K_a:
                piece.tourneAntiHoraire()
                affiche()
            elif event.key == K_q or event.key == K_LEFT:
                piece.deplace('gauche')
                affiche()
            elif event.key == K_d or event.key == K_RIGHT:
                piece.deplace('droite')
                affiche()
            elif event.key == K_s or event.key == K_DOWN:
                gravit = piece.deplace('bas')
                affiche()
            elif event.key == K_SPACE or event.key == K_RETURN:
                gravit = piece.deplace('chute')
                affiche()
        
        if event.type == (USEREVENT + 1):
            gravit = piece.deplace('bas')
            affiche()
        if not gravit:
            gravit = True
            fixe()
            piece = piece2
            apparition(piece)
            
            if perdu:
                for i in range(colonnes):
                    for j in range(lignes):
                        fenetre.blit(fin, (16*(i+1), 16*(j+1)))
                pygame.display.flip()
                continuer = False
            else:
                piece2 = genere()
                for j in range(lignes):
                    ligne = True
                    for i in range(colonnes):
                        if not table[i][j]:
                            ligne = False
                    if ligne:
                        effLigne(j)
                affiche()
                pygame.time.set_timer(USEREVENT + 1, delai)
