import time

import pygame
import random

pygame.init()

runned = True

WIDTH, HEIGHT, BLOCK = 700, 700, 50
# the dimension of the screen and the size of each snake body block

clock = pygame.time.Clock()

dx, dy = 0, 0
# variables for moving the snake

x = 5
# FPS

level = 1
# responsible for the difficulity of the game

saved_lenght = 0
# information about the length(number of blocks added to the head)

SCREEN = pygame.display.set_mode((HEIGHT, WIDTH))

all_font = pygame.font.SysFont("Italic", 50)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    snakebody = []

    # saves the blocks of the snake
    def __init__(self):
        self.snakebody = [(Point(x=HEIGHT // 2 // BLOCK, y=WIDTH // 2 // BLOCK))]
        self.dead = 0
        # var in case snake crosses the border

    def draw(self):
        snake_head = self.snakebody[0]
        x_block_head = snake_head.x * BLOCK
        y_block_head = snake_head.y * BLOCK

        pygame.draw.rect(SCREEN, (0, 255, 0), pygame.Rect(x_block_head, y_block_head, BLOCK, BLOCK))
        # draws the head of the snake
        for body in self.snakebody[1:]:
            x_block_body = body.x * BLOCK
            y_block_body = body.y * BLOCK
            pygame.draw.rect(SCREEN, (0, 225, 100), pygame.Rect(x_block_body, y_block_body, BLOCK, BLOCK))
            # for loop for iterating trough the list and drawing all the body blocks

    def move(self, dx, dy):
        for inx in range(len(self.snakebody) - 1, 0, -1):
            self.snakebody[inx].x = self.snakebody[inx - 1].x
            self.snakebody[inx].y = self.snakebody[inx - 1].y
        self.snakebody[0].x += dx
        self.snakebody[0].y += dy
        if self.snakebody[0].x >= HEIGHT // BLOCK:
            self.dead = 1
        elif self.snakebody[0].x < 0:
            self.dead = 1
        elif self.snakebody[0].y >= WIDTH // BLOCK:
            self.dead = 1
        elif self.snakebody[0].y < 0:
            self.dead = 1

    def collision(self, foodx, foody):
        if foodx == self.snakebody[0].x and foody == self.snakebody[0].y:
            return True
        # checks if the food collides with the head
        return False


class Food:
    def __init__(self):
        self.x = random.randint(0, HEIGHT // BLOCK - 1)
        self.y = random.randint(0, WIDTH // BLOCK - 1)
        # generates a random spawnpoint for a food block

    def draw(self):
        pygame.draw.rect(SCREEN, (200, 0, 0),
                         pygame.Rect(self.x * BLOCK + BLOCK // 2 - 10, self.y * BLOCK + BLOCK // 2 - 10, BLOCK / 2,
                                     BLOCK / 2))
        # draws the food in randomnly generated position


snake = Snake()
food = Food()
while runned:
    SCREEN.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runned = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0
            elif event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            # getting the input and changing the dx, dy variables
    snake.move(dx, dy)
    food.draw()
    for i in range(1, len(snake.snakebody)):
        if snake.collision(snake.snakebody[i].x, snake.snakebody[i].y):
            runned = False
        # checks if snake made collision with itself
    if snake.dead == 1:
        runned = False
        # checks if snake crossed the border
    snake.draw()
    level_see = all_font.render(f"level: {level}", True, (255, 255, 255))
    score_see = all_font.render(f"score: {len(snake.snakebody)}", True, (255, 255, 255))
    # the number of collected points and the level
    SCREEN.blit(level_see, (0, 0))
    SCREEN.blit(score_see, (HEIGHT - 150, 0))
    if snake.collision(food.x, food.y):
        snake.snakebody.append(Point(food.x, food.y))
        food.x = random.randint(0, HEIGHT // BLOCK - 1)
        food.y = random.randint(0, WIDTH // BLOCK - 1)
    # check if snake collided with food and increase the score if it did
    if len(snake.snakebody) % 5 == 0 and saved_lenght != len(snake.snakebody):
        x += 1
        saved_lenght = len(snake.snakebody)
        level += 1

    pygame.display.flip()
    clock.tick(x)
