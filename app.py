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

# Ф - добавляем таблицу игры
imgG = pygame.image.load("images/g.png")
window.blit(imgG,(0,0))

# Ф - Добаляем функцию которая будет возрвращать координаты картинки по переданному номеру ячейки, как аргумент
def getImgPos(index):
    # Определяем размер картинок. Картинки квадратные так что можем определить один размер без высоты и ширины
    imgSize = 140
    # Определяем отступ для картинок в ячейке
    imgMargin = 10
    # Опередляем толщину границы таблицы
    tableBorder = 40
    # Определяем толщину границы ячеек
    cellBorder = 20
    # Ф - цикл for от 0 до 8 (от количества ячеек в игре)
    for cell in range(9):
        # Ф - когда цикл проходит находится в 1 ячейке, то устанавливаем начальные значения переменных 
        if cell == 0:
            # Ф - тут переменные с количеством отступа для картинок в ячейке по кординатам Х и У (1 - означает количество отступов 1*10px.) Т.е. в начале и по Х и по У у нас одинаковое количество отсупов
            marginsX = marginsY = 1
            # Ф - тут так же определяем отступы(cellBordersX, cellBordersY - позиция картинки с границами ячеек) в первой ячейке нет никаких границ значит 0 (0*20px)
            # Ф - позиция картинки относительно других картинок (imgSizesX, imgSizesY ). В первой ячейке нет картинок слева значит 0(0*140px) 
            cellBordersX = cellBordersY = imgSizesX = imgSizesY = 0
        elif cell % 3 == 0:
            # Ф - когда находимся в 4 и 7 ячейке (т.е. в цикле cell=3 или cell=6, т.е. индекс ячейки кратный 3) количество отступов для картинки marginsX, а также кол-во границ и кол-во картинок слева(cellBordersX, imgSizesX) определяем как начальные без измененй 1
            marginsX = 1
            cellBordersX = imgSizesX = 0
            # Ф - кол-во отступов для картинки определяем вниз +2(marginsY), кол-во границ ячеек определяем вниз +1(cellBordersY), кол-во картинок со вниз +1(imgSizesY)
            marginsY += 2
            cellBordersY += 1
            imgSizesY +=1
        else:
            # Ф - в остальных случаях когда цикл находиться не в ячейке 1, находимся в ячейках (2,3,5,6,8,9) не изменяем позиции картинок по У, только по Х. Т.е. кол-во отступов для картинки +2. Кол-во границ ячеек +1. Кол-во отступов картинок слева +1
            marginsX += 2
            cellBordersX += 1
            imgSizesX += 1
        
        # Ф - к конце функции добавляем условие которое проверяет номер ячейки (аргумента функции) с индексом ячейки в цикле и в условии возращаем координаты выбранной ячейки
        if cell == index-1:
            # Ф - записываем все изменения в переменные позиций и рисуем в игре
            posX = tableBorder + marginsX*imgMargin + cellBordersX*cellBorder + imgSizesX*imgSize
            posY = tableBorder + marginsY*imgMargin + cellBordersY*cellBorder + imgSizesY*imgSize
            return {"x":posX, "y":posY}

# Ф - добавляем функцию создания, получения координат по номеру ячейки и добавления картинки в таблицу игры
def addImg(name,index):
    img = pygame.image.load("images/{}.png".format(name))
    imgPos = getImgPos(index)
    window.blit(img, (imgPos["x"], imgPos["y"]))

# Ф - тут определяем состояние игры для дальнейшей передачи в цикл ниже
running = True

# Ф - запускаем цикл игры
while running:

    # E - немогу понять почему именно в этой позиции я пишу но вот они линии, пропишу все сразу
    # pygame.draw.line(window, 'red', (118, 58), (118, 540), 10)
    # pygame.draw.line(window, 'red', (298, 58), (298, 540), 10)
    # pygame.draw.line(window, 'red', (478, 58), (478, 540), 10)

    # pygame.draw.line(window, 'red', (58, 118), (540, 118), 10)
    # pygame.draw.line(window, 'red', (58, 298), (540, 298), 10)
    # pygame.draw.line(window, 'red', (58, 478), (540, 478), 10)

    # pygame.draw.line(window, 'red', (56, 56), (540, 540), 10)
    # pygame.draw.line(window, 'red', (540, 56), (56, 540), 10)

    # Ф - запускаем цикл, который ловит нажатие клавишей и события мышки чтобы можно было что-нибудь с этой игрой делать
    for event in pygame.event.get():
        # Ф - если ловим событие мышкой на закрытие окна
        if event.type == pygame.QUIT:
            # Ф - делаем состояние игры False. Т.е. сбрасываем
            running = False

        # Ф - Добавил событие мышки клика
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ф - добавил событие отслежевания позиции курсора мыши 
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if (mouseX >= 40 and mouseX >= 40) and (mouseY <=200 and mouseY <= 200):
                # Ф - добавляем О в ячейку 1
                addImg("o",1)
                


    # Ф - метод который обнавляет события на экране
    pygame.display.update()

# Ф - выключаем и выходим из библиотеки pygame
pygame.quit()
