import pygame
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables


circle_x = 0
circle_y = 90
circle_radius = 30
circle_x_speed = 3
r = 4
g = 26
b = 64
sun_y = 280
bird_x = 0
bird_y = 130



# ---------------------------


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # GAME STATE UPDATES

    bird_x += 2

    if bird_x > WIDTH + 100:
        bird_x = -150



    circle_x += circle_x_speed

    if circle_x > WIDTH + circle_radius + 10:
        circle_x = -150

    if r <= 135:
        r += 2
    if g <= 206:
        g += 2
    if b <= 235:
        b += 2
    if sun_y <= 50:
       sun_y -= 3
    # DRAWING

    screen.fill((r, g, b))
    #night sky = (4,26,64)
    #morning sky = (135, 206, 235)

    #THE SUN
    pygame.draw.circle(screen, (255, 0, 0), (320, sun_y), circle_radius + 10)

    #BIRDS 
    for i in range(3):
        x = bird_x + i * 50
        y = bird_y + i * 15

        pygame.draw.line(screen, (0, 0, 0),
                     (x - 10, y + 5), (x, y), 3)

        pygame.draw.line(screen, (0, 0, 0),
                     (x, y), (x + 10, y + 5), 3)

    #Cloud #1
    pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), circle_radius + 10)
    pygame.draw.circle(screen, (255, 255, 255), (circle_x + 30, circle_y - 30), circle_radius + 20)
    pygame.draw.circle(screen, (255, 255, 255), (circle_x + 60, circle_y), circle_radius + 20)
    pygame.draw.circle(screen, (255, 255, 255), (circle_x + 90, circle_y - 20), circle_radius + 10)


    #Hill
    pygame.draw.circle(screen, (0,255,0), (320, 1020), 640)


    #House
    pygame.draw.rect(screen, (105, 105, 105) , (355, 200, 45, 100)) #
    pygame.draw.polygon(screen, (255 , 255 , 0), ((320, 200),(220, 280),(420, 280) )) #Roof
    pygame.draw.rect(screen, (245, 245, 220), (240, 280, 160, 120 )) #Wall
    pygame.draw.rect(screen, (0, 0, 0), (330, 300, 50, 50 )) # Window
    pygame.draw.line(screen, (255,255,255),(355,300),(355,350), width = 5 ) #Window line
    pygame.draw.line(screen, (255,255,255),(330,325),(380,325), width = 5 ) #Window line
    pygame.draw.rect(screen, (165, 42, 42) , (260, 300, 50, 100)) #Door
    pygame.draw.circle(screen, (255,255,0),(300,350),3) #Doorknob
    pygame.draw.circle(screen, (0, 0, 0) , (320,240) , 20) #Window_2
    pygame.draw.line(screen, (255, 255, 255) , (320,220) , (320,260), width = 5) #Window_2 line
    pygame.draw.line(screen, (255, 255, 255) , (300,240) , (340,240), width = 5) #Window_2 line


    #Trees - Trunks
    pygame.draw.rect(screen, (165, 42, 42) , (140, 320, 30, 100))
    pygame.draw.rect(screen, (165, 42, 42) , (40, 350, 30, 100))
    pygame.draw.rect(screen, (165, 42, 42) , (480, 320, 30, 100))
    pygame.draw.rect(screen, (165, 42, 42) , (580, 350, 30, 100))


    #Trees - Leaves
    pygame.draw.circle(screen, (0, 255, 0) , (55, 330) , 60)
    pygame.draw.circle(screen, (0, 255, 0) , (155, 300) , 60)
    pygame.draw.circle(screen, (0, 255, 0) , (495, 300) , 60)
    pygame.draw.circle(screen, (0, 255, 0) , (595, 330) , 60)
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------




pygame.quit()
