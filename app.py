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
isXfirst = True
usedPos = []
winnedPos = [[1,2,3], [4,5,6], [7,8,9], [1,4,7],
             [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

pygame.display.set_caption(gameName)
window = pygame.display.set_mode((gameWidth, gameHeight))
window.fill(gameBg)

# Ф - добавляем картинки крестика и нолика
imgO = pygame.image.load("images/o.png")
imgX = pygame.image.load("images/x.png")
# E - добавляем картинку поля
imgG = pygame.image.load("images/g.png")

# Ф - позиции картинок для ячеек
img1 = (
    # Ф - позиция Х картинки, получение позиции х - img1[0]
    tableBorder + imgMargin,
    # Ф - позиция У картинки, получение позиции у - img1[1]
    tableBorder + imgMargin
)
img2 = (tableBorder + 3*(imgMargin) + cellBorder + imgSize, tableBorder + imgMargin)
img3 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize), tableBorder + imgMargin)
img4 = (tableBorder + imgMargin, tableBorder + 3*(imgMargin) + cellBorder + imgSize)
img5 = (tableBorder + 3*(imgMargin) + cellBorder + imgSize, tableBorder + 3*(imgMargin) + cellBorder + imgSize)
img6 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize), tableBorder + 3*(imgMargin) + cellBorder + imgSize)
img7 = (tableBorder + imgMargin, tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize))
img8 = (tableBorder + 3*(imgMargin) + cellBorder + imgSize, tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize))
img9 = (tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize), tableBorder + 5*(imgMargin) + 2*(cellBorder) + 2*(imgSize))

# Ф - позиции линий в игре, основанных на позициях картинок.
line1 = (
    # Ф - позиция х1 линии, получение позиции - line1[0]
    img1[0],
    # Ф - позиция у1 линии, получение позиции - line1[1]
    img1[1] + imgSize/2,
    # Ф - позиция х2 линии, получение позиции - line1[2]
    img3[0] + imgSize,
    # Ф - позиция у2 линии, получение позиции - line1[3]
    img3[1] + imgSize/2
)
# ......... далее сделать подобно для останльных 7 линий. можно писать в одну линию. Это я для примера написал каждую позицию отдельно, чтобы ясно видеть каждую позицию

# Ф - позиции ячеек в игре подобно line1...
cell1 = (
    # Ф - позиция х1 ячейки, получение позиции ячейки - cell1[0]
    img1[0] - imgMargin,
    # Ф - позиция y1 ячейки, получение позиции ячейки - cell1[1]
    img1[1] - imgMargin,
    # Ф - позиция х2 ячейки, получение позиции ячейки - cell1[2]
    img1[0] + imgSize + imgMargin,
    # Ф - позиция y2 ячейки, получение позиции ячейки - cell1[3]
    img1[1] + imgSize + imgMargin
)
# ........... далее сделать подобно для остальных 8 ячеек

# Ф - запускаем цикл игры
while isGameRunning:
    # Е - передаем функцию blit 2 параметра()
    window.blit(imgG, (0, 0))
    
    # Ф - после рисуем линии в игре, получая данные из переменных, записанных ранее
    pygame.draw.line(window, lineColor, (line1[0], line1[1]), (line1[2], line1[3]), lineWidth)

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


    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()