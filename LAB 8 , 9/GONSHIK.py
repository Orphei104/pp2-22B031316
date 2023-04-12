import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 80

# Enemy
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
ADDNEWCOINRATE = 1
PLAYERMOVERATE = 5
count = 3

# Coin
COINMAXSIZE = 10
COINMINSPEED = 15
COINMAXSPEED = 15
ADDNEWCOINRATE = 1

def terminate() :
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey() :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :  # escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies) :
    for b in baddies :
        if playerRect.colliderect(b['rect']) :
            return True
    return False


def playerHasHitCoin(playerRect, coins):
    for c in coins:
        if playerRect.colliderect(c['coinrect']):
            coins.pop()
            return True
    return False


def drawText(text, font, surface, x, y) :
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('THE REALNYIE SHASHKI NA DOROGAX')
pygame.mouse.set_visible(False)

# fonts
font = pygame.font.SysFont(None, 30)

# sound
pygame.mixer.music.load('pygame_data/erondondon.mp3')
gameOverSound = pygame.mixer.Sound('pygame_data/roblox_death_sound.mp3')
laugh = pygame.mixer.Sound('pygame_data/shaokhan_laugh.mp3')

# coin collection sound
coin_collection = pygame.mixer.Sound("pygame_data/sonic_ring.mp3")

# images
playerImage = pygame.image.load('pygame_data/car1.png')
car3 = pygame.image.load('pygame_data/car3.png')
car4 = pygame.image.load('pygame_data/car4.png')
playerRect = playerImage.get_rect()

baddieImage = pygame.image.load('pygame_data/car2.png')
sample = [car3, car4, baddieImage]

wallLeft = pygame.image.load('pygame_data/left.png')
wallRight = pygame.image.load('pygame_data/right.png')

# coin image
coinImage = pygame.image.load("pygame_data/sonic_ring.gif")
coinImageBig = pygame.image.load("pygame_data/sonic_super_ring.png")
coinRect = coinImage.get_rect()

# initial position of a coin
# x = random.randint(128, 400)
# y = random.randint(128, 400)
# coinRect.center = (x, y)

# "Start" screen
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('SHOW ME YOUR SHUMAXER MOTIVATION', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0

if not os.path.exists("pygame_data/save.dat") :
    f = open("pygame_data/save.dat", 'w')
    f.write(str(zero))
    f.close()

v = open("pygame_data/save.dat", 'r')
topScore = int(v.readline())
v.close()

while (count > 0) :
    # start of the game
    baddies = []

    # coins
    coins = []
    score = 0

    # coin score
    coin_score = 0

    # coin size
    coinSize1 =  30
    coinSize2 = 40

    # list ti compare sizes of coins
    cointypeComp = []

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    # coin addition will be 1 by default
    coinAddCounter = 0

    pygame.mixer.music.play(-1, 0, 0)

    while True :  # the game loop
        score += 1  # increase score

        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()

            if event.type == KEYDOWN :
                if event.key == ord('z') :
                    reverseCheat = True
                if event.key == ord('x') :
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a') :
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w') :
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s') :
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP :
                if event.key == ord('z') :
                    reverseCheat = False
                    score = 0
                if event.key == ord('x') :
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE :
                    terminate()

                if event.key == K_LEFT or event.key == ord('a') :
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d') :
                    moveRight = False
                if event.key == K_UP or event.key == ord('w') :
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s') :
                    moveDown = False

        # Add new baddies at the top of the screen
        if not reverseCheat and not slowCheat :
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE :
            baddieAddCounter = 0
            baddieSize = 30

            # Increase the speed of Enemy when the player earns N coins
            if coin_score >= 5:
                BADDIEMINSPEED = 50
                BADDIEMAXSPEED = 50

            else:
                BADDIEMINSPEED = 8
                BADDIEMAXSPEED = 8

            newBaddie = {'rect' : pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect' : pygame.Rect(0, 0, 126, 600),
                        'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface' : pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect' : pygame.Rect(497, 0, 303, 600),
                         'speed' : random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface' : pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)

        if not reverseCheat and not slowCheat:
            if(len(coins)<=0):
                coinAddCounter += 1

        if coinAddCounter == ADDNEWCOINRATE:
            coinAddCounter = 0

            newCoin = {'coinrect': pygame.Rect(random.randint(140, 485), 0 - coinSize1, 27, 27),
                         'coinspeed': random.randint(COINMINSPEED, COINMAXSPEED),
                         'coinsurface': pygame.transform.scale(coinImage, (27, 27)),
                         }
            # coins.append(newCoin)

            newCoinBig = {'coinrect': pygame.Rect(random.randint(140, 485), 0 - coinSize2, 40, 40),
                         'coinspeed': random.randint(COINMINSPEED, COINMAXSPEED),
                         'coinsurface': pygame.transform.scale(coinImageBig, (40, 40)),
                         }
            # coins.append(newCoinBig)
            comp = [newCoinBig['coinrect'].size, newCoin['coinrect'].size]
            definecointype = [newCoin, newCoinBig]

            x = random.choice(definecointype)

            coins.append(x)

            # cointypeComp.append(y['coinrect'].size)

            print(cointypeComp)

            # sideLeftCoin = {'coinrect': pygame.Rect(0, 0, 126, 600),
            #             'coinspeed': random.randint(COINMINSPEED, COINMAXSPEED),
            #             'coinsurface': pygame.transform.scale(wallLeft, (126, 599)),
            #             }
            # coins.append(sideLeftCoin)
            #
            # sideRightCoin = {'coinrect': pygame.Rect(497, 0, 303, 600),
            #              'coinspeed': random.randint(COINMINSPEED, COINMAXSPEED),
            #              'coinsurface': pygame.transform.scale(wallRight, (303, 599)),
            #              }
            # coins.append(sideRightCoin)

        # Move the player around.
        if moveLeft and playerRect.left > 0 :
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH :
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0 :
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT :
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the baddies down.
        for b in baddies :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:] :
            if b['rect'].top > WINDOWHEIGHT :
                baddies.remove(b)

        # Move the coins down.
        for c in coins :
            if not reverseCheat and not slowCheat :
                c['coinrect'].move_ip(0, c['coinspeed'])
            elif reverseCheat :
                c['coinrect'].move_ip(0, -5)
            elif slowCheat :
                c['coinrect'].move_ip(0, 1)

        # Delete coins that have fallen past the bottom.
        for c in coins[:]:
            if c['coinrect'].top > WINDOWHEIGHT:
                coins.remove(c)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)

        # Draw the coin score
        drawText('Coins: %s' % (coin_score), font, windowSurface, 400, 0)

        # image addition
        windowSurface.blit(playerImage, playerRect)

        for b in baddies :
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        for c in coins :
            windowSurface.blit(c['coinsurface'], c['coinrect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if playerHasHitBaddie(playerRect, baddies) :
            if score > topScore :
                g = open("pygame_data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break

        mainClock.tick(FPS)

        # coin collection
        if playerHasHitCoin(playerRect, coins):
            y = x['coinrect'].size
            cointypeComp.append(y)

            if cointypeComp[-1] == (27, 27):
                coin_score += 1
            else:
                coin_score += 3

            coin_collection.play()
            cointypeComp.clear()
            # coin_score += 1
            x = random.randint(128, 400)
            y = random.randint(128, 400)
            # coinRect.top = y
            coinRect.center = (x, y)
            coin_collection.play()
            pygame.display.update()

        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    count = count - 1
    gameOverSound.play()
    time.sleep(1)

    if (count == 0) :
        laugh.play()
        drawText('Game over, bro touch the grass', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 30)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
        gameOverSound.stop()