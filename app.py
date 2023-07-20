import pygame

# включаем, запускаем pygame библиотеку
pygame.init()
# определяем размер екрана для игры
window = pygame.display.set_mode((800,800))
# определяем название для окна игры
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