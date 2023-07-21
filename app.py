import pygame

# включаем, запускаем pygame библиотеку
pygame.init()

# Ф - определяем переменные для размера экрана.
# Делаем это для того чтобы создавать другие элементы, размеры которых будут зависить от размера экрана игры
windowWidth = 600
windowHeight = 600

# Ф - определяем размер екрана для игры
window = pygame.display.set_mode((windowWidth, windowHeight))

# Ф - определяем название для окна игры
pygame.display.set_caption("Крестики Нолики")
# тут определяем состояние игры для дальнейшей передачи в цикл ниже
running = True

# запускаем цикл игры
while running:
    # запускаем цикл, который ловит нажатие клавишей и события мышки чтобы можно было что-нибудь с этой игрой делать
    for event in pygame.event.get():
        # если ловим событие мышкой на закрытие окна  
        if event.type==pygame.QUIT:
            # делаем состояние игры False
            running = False
    
    # определяем цвет окна
    window.fill("white")
    # метод который обнавляет события на экране
    pygame.display.flip()
    
# выключаем и выходим из библиотеки pygame
pygame.quit()