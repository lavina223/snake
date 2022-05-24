import pygame
import random

w, h = 900, 900
screen = pygame.display.set_mode((w,h))
screen
size = 90
fps = pygame.time.Clock()

class Gameobject:
    def __init__(self, x, y, color):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)

class Snake(Gameobject):
    speed_x = size
    speed_y = 0
    timer = 0
    def move(self):
        if self.timer == 0:    
            self.hitbox.x += self.speed_x
            self.hitbox.y += self.speed_y
            self.timer = 15
        self.timer -= 1
    def control(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_w]:
            self.speed_x = 0
            self.speed_y = -size
        if keys [pygame.K_s]:
            self.speed_x = 0
            self.speed_y = size
        if keys [pygame.K_a]:
            self.speed_x = -size
            self.speed_y = 0
        if keys [pygame.K_d]:
            self.speed_x = size
            self.speed_y = 0

food = Gameobject(size*random.randrange(w//size),size* random.randrange(h//size), (100,210, 0))
snake = Snake(0,0, (0,255,0))

while True:
    screen.fill((50,200,255))
    event_list = pygame.event.get()
    for event in event_list:    
        if event.type == pygame.QUIT:
           pygame.QUIT()
           break
    screen.blit(food.image, food.hitbox)
    screen.blit(snake.image, snake.hitbox)
    snake.move()
    snake.control()
    pygame.display.update()
    fps.tick(25) 