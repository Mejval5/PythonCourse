import pygame
import random

snake_color = (52, 97, 235)
dilek_color = (235, 104, 52)
background_color = (143, 235, 52)

clock = pygame.time.Clock()

sirka_obrazovky = 400
vyska_obrazovky = 300

pygame.init()
dis=pygame.display.set_mode((sirka_obrazovky, vyska_obrazovky))
pygame.display.set_caption('Hrani si s hadikem')
pygame.display.update()

x_dilek = 100
y_dilek = 120

x_velocity = 0
y_velocity = 0
x_position = 200
y_position = 150

velikost_hada = 10
velikost_dilku = 10
rychlost_hada = 4

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_velocity = - rychlost_hada
                y_velocity = 0
            elif event.key == pygame.K_RIGHT:
                x_velocity = rychlost_hada
                y_velocity = 0
            elif event.key == pygame.K_UP:
                x_velocity = 0
                y_velocity = - rychlost_hada
            elif event.key == pygame.K_DOWN:
                x_velocity = 0
                y_velocity = rychlost_hada
            
    x_position += x_velocity
    y_position += y_velocity
    
    max_vzdalenost = (velikost_hada + velikost_dilku)/2
    x_podminka = max_vzdalenost > abs((x_dilek + velikost_dilku/2) - (x_position + velikost_hada/2))
    y_podminka = max_vzdalenost > abs((y_dilek + velikost_dilku/2) - (y_position + velikost_hada/2))
    
    if x_podminka and y_podminka:
        x_dilek = random.randint(velikost_dilku * 2, sirka_obrazovky - velikost_dilku * 2)
        y_dilek = random.randint(velikost_dilku * 2, vyska_obrazovky - velikost_dilku * 2)
        velikost_hada += 5
        rychlost_hada += 1
        
    dotek_steny_x = x_position < 0 or x_position + velikost_hada > sirka_obrazovky
    dotek_steny_y = y_position < 0 or y_position + velikost_hada > vyska_obrazovky
    
    if dotek_steny_x or dotek_steny_y:
        x_dilek = 100
        y_dilek = 120

        x_velocity = 0
        y_velocity = 0
        x_position = 200
        y_position = 150

        velikost_hada = 10
        velikost_dilku = 10
        rychlost_hada = 4
        
    dis.fill(background_color)
    pygame.draw.rect(dis, dilek_color, [x_dilek, y_dilek, velikost_dilku, velikost_dilku])
    pygame.draw.rect(dis, snake_color, [x_position, y_position, velikost_hada, velikost_hada])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()