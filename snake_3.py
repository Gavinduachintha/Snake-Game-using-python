#snake_2.py is the complete game.
#This version has the apple effect and the score functions

import pygame
import random
import time

pygame.init()

width = 720
height = 480
snake_color = (173,216,153)  # Snake color
fruit_color = (226,183,233) #Fruit color
background_color = (90, 99, 159)

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)


direction = 'RIGHT'
change_to = direction

# Load the image and set the caption
pygame.display.set_caption("Snake")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode([width, height])

#Snake Position
snake_position = [100, 50]  # Defining the snake position
snake_body = [[100, 50], [90, 50], [80, 50], [70,50]]  # Define a 4-block snake

#Fruit Position
fruit_position = [random.randrange(1,(width//10))*10, random.randrange(1,(height//10))*10]
fruit_spawn = True

score = 0
font = pygame.font.SysFont('Arial',35)

def showScores():
    score_text = font.render('Score:{score}', True, (255,255,255))
    screen.blit(score_text,[0,0])




running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key ==pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    elif change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to

    if direction == 'UP':
        snake_position[1]-=10
    elif direction == 'DOWN':
        snake_position[1]+=10
    elif direction == 'LEFT':
        snake_position[0]-=10
    elif direction == 'RIGHT':
        snake_position[0]+=10

    snake_body.insert(0,list(snake_position))
    #snake_body.pop()

    #Collision with boundaries
    if (snake_position[0] < 0 or snake_position[0] >= width) or (snake_position[1] < 0 or snake_position[1] >= height):
        running = False
        print("Game Over")
    
    #COllision with it self
    for block in snake_body[1:]:
        if snake_position == block:
            running = False
            print("Game Over")
    if snake_position == fruit_position:
        score +=1


    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1,(width//10))*10, random.randrange(1,(height//10))*10]
        fruit_spawn = True

        

    # Fill the screen with background color
    screen.fill(background_color)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, fruit_color,pygame.Rect(fruit_position[0],fruit_position[1],10,10))
    
    showScores()
    pygame.display.flip()
    clock.tick(15)
    

pygame.quit()
