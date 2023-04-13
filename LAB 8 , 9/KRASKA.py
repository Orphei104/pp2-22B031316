# Добавляем Библиотеки 
import random
import pygame
import sys

#Создаем функцию для круглых объектов
def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

#Создаем основную функцию для манипуляции 
def main():
    #инициализируем библиотеку пайгейм и создаем монитор с слоем на котором будут рисунки
    pygame.init()
    global screen, baseLayer
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()

    # Цвета
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    color = WHITE

    #Переменные которые хранят в себе старые координаты
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1

    screen.fill((0, 0, 0))

    # Переменные что хранят в себе последние значения 
    isMouseDown = False
    figure = ""

    last_pos = (0, 0)
    radius = 1

    #основная линия для запуска окна в пайгейм
    while True:
        #Пишем pressed которая откатывает все нажатые последнии клавиши если они нажаты
        pressed = pygame.key.get_pressed()
        #цикл чтобы можно было закрыть окно
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # То что считает момент когда ЛКМ нажат и обратно
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True
                    currentX = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))

            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]

            # Цвета для кнопок
            if pressed[pygame.K_r]:
                color = RED
            if pressed[pygame.K_g]:
                color = GREEN
            if pressed[pygame.K_b]:
                color = BLUE

            # прямоугольник
            if pressed[pygame.K_1]:
                figure = "rectangle"
            # овал
            if pressed[pygame.K_2]:
                figure = "ellipse"

            # круг
            if pressed[pygame.K_3]:
                figure = "circle"
            # квадрат
            if pressed[pygame.K_4]:
                figure = "square"
            # Прямоугольный треугольник
            if pressed[pygame.K_5]:
                figure = "right triangle"
            # Правильный треугольник
            if pressed[pygame.K_6]:
                figure = "equilateral triangle"
            # ромб
            if pressed[pygame.K_7]:
                figure = "rhombus"

            # Стерка(резинка)
            if pressed[pygame.K_8]:
                figure = "eraser"

        # прямоугольник
        if figure == "rectangle":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        # овал
        if figure == "ellipse":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX, prevY, currentX, currentY)
                pygame.draw.ellipse(screen, color, pygame.Rect(r), 1)
        # круг
        if figure == "circle":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                center = calculateCenter(prevX, prevY, currentX, currentY)
                radius = calculateRadius(prevX, prevY, currentX, currentY)
                pygame.draw.circle(screen, color, tuple(center), radius, 1)
        # квадрат
        if figure == "square":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateSquare(prevX, prevY, currentX, currentY)
                pygame.draw.rect(screen, color, pygame.Rect(r), 1)

        # прямоугольный треугольник
        if figure == "right triangle":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = rightTriangle(prevX, prevY, currentX, currentY)
                pygame.draw.polygon(screen, color, r, 1)

        # Правильный треугольник
        if figure == "equilateral triangle":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = equilateralTriangle(prevX, prevY, currentX, currentY)
                pygame.draw.polygon(screen, color, r, 1)
        # Ромб
        if figure == "rhombus":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRhombus(prevX, prevY, currentX, currentY)
                pygame.draw.polygon(screen, color, r, 1)

        # Стерка(резинка)
        if figure == "eraser":
            if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
                screen.blit(baseLayer, (5, 5))
                eraser()

        pygame.display.flip()
        clock.tick(60)

# Функции для каждой из фигур; каждая из которых берет четыре переменные как сами координаты и проводит между нужными линию
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def calculateSquare(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), (abs(x1 - x2) + abs(y1 - y2)) / 2, (abs(x1 - x2) + abs(y1 - y2)) / 2)


def calculateCenter(x1, y1, x2, y2):
    return [min(x1, x2) + abs(x1 - x2) / 2, min(y1, y2) + abs(y1 - y2) / 2]


def calculateRadius(x1, y1, x2, y2):
    return int(abs(x1 - x2) / 2)


def rightTriangle(x1, y1, x2, y2):
    return ((min(x1, x2), min(y1, y2)), (min(x1, x2), max(y1, y2)), (max(x1, x2), max(y1, y2)))


def equilateralTriangle(x1, y1, x2, y2):
    return (((x1 + x2) / 2, min(y1, y2)), (min(x1, x2), max(y1, y2)), (max(x1, x2), max(y1, y2)))


def calculateRhombus(x1, y1, x2, y2):
    a1 = (min(x1, x2), (y1 + y2) / 2)
    a2 = ((x1 + x2) / 2, min(y1, y2))
    a3 = (max(x1, x2), (y1 + y2) / 2)
    a4 = ((x1 + x2) / 2, max(y1, y2))
    return (a1, a2, a3, a4)

#функция для Стерки(резинки)
def eraser():
    clock = pygame.time.Clock()

    prevX = 0
    prevY = 0

    # screen.fill((0, 0, 0))

    isMouseDown = False

    while True:

        pressed = pygame.key.get_pressed()

        currentX = prevX
        currentY = prevY
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                currentX = event.pos[0]
                currentY = event.pos[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return 0

        if isMouseDown:
            pygame.draw.line(screen, (0, 0, 0), (prevX, prevY), (currentX, currentY), 10)

        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)


main()