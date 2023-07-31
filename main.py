import pygame
import random

pygame.init()
# color
green=(174, 235, 52)
black=(15, 14, 6)
red=(245, 66, 66)

screen_hight=600
screen_widht=800
gamewindow= pygame.display.set_mode((screen_widht,screen_hight))
pygame.display.set_caption("Snake Game")
pygame.display.update()

#Game specific variebeles

clock=pygame.time.Clock()
font=pygame.font.SysFont("Verdana",25)



def score_screen(text , color , x , y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow, color,snk_list,snake_size):
    for x,y in snk_list:
         pygame.draw.rect(gamewindow, black, [x,y,snake_size, snake_size])

def Game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    snk_list = []
    snk_length = 1
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    food_x = random.randint(20, screen_widht / 2)
    food_y = random.randint(20, screen_hight / 2)
    velocity_x = 0
    velocity_y = 0
    score = 0
    fps = 30
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
               f.write(str(highscore))

            gamewindow.fill(green)
            score_screen("Game Over! Press Enter to Continue", red,180,200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Game_loop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game= True

                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x= 10
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x= -10
                        velocity_y=0
                    if event.key == pygame.K_DOWN:
                        velocity_y= 10
                        velocity_x=0
                    if event.key == pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
                score += 10
                food_x = random.randint(20, screen_widht / 2)
                food_y = random.randint(20, screen_hight / 2)
                snk_length +=4

                if score>int(highscore):
                    highscore=score



            gamewindow.fill(green)
            score_screen("Score:" + str(score) + " HighScore:"+ str(highscore), black, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_length:
                del snk_list[0]


            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_widht or snake_y<0 or snake_y>screen_hight:
                game_over = True
        plot_snake(gamewindow,black ,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
Game_loop()