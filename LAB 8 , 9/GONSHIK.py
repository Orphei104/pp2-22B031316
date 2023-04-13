#Библиотеки
import pygame, random, sys, os, time
from pygame.locals import *
#Высота и ширина окна 
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 80

# ВРАГИ
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
ADDNEWCOINRATE = 1
PLAYERMOVERATE = 5
count = 3

# МОНЕТКА
COINMAXSIZE = 10
COINMINSPEED = 15
COINMAXSPEED = 15
ADDNEWCOINRATE = 1

#Это сделано чтобы программа при закрытие закрылась удачно
def terminate() :
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey() :
    while True :
        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :  # Выходит из проги
                    terminate()
                return

#функция если игрок столкнеться с врагом
def playerHasHitBaddie(playerRect, baddies) :
    for b in baddies :
        if playerRect.colliderect(b['rect']) :
            return True
    return False


#функция если игрок столкнеться с монеткой 
def playerHasHitCoin(playerRect, coins):
    for c in coins:
        if playerRect.colliderect(c['coinrect']):
            coins.pop()
            return True
    return False


#функция для текста который позже будем отображать
def drawText(text, font, surface, x, y) :
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Включаем и инициализируем все по деффолту
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('THE REALNYIE SHASHKI NA DOROGAX')
pygame.mouse.set_visible(False)
# Шрифт
font = pygame.font.SysFont(None, 30)
# Звуки и музыка
pygame.mixer.music.load('pygame_data/erondondon.mp3')
gameOverSound = pygame.mixer.Sound('pygame_data/roblox_death_sound.mp3')
laugh = pygame.mixer.Sound('pygame_data/shaokhan_laugh.mp3')
# Звук при собирания монетки
coin_collection = pygame.mixer.Sound("pygame_data/sonic_ring.mp3")
# И все картинки которые будут в игре
playerImage = pygame.image.load('pygame_data/car1.png')
car3 = pygame.image.load('pygame_data/car3.png')
car4 = pygame.image.load('pygame_data/car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('pygame_data/car2.png')
# Лист из врагов дабы не добавлять каждого по отдельности
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('pygame_data/left.png')
wallRight = pygame.image.load('pygame_data/right.png')
coinImage = pygame.image.load("pygame_data/sonic_ring.gif")
coinImageBig = pygame.image.load("pygame_data/sonic_super_ring.png")
coinRect = coinImage.get_rect()

# Окно и надписи при запуске кода 
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('SHOW ME YOUR SHUMAXER MOTIVATION', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3) + 30)
pygame.display.update()
waitForPlayerToPressKey()
zero = 0

# для сохранения результата или HIGHSCORE
if not os.path.exists("pygame_data/save.dat") :
    f = open("pygame_data/save.dat", 'w')
    f.write(str(zero))
    f.close()

v = open("pygame_data/save.dat", 'r')
topScore = int(v.readline())
v.close()

# Настройка для начала игрыи что кто будет
while (count > 0) :
    # Начало
    baddies = []

    # Монетки(кольца)
    coins = []
    score = 0

    # Кол-во очков
    coin_score = 0

    # Размер Монеток
    coinSize1 =  30
    coinSize2 = 40

    # Лист для сравнения монеток 
    cointypeComp = []

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    # Обычные монетки дают 1 очко по умолчанию
    coinAddCounter = 0
    # Микшер чтобы проигрывать
    pygame.mixer.music.play(-1, 0, 0)

    # Цикл основной игры
    while True :  
        score += 1  

        for event in pygame.event.get() :
            if event.type == QUIT :
                terminate()
            # Биндим кнопки на функционал
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

        # Добавляем новых врагов 
        if not reverseCheat and not slowCheat :
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE :
            baddieAddCounter = 0
            baddieSize = 30

            # УВЕЛИЧИВАЕМ СКОРОСТЬ при наборе определнного кол-во монет
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
            print(cointypeComp)

        # Движение игрока по стороннам
        if moveLeft and playerRect.left > 0 :
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH :
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0 :
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT :
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Откат врагов в реверс
        for b in baddies :
            if not reverseCheat and not slowCheat :
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat :
                b['rect'].move_ip(0, -5)
            elif slowCheat :
                b['rect'].move_ip(0, 1)

        # Удалить врагов что снизу чтобы они не скапливались
        for b in baddies[:] :
            if b['rect'].top > WINDOWHEIGHT :
                baddies.remove(b)

        # Откат монеток
        for c in coins :
            if not reverseCheat and not slowCheat :
                c['coinrect'].move_ip(0, c['coinspeed'])
            elif reverseCheat :
                c['coinrect'].move_ip(0, -5)
            elif slowCheat :
                c['coinrect'].move_ip(0, 1)

        # Удалить монетки что на дне
        for c in coins[:]:
            if c['coinrect'].top > WINDOWHEIGHT:
                coins.remove(c)

        # Рисовка игрового мира
        windowSurface.fill(BACKGROUNDCOLOR)

        # Рисовка Очков
        drawText('Score: %s' % (score), font, windowSurface, 128, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 20)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 40)

        # Рисовка монеток 
        drawText('Coins: %s' % (coin_score), font, windowSurface, 400, 0)

        # Добавление всех картинок 
        windowSurface.blit(playerImage, playerRect)

        for b in baddies :
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        for c in coins :
            windowSurface.blit(c['coinsurface'], c['coinrect'])

        pygame.display.update()

        # Проверка на столкновение с врагом
        if playerHasHitBaddie(playerRect, baddies) :
            if score > topScore :
                g = open("pygame_data/save.dat", 'w')
                g.write(str(score))
                g.close()
                topScore = score
            break

        mainClock.tick(FPS)

        # Сбор монеток
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

    # "Game Over" Окно
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