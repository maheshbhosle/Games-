#Turtle-Rabbit race
import pygame

#initialize pygame
pygame.init()

#create window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Turtle vs Rabbit')

#clock and FPS
FPS = 30
clock = pygame.time.Clock()

#colors
GRASS = pygame.Color(181, 230, 29)
RED = pygame.Color(255,0,0)
DARK_GREEN = pygame.Color(18,95,41)


#coords
start_line_point1 = (64,0)
start_line_point2 = (64,WINDOW_HEIGHT)

stop_line_point1 = (WINDOW_WIDTH-64,0)
stop_line_point2 = (WINDOW_WIDTH-64, WINDOW_HEIGHT)

# contestents
rabbit = pygame.image.load('d:/rabbit.png')
rabbit_rect = rabbit.get_rect()
rabbit_rect.right = 64
rabbit_rect.centery = WINDOW_HEIGHT // 3

turtle = pygame.image.load('d:/turtle.png')
turtle_rect = turtle.get_rect()
turtle_rect.right = 64
turtle_rect.centery = WINDOW_HEIGHT - WINDOW_HEIGHT // 3

#game values
game_status = 0 #about to start
turtle_velcoity = 30
rabbit_velocity = 5
count_down = 100

#sound
gunshot = pygame.mixer.Sound('d:/music/free/gunshot.wav')

#define the life of the game (main game loop)
running = True

while running:
    if game_status == 0:
        count_down-=1
    if count_down == 0 :
        gunshot.play()
        game_status = 1
        count_down = -1

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN: #some key got pressed
            if ev.key == pygame.K_RIGHT and game_status==1: #right arrow key
                turtle_rect.right += turtle_velcoity
            elif ev.key == pygame.K_r and game_status ==2: # to restart the game
                turtle_rect.right = 64
                turtle_rect.centery = WINDOW_HEIGHT - WINDOW_HEIGHT//3
                rabbit_rect.right = 64
                rabbit_rect.centery = WINDOW_HEIGHT // 3
                game_status = 0
                count_down = 100

    if (rabbit_rect.right > WINDOW_WIDTH - 64 or turtle_rect.right > WINDOW_WIDTH -64) and game_status == 1:
        game_status = 2
        gunshot.play()

    #pour the grass color on the display surface
    display_surface.fill(GRASS)

    #draw the lines
    pygame.draw.line(surface=display_surface, color=DARK_GREEN, start_pos=start_line_point1, end_pos=start_line_point2, width=5)
    pygame.draw.line(surface=display_surface, color=RED, start_pos= stop_line_point1, end_pos= stop_line_point2, width=5)

    if game_status == 1:
        rabbit_rect.right+=  rabbit_velocity

    #blit the contestents
    display_surface.blit(source=rabbit, dest=rabbit_rect)
    display_surface.blit(source=turtle, dest=turtle_rect)

    #refresh the display
    pygame.display.update()
    #moderate the rate of loop iteration (achieve cooperative multitasking)
    #game runs at the same speed across different processors
    clock.tick(FPS)


#deallocate
pygame.quit()