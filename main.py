import pygame, sys, random
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size, cell_size, cell_size)
        #screen.blit(apple, fruit_rect)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_num-1)
        self.y = random.randint(0,cell_num-1)
        self.pos = Vector2(self.x,self.y)

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]  
        self.direction = Vector2(1,0)
        self.new_block = False
        self.score = 0

    def draw_snake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size) 
            pygame.draw.rect(screen,(183,111,122),body_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.score += 1
        else: 
            body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+ self.direction)
        self.body = body_copy[:]
        self.new_block = False

    def add_block(self):
        self.new_block = True

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_death()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_death(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
            

pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num*cell_size,cell_num*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("Graphics/apple.png").convert_alpha()

main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            s = main_game.snake
            if event.key == pygame.K_UP:
                if not s.direction == Vector2(0,1): 
                    main_game.snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_LEFT:
                if not s.direction == Vector2(1,0):
                    main_game.snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_DOWN:
                if not s.direction == Vector2(0,-1):
                    main_game.snake.direction = Vector2(0,1)
            elif event.key == pygame.K_RIGHT:
                if not s.direction == Vector2(-1,0):
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)