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
# Ф - Определям переменную для картинки по Х
# Ф - позицию Y для первой такая же самая как и для Х
img1PosY = tableBorder + imgMargin
# Ф - после добавляем нашу картинку в игру
window.blit(imgO, (img1PosX, img1PosY))



# Е - передаем функцию blit 2 параметра()
window.blit(imgG, (0, 0))

# Ф - тут определяем состояние игры для дальнейшей передачи в цикл ниже
running = True

# Ф - запускаем цикл игры
while running:

    # E - немогу понять почему именно в этой позиции я пишу но вот они линии, пропишу все сразу
    pygame.draw.line(window, 'red', (118, 58), (118, 540), 10)
    pygame.draw.line(window, 'red', (298, 58), (298, 540), 10)
    pygame.draw.line(window, 'red', (478, 58), (478, 540), 10)

    pygame.draw.line(window, 'red', (58, 118), (540, 118), 10)
    pygame.draw.line(window, 'red', (58, 298), (540, 298), 10)
    pygame.draw.line(window, 'red', (58, 478), (540, 478), 10)

    pygame.draw.line(window, 'red', (56, 56), (540, 540), 10)
    pygame.draw.line(window, 'red', (540, 56), (56, 540), 10)

    # Ф - запускаем цикл, который ловит нажатие клавишей и события мышки чтобы можно было что-нибудь с этой игрой делать
    for event in pygame.event.get():

        # Ф - если ловим событие мышкой на закрытие окна
        if event.type == pygame.QUIT:

            # Ф - делаем состояние игры False. Т.е. сбрасываем
            running = False

    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()
