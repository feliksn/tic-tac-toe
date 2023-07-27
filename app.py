import pygame as pg
# import numpy as np

pg.init()

# Определяем настройки игры
gameName = "Крестики-нолики"
gameBg = "#ffffff"
gameWidth = 600
gameHeight = 600
imgSize = 140
imgMargin = 10
tableSize = 600
tableBorder = 40
cellBorder = 20
lineWidth = 10
lineColor = "#ffff00"
isGameRunning = True
isXfirst = True
usedPos = []
usedPosX = []
usedPosO = []
winnedLines = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,4,7],
    [2,5,8],
    [3,6,9],
    [1,5,9],
    [3,5,7]
]

pg.display.set_caption(gameName)
window = pg.display.set_mode((gameWidth, gameHeight))
window.fill(gameBg)

# Ф - Функция возвращает координаты картинки по переданному ей аргументу(номеру ячейки)Т.е.  
def getImgPos(index):
    for i in range(9):
        if i == 0:
            marginsX = marginsY = 1
            cellBordersX = cellBordersY = imgSizesX = imgSizesY = 0
        elif i % 3 == 0:
            marginsX = 1
            cellBordersX = imgSizesX = 0
            marginsY += 2
            cellBordersY += 1
            imgSizesY += 1
        else:
            marginsX += 2
            cellBordersX += 1
            imgSizesX += 1

        if i == index-1:
            x = tableBorder + marginsX*imgMargin + cellBordersX*cellBorder + imgSizesX*imgSize
            y = tableBorder + marginsY*imgMargin + cellBordersY*cellBorder + imgSizesY*imgSize
            return {"x":x, "y":y}

# Добавление картинки в игру по аргументам(имя картинки, позиция ячейки)
def addImg(name, index=False):
    img = pg.image.load("images/{}.png".format(name))
    if index:
        pos = getImgPos(index)
    else:
        pos = {"x": 0, "y": 0}
    window.blit(img, (pos["x"], pos["y"]))

# Получение позиции ячейки по ее номеру в аргументе
def getCellPos(index):
    imgPos = getImgPos(index)
    x1 = imgPos["x"] - imgMargin
    y1 = imgPos["y"] - imgMargin
    x2 = imgPos["x"] + imgSize + imgMargin
    y2 = imgPos["y"] + imgSize + imgMargin
    return {
        "x1":x1,
        "y1":y1,
        "x2":x2,
        "y2":y2
    }

# Получение сетки игры с координатами ячеек. Возращаем Номер ячейки и ее координаты
def getCellMap():
    result = []
    for i in range(1,10):
        result.append({
            "id": i,
            "coords": getCellPos(i)
        })
    return result

# Пока игра запущенна, выполняем код внутри цикла
while isGameRunning:
    addImg("g")
    
    # pygame.draw.line(window, 'red', (118, 58), (118, 540), 10)
    # pygame.draw.line(window, 'red', (298, 58), (298, 540), 10)
    # pygame.draw.line(window, 'red', (478, 58), (478, 540), 10)

    # pygame.draw.line(window, 'red', (58, 118), (540, 118), 10)
    # pygame.draw.line(window, 'red', (58, 298), (540, 298), 10)
    # pygame.draw.line(window, 'red', (58, 478), (540, 478), 10)

    # pygame.draw.line(window, 'red', (56, 56), (540, 540), 10)
    # pygame.draw.line(window, 'red', (540, 56), (56, 540), 10)
    
    for event in pygame.event.get():
        

# Пока игра запущенна, выполняем код внутри цикла
while isGameRunning:
    addImg("g")
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            isGameRunning = False
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            # записываем в переменные позиции х,у мышки после нажатия
            mousePosX = pg.mouse.get_pos()[0]
            mousePosY = pg.mouse.get_pos()[1]
            # получаем сетку игры с координатами ячеек и записываем ее в переменную, которая являеться массивом
            cellMap = getCellMap()
            # создаем цикл котором будем получать данные о номере ячейки и ее кодинатах в каждом повторении
            for cell in cellMap:
                # сравниваем позицию курсора мышки с позицией каждой ячейки
                if mousePosX >= cell["coords"]["x1"] and mousePosY >= cell["coords"]["y1"] and mousePosX <= cell["coords"]["x2"] and mousePosY <= cell["coords"]["y2"]:
                    # когда курсор ячейки находиться в 1 из 9 позиций ячейки, проверяем массив использованных позиций игры. Т.е. проверяем номер ячейки где находиться курсор с массивом использованных позиций. Не была ли она ранее уже использована 
                    if not cell["id"] in usedPos:
                        # если номер ячейки не был использован то ее не будет в массиве usedPos и далее проверяем очередность добавления картинок
                        # если начинали с Х, то ходы в очередности 1,3,5,9 будут с Х 
                        if isXfirst:
                            # добавляем картинку Х по номеру ячейки
                            addImg("x", cell["id"])
                            # меняем значение переменой на False чтобы следующая картинка не повтрорялась и картинки чередовались
                            isXfirst = False
                        # если начинали с Х, ходы 2,4,6,8 в данном блоке будут с О
                        # eсли в начале файла поменять isXfirst=False то игра будет начинаться с О
                        else:
                            addImg("o", cell["id"])
                            isXfirst = True
                        # после того как добавили любую картинку, записываем в массив номер уже использованной позиции, чтобы не добавлять других картинок
                        usedPos.append(cell["id"])

    pg.display.update()

pg.quit()
