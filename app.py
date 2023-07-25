import pygame

# Ф - включаем, запускаем pygame библиотеку
pygame.init()

# Ф - определяем переменные для размера экрана.
# Делаем это для того чтобы создавать другие элементы, размеры которых будут зависить от размера экрана игры
windowWidth = 600
windowHeight = 600

# Ф - определяем размер екрана для игры
window = pygame.display.set_mode((windowWidth, windowHeight))

# Е - событие мышки добавил 25.07
pygame.display.set_caption('событие от мыши')


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
# Ф - Определям переменную для картинки по Х
# Ф - позицию Y для первой такая же самая как и для Х
img1PosY = tableBorder + imgMargin
# Ф - после добавляем нашу картинку в игру
# window.blit(imgO, (img1PosX, img1PosY))

# E - координаты для других картинок img2 -- img9
img2PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img2PosY = tableBorder + imgMargin
# window.blit(imgO, (img2PosX, img2PosY))

img3PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img3PosY = tableBorder + imgMargin
# window.blit(imgO, (img3PosX, img3PosY))

img4PosX = tableBorder + imgMargin
img4PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize
# window.blit(imgO, (img4PosX, img4PosY))

img5PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img5PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize
# window.blit(imgO, (img5PosX, img5PosY))

img6PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img6PosY = tableBorder + 3*(imgMargin) + cellBorder + imgSize
# window.blit(imgO, (img6PosX, img6PosY))

img7PosX = tableBorder + imgMargin
img7PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
# window.blit(imgO, (img7PosX, img7PosY))

img8PosX = tableBorder + 3*(imgMargin) + cellBorder + imgSize
img8PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
# window.blit(imgO, (img8PosX, img8PosY))

img9PosX = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
img9PosY = tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize)
# window.blit(imgO, (img9PosX, img9PosY))


# Е - передаем функцию blit 2 параметра()
window.blit(imgG, (0, 0))

# Ф - тут определяем состояние игры для дальнейшей передачи в цикл ниже
running = True

# добавил ФПС и клок незнаю зачем но без них окно закрыывалось сразу же
FPS = 60
clock = pygame.time.Clock()

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
            exit()  # E - добавил потому что если оставить пустую строку то не работают ниже elif и закрывает по крестику

        # E - работа мышки оп экрану игры
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Е - нажатие клавиши мыши
            # Е - если в скобках еще дописать 1, перед event.button то покажет при нажатии что выполняется пункт 1 нажате на клавишу
            print(event.button)
        elif event.type == pygame.MOUSEMOTION:      # Е - показывает кординаты расположения мышки на поле
            # Е - выводит ее координаты (думаю приниты потом убрать  придется)
            print(event.pos)

# добавил чтоб заработал экран + выше до while running добавил еще двестроки с фпси клок
    clock.tick(FPS)

    # Ф - делаем состояние игры False. Т.е. сбрасываем
    # running = False  ---------------- ###### E - закомментировал эту строку и стало  работать.

    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()
