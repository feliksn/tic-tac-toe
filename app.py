import pygame

pygame.init()

# Определяем настройки игры
gameName = "Крестики-нолики"
gameBg = "#ffffff"
gameWidth = 600
gameHeight = 600
imgSize = 140
imgMargin = 10
tableBorder = 40
cellBorder = 20
lineColor = "#ff0000"
lineWidth = 10
isGameRunning = True
winnedPos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
             [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

pygame.display.set_caption(gameName)
window = pygame.display.set_mode((gameWidth, gameHeight))
window.fill(gameBg)

# Ф - добавляем картинки крестика и нолика
imgO = pygame.image.load("images/o.png")
imgX = pygame.image.load("images/x.png")
# E - добавляем картинку поля
imgG = pygame.image.load("images/g.png")

img1 = (tableBorder + imgMargin, tableBorder + imgMargin)
img2 = (tableBorder + 3*(imgMargin) + cellBorder +
        imgSize, tableBorder + imgMargin)
img3 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) +
        2*(imgSize), tableBorder + imgMargin)
img4 = (tableBorder + imgMargin, tableBorder +
        3*(imgMargin) + cellBorder + imgSize)
img5 = (tableBorder + 3*(imgMargin) + cellBorder + imgSize,
        tableBorder + 3*(imgMargin) + cellBorder + imgSize)
img6 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize),
        tableBorder + 3*(imgMargin) + cellBorder + imgSize)
img7 = (tableBorder + imgMargin, tableBorder + 5 *
        (imgMargin) + 2*(cellBorder) + 2*(imgSize))
img8 = (tableBorder + 3*(imgMargin) + cellBorder + imgSize,
        tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize))
img9 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize),
        tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize))

line1 = (tableBorder + imgMargin, tableBorder + imgMargin + imgSize/2,
         gameWidth - tableBorder - imgMargin, tableBorder + imgMargin + imgSize / 2)
line2 = (tableBorder + imgMargin, tableBorder + 3*imgMargin + 1.5*imgSize + cellBorder,
         gameWidth - tableBorder - imgMargin, tableBorder + 3*imgMargin + 1.5*imgSize + cellBorder)
line3 = (tableBorder + imgMargin, tableBorder + 5*imgMargin + 2.5*imgSize + 2*cellBorder,
         gameWidth - tableBorder - imgMargin, tableBorder + 5*imgMargin + 2.5*imgSize, 2*cellBorder)
line4 = (tableBorder + imgMargin + imgSize/2, tableBorder + imgMargin,
         tableBorder + imgMargin + imgSize/2, gameHeight - tableBorder - imgMargin)
line5 = (tableBorder + 3*imgMargin + 1.5*imgSize + cellBorder, tableBorder + imgMargin,
         tableBorder + 3*imgMargin + 1.5*imgSize + cellBorder, gameHeight - tableBorder - imgMargin)
line6 = (tableBorder + 5*imgMargin + 2.5*imgSize + 2*cellBorder, tableBorder + imgMargin,
         tableBorder + 5*imgMargin + 2.5*imgSize + 2*cellBorder, gameHeight - tableBorder - imgMargin)
line7 = (tableBorder + imgMargin, tableBorder + imgMargin, gameWidth -
         tableBorder - imgMargin, gameHeight - tableBorder - imgMargin)
line8 = (gameWidth - tableBorder - imgMargin, tableBorder + imgMargin, tableBorder + imgMargin, gameHeight - tableBorder -
         imgMargin)

cell1 = (tableBorder, tableBorder, tableBorder + 2*imgMargin +
         imgSize, tableBorder + 2*imgMargin + imgSize)
cell2 = (tableBorder + 2*imgMargin + imgSize + cellBorder, tableBorder, tableBorder +
         4*imgMargin + 2*imgSize + cellBorder, tableBorder + 2*imgMargin + imgSize)
cell3 = (tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder, tableBorder, tableBorder +
         6*imgMargin + 3*imgSize + 2*cellBorder, tableBorder + 2*imgMargin + imgSize)
cell4 = (tableBorder, tableBorder + 2*imgMargin + imgSize + cellBorder, tableBorder +
         2*imgMargin + imgSize, tableBorder + 4*imgMargin + 2*imgSize + cellBorder)
cell5 = (tableBorder + 2*imgMargin + imgSize + cellBorder, tableBorder + 2*imgMargin + imgSize + cellBorder,
         tableBorder + 4*imgMargin + 2*imgSize + cellBorder, tableBorder + 4*imgMargin + 2*imgSize + cellBorder)
cell6 = (tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder, tableBorder + 2*imgMargin + imgSize + cellBorder,
         tableBorder + 6*imgMargin + 3*imgSize + 2*cellBorder, tableBorder + 4*imgMargin + 2*imgSize + cellBorder)
cell7 = (tableBorder, tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder, tableBorder +
         2*imgMargin + imgSize, tableBorder + 6*imgMargin + 3*imgSize + 2*cellBorder)
cell8 = (tableBorder + 2*imgMargin + imgSize + cellBorder, tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder,
         tableBorder + 4*imgMargin + 2*imgSize + cellBorder, tableBorder + 6*imgMargin + 3*imgSize + 2*cellBorder)
cell9 = (tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder, tableBorder + 4*imgMargin + 2*imgSize + 2*cellBorder,
         tableBorder + 6*imgMargin + 3*imgSize + 2*cellBorder,  tableBorder + 6*imgMargin + 3*imgSize + 2*cellBorder)


# Ф - запускаем цикл игры
while isGameRunning:
    # Е - передаем функцию blit 2 параметра()
    window.blit(imgG, (0, 0))

    # Ф - после рисуем линии в игре, получая данные из переменных, записанных ранее
    pygame.draw.line(window, lineColor,
                     (line1[0], line1[1]), (line1[2], line1[3]), lineWidth)

    # Ф - запускаем цикл, который ловит нажатие клавишей и события мышки чтобы можно было что-нибудь с этой игрой делать
    for event in pygame.event.get():

        # Ф - если ловим событие мышкой на закрытие окна
        if event.type == pygame.QUIT:
            isGameRunning = False

        # E - работа мышки оп экрану игры
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Е - нажатие клавиши мыши
            # Е - если в скобках еще дописать 1, перед event.button то покажет при нажатии что выполняется пункт 1 нажате на клавишу
            print(event.button)

        elif event.type == pygame.MOUSEMOTION:      # Е - показывает кординаты расположения мышки на поле
            # Е - выводит ее координаты (думаю приниты потом убрать  придется)
            print(event.pos)

         # Е - выводит позицию клика мышки
        x, y = pygame.mouse.get_pos()
        print('Mouse position: ({},{})'.format(x, y))

    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()
