import pygame, random, sys
from pygame.locals import *



#jump informations
isJump = False
jumpCount = 8


#Animation
RunRight = [pygame.transform.scale(pygame.image.load('RR1.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR2.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR3.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR4.png'), (233,160)), pygame.image.load('RR5.png'), pygame.image.load('RR6.png'), pygame.image.load('RR7.png'), pygame.image.load('RR8.png'), pygame.image.load('RR9.png'),pygame.image.load('RR10.png'),pygame.image.load('RR11.png')]
RunLeft = [pygame.image.load('RL1.png'), pygame.image.load('RL2.png'), pygame.image.load('RL3.png'), pygame.image.load('RL4.png'), pygame.image.load('RL5.png'), pygame.image.load('RL6.png'), pygame.image.load('RL7.png'), pygame.image.load('RL8.png'), pygame.image.load('RL9.png'),pygame.image.load('RL10.png'),pygame.image.load('RL11.png')]

bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale2x(bg)
x = 20
y = 10


#Animations info
walkCount = 0

#playermoves

def redrawGameWindow():
    global walkCount
    windowSurface.blit(bg, (0, 0))
    if walkCount + 1 >= 33:
        walkCount = 0

    if moveLeft:
        windowSurface.blit(RunLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif moveRight:
        windowSurface.blit(RunRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        windowSurface.blit(playerImage, (x, y))

    pygame.display.update()


#sol qui bouge
#floor_surface = pygame.image.load('base.png')
#floor_surface = pygame.transform.scale2x(floor_surface)
#floor_x_pos = 0
#def mouv_sol() :
    #windowSurface.blit(floor_surface, (floor_x_pos, 500))
    #windowSurface.blit(floor_surface, (floor_x_pos +600, 500))


WINDOWWIDTH = 900
WINDOWHEIGHT = 700
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
BADDIEMINSIZE = 25
BADDIEMAXSIZE = 50
BADDIEMINSPEED = 0
BADDIEMAXSPEED = 0
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 10
#character informations
x = 5
y = 20
width = 64
height = 64
vel = 10

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set up pygame, the window, and the mouse cursor.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('coronascape')


# Set up the fonts.
font = pygame.font.SysFont(None,48)

# Set up sounds.
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# Set up images.
playerImage = pygame.image.load('Standing.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('virus.png')

# Show the "Start" screen.
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # Set up the start of the game.
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > PLAYERMOVERATE:
            x -= PLAYERMOVERATE
            moveLeft = True
            moveRight = False
        elif keys[pygame.K_RIGHT] and x < 900 - width - PLAYERMOVERATE:
            x += PLAYERMOVERATE
            moveLeft = False
            moveRight = True

        else:
            moveRight = False
            moveLeft = False
            walkCount = 0

        if not (isJump):
            if keys[pygame.K_UP]:
                isJump = True
                moveRight = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -8:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1

            else:
                isJump = False
                jumpCount = 8

        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        redrawGameWindow()

        # Move the baddies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)



        # sol en mouvement
       #floor_x_pos -= 1
        #mouv_sol()
        #if floor_x_pos <= -600:
            #floor_x_pos = 0


        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(60)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()

