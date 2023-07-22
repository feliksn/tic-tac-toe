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

# Ф - риусем наши картинки в окне игры
# Ф - передаем функции blit 2 параметра (саму кратинку, в скобках позицию картинок. координаты (x,y))

# E - расположение по координатам ноликов
window.blit(imgO, (48, 48))
window.blit(imgO, (230, 48))
window.blit(imgO, (410, 48))
window.blit(imgO, (48, 230))
window.blit(imgO, (230, 230))
window.blit(imgO, (410, 230))
window.blit(imgO, (48, 410))
window.blit(imgO, (230, 410))
window.blit(imgO, (410, 410))

# Е - расположение по координатам крестиков
window.blit(imgX, (48, 48))
window.blit(imgX, (230, 48))
window.blit(imgX, (410, 48))
window.blit(imgX, (48, 230))
window.blit(imgX, (230, 230))
window.blit(imgX, (410, 230))
window.blit(imgX, (48, 410))
window.blit(imgX, (230, 410))
window.blit(imgX, (410, 410))

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
