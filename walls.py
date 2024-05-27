#Roldie Olsim and Hannah Buizon
#References: http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py


import pygame
import sys
from os import system
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
#Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([25, 25])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        if 540<self.rect.x<600 and 580<self.rect.y<610:
            #ctypes.windll.user32.MessageBoxW(0,"You  win","Wow",1)
            system("osascript -e 'Tell application \"System Events\" to display dialog\""+"You Win!"+"\"'")
            sys.exit("Win!")
            
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Maze Thingy')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

#left wall
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

#up wall
wall = Wall(10, 0, 590, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

#right wall
wall = Wall(590, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

#down wall
wall = Wall(10, 590, 535, 590)
wall_list.add(wall)
all_sprite_list.add(wall)

#other walls
wall = Wall(320, 10, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(320, 300, 10, 590)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(165, 50, 10, 110)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 300, 150, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 300, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(325, 100, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 150, 200, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 150, 10, 75)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 50, 165, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 50, 10, 140)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(215, 50, 115, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 50, 125, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(535, 50, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(535, 150, 75, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 150, 75, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 100, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 225, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(325, 225, 10, 40)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 225, 10, 85)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 225, 10, 125)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 350, 10, 150)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 550, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 500, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 500, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 385, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 225, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 190, 120, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(165, 190, 210, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 190, 75, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 100, 175, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 100, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 225, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 225, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(325, 260, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 260, 70, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(535, 200, 10, 35)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(535, 265, 10, 130)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 385, 70, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(325, 385, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(375, 500, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(545, 500, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 550, 120, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(425, 455, 120, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(535, 455, 10, 55)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(475, 385, 10, 35)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(545, 420, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 100, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 225, 10, 80)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(220, 150, 10, 120)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(125, 225, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(115, 225, 10, 45)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 300, 175, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 350, 225, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(165, 270, 10, 35)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 400, 220, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(220, 300, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(270, 350, 10, 100)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 445, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 515, 155, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 480, 60, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 410, 10, 70)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(165, 440, 10, 115)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 560, 10, 35)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(50, 560, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(275, 485, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(230, 440, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(230, 535, 50, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(280, 535, 10, 60)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(230, 450, 10, 90)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(200, 550, 10, 50)
wall_list.add(wall)
all_sprite_list.add(wall)



# Create the player paddle object
player = Player(10, 10)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Hello, World", True, BLACK)
done = False
 #540,590
while not done:
 
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 5)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -5)
                
 
    all_sprite_list.update()
 
    screen.fill(WHITE)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
