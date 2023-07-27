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
    # Используем функцию для получения координат картники по номеру, чтобы сформировать координаты ячеек
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
        # записываем в массив dictionary для формирования сетки игры с координатами
        result.append({
            "id": i,
            "x1": getCellPos(i)["x1"],
            "y1": getCellPos(i)["y1"],
            "x2": getCellPos(i)["x2"],
            "y2": getCellPos(i)["y2"]
        })
    return result

# Сравниваем позиции картинок с выигрышными позициям в игре
# Передаем аргумент массив с позициями которые были использованы определенной картинкой
def isWinnedPos(arr):
    posIndex = 0
    if len(arr) >= 3:
        for line in winnedLines:
            for pos in arr:
                if pos in line:
                    posIndex += 1
            if posIndex == 3:
                return True              
            else:
                posIndex = 0
    return False

# def getLineMap():
#     result = []
#     for i in range(1,7):
#         if i <= 3:
#             h = 
#             x1 = getImgPos(i)["x"]
#             y1 = getImgPos(i)["x"] + imgSize/2
#             x2 = getImgPos(i)["x"]
#             y2 = getImgPos(i)["x"]
#         if i > 3 and i <= 6:


#         result.append({
#             "id": i,
#             "x1": getImgPos(i)["x"],
#             "y1": getImgPos(i)["y"],
#             "x2": getImgPos(i)["x"],
#             "y2": getImgPos(i)["y"]
#         })

    # pg.draw.line(window, lineColor, (x1,y1), (x2,y2), lineWidth)


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
               
                # проверяем массив использованных позиций игры. Не была ли она ранее уже использована 
                if not cell["id"] in usedPos:
                    
                    # Если не была использована позиция, тогда сравниваем позицию курсора мышки с позицией каждой ячейки, чтобы знать в какую ячейку вставить картинку, по каким позициям
                    if mousePosX >= cell["x1"] and mousePosY >= cell["y1"] and mousePosX <= cell["x2"] and mousePosY <= cell["y2"]:
                        
                        # если номер ячейки не был использован то ее не будет в массиве usedPos и далее проверяем очередность добавления картинок
                        # если начинали с Х, то ходы в очередности 1,3,5,9 будут с Х 
                        if isXfirst:
                            # добавляем картинку Х по номеру ячейки
                            addImg("x", cell["id"])
                            # после того как добавилп Х в игру, записываем позицию Х в массив использованных позиций только для Х
                            usedPosX.append(cell["id"])
                            
                            # Сравниваем какие позиции были использованы Х с позициями выиграшными 
                            if isWinnedPos(usedPosX):
                                print("Game over! X wins!")
                            
                            # меняем значение переменой на False чтобы следующая картинка не повтрорялась и картинки чередовались
                            isXfirst = False
                        
                        # если начинали с Х, то ходы в очереди 2,4,6,8 в блоке else будут начинаться с О
                        else:
                            addImg("o", cell["id"])
                            usedPosO.append(cell["id"])
                            if isWinnedPos(usedPosO):
                                print("Game over! O wins!")
                            isXfirst = True
                        
                        # после того как добавили любую картинку, записываем в массив номер уже использованной позиции, чтобы не добавлять других картинок
                        usedPos.append(cell["id"])

    pg.display.update()

pg.quit()
