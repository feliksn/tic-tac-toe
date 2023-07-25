import pygame

# Ф - включаем, запускаем pygame библиотеку
pygame.init()

# Ф - определяем переменные для размера экрана.
# Делаем это для того чтобы создавать другие элементы, размеры которых будут зависить от размера экрана игры
windowWidth = 600
windowHeight = 600

# Ф - определяем размер екрана для игры
window = pygame.display.set_mode((windowWidth, windowHeight))

# Ф - определяем название для окна игры
pygame.display.set_caption("Крестики Нолики")

# Ф - определяем цвет окна
window.fill("white")

# Ф - добавляем картинки крестика и нолика
imgO = pygame.image.load("images/o.png")
imgX = pygame.image.load("images/x.png")

# E - добавляем картинку поля
imgG = pygame.image.load("images/g.png")

# Определяем размер картинок. Картинки квадратные так что можем определить один размер без высоты и ширины
imgSize = 140

# Определяем отступ для картинок в ячейке
imgMargin = 10

# Опередляем толщину границы таблицы
tableBorder = 40

# Определяем толщину границы ячеек
cellBorder = 20

# Ф - Определям переменную для картинки по Х
# Ф - позицию Х для первой картинки вычесляем по формуле (граница таблицы + отступ для картинки)
img1PosX = tableBorder + imgMargin
img1PosY = tableBorder + imgMargin

# E - координаты для других картинок img2 -- img9
img2PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img2PosY = tableBorder + imgMargin

img3PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img3PosY = tableBorder + imgMargin

img4PosX = tableBorder + imgMargin
img4PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize

img5PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img5PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize

img6PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img6PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize

img7PosX = tableBorder + imgMargin
img7PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)

img8PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img8PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)

img9PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img9PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)

# опеределяем координаты ячеек в игре и записываем в переменные, чтобы их потом использовать. А не помнить какие координаты имеет какая ячейка
cell1Pos = (img1PosX, img1PosY, img1PosX + imgSize, img1PosY + imgSize)
cell2Pos = (img2PosX, img2PosY, img2PosX + imgSize, img2PosY + imgSize)
cell3Pos = (img3PosX, img3PosY, img3PosX + imgSize, img3PosY + imgSize)
cell4Pos = (img4PosX, img4PosY, img4PosX + imgSize, img4PosY + imgSize)
cell5Pos = (img5PosX, img5PosY, img5PosX + imgSize, img5PosY + imgSize)
cell6Pos = (img6PosX, img6PosY, img6PosX + imgSize, img6PosY + imgSize)
cell7Pos = (img7PosX, img7PosY, img7PosX + imgSize, img7PosY + imgSize)
cell8Pos = (img8PosX, img8PosY, img8PosX + imgSize, img8PosY + imgSize)
cell9Pos = (img9PosX, img9PosY, img9PosX + imgSize, img9PosY + imgSize)

# Ф - добавляем в игру сетку
# Е - передаем функцию blit 2 параметра()
window.blit(imgG, (0, 0))

# Ф - тут определяем состояние игры для дальнейшей передачи в цикл ниже
running = True

# Ф - определяем переменную в которой записываем с какой картинки будем начинать игру
firstX = True

# Ф - создаем переменную массива в котором будет записывать ячейки, где уже были добавлены картинки, чтобы не добавлять их опять и опять)))
cachedPos = []

# Ф - запускаем цикл игры
while running:
    # E - немогу понять почему именно в этой позиции я пишу но вот они линии, пропишу все сразу
    '''
    pygame.draw.line(window, 'red', (118, 58), (118, 540), 10)
    pygame.draw.line(window, 'red', (298, 58), (298, 540), 10)
    pygame.draw.line(window, 'red', (478, 58), (478, 540), 10)

    pygame.draw.line(window, 'red', (58, 118), (540, 118), 10)
    pygame.draw.line(window, 'red', (58, 298), (540, 298), 10)
    pygame.draw.line(window, 'red', (58, 478), (540, 478), 10)

    pygame.draw.line(window, 'red', (56, 56), (540, 540), 10)
    pygame.draw.line(window, 'red', (540, 56), (56, 540), 10)
    '''

    # Ф - запускаем цикл, который ловит нажатие клавишей и события мышки чтобы можно было что-нибудь с этой игрой делать
    for event in pygame.event.get():
        # Ф - если ловим событие мышкой на закрытие окна
        if event.type == pygame.QUIT:
            running = False
        # E - работа мышки оп экрану игры
        # Е - нажатие клавиши мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Ф - записываем в переменные позиции мышки при нажатии мышки
            mousePosX = pygame.mouse.get_pos()[0]
            mousePosY = pygame.mouse.get_pos()[1]
            # Ф - проверяем есть ли курсор мышка в певрой ячейке когда кликаем
            # Ф - если мышка есть при клике, тогда добавляем туда картинку
            if mousePosX >= cell1Pos[0] and mousePosY >= cell1Pos[1] and mousePosX <= cell1Pos[2] and mousePosY <= cell1Pos[3]:
                if not 1 in cachedPos:
                    if firstX:
                        window.blit(imgX, (img1PosX, img1PosY))
                        firstX = False
                    else:
                        window.blit(imgO, (img1PosX, img1PosY))
                        firstX = True
                    cachedPos.append(1)

    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()
