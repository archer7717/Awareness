import pygame,controls


def run():
    print("запуск Игры")
    pygame.init()
    screen  =   pygame.display.set_mode((800,800))
    pygame.display.set_caption("Awarnes")
    # цвет заднего фона
    bg_color = (0,0,0)
    gun = Gun(screen)
    
      #Добавление музыки
    # pygame.mixer.music.load("Часть_2/sound/background.ogg")
    # pygame.mixer.music.play()
    #Игровой цикл
    while True:
        controls.events(screen, gun, bullets)    # обрабатываем события нажатия клавиш ставим True или False
        gun.update_gun()        # если клавиша нажата смещаем космо аппарат
        controls.update(screen,gun,bg_color,bullets)
        controls.update_bullets(bullets)


run()
        


