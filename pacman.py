# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Load images ##
pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)

class PacMan:
    # Constructor
    # pacman=PacMan(100,100)
    def __init__(self,x,y):
        self.x = x # attribute
        self.y = y # attribute
        print("Hello from init", x, y)

    def move(self, new_direction):
        if new_direction == "left":
            self.x -= 5
        if new_direction == "right":
            self.x += 5
        if new_direction == "up":
            self.y -= 5
        if new_direction == "down":
            self.y += 5

    def draw(self,screen):
        pg.draw.circle(screen, (220,220,0), 
                       (self.x,self.y), 16)

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man")
pg.display.set_icon(pacman_images[1])

# Creating a PacMan object
pacman = PacMan(100,100)
#pacman2 = PacMan(200,200)

direction = None
running = True
tick = 0
while running:

    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            if event.key == pg.K_RIGHT:
                direction = "right"
            if event.key == pg.K_UP:
                direction = "up"
            if event.key == pg.K_DOWN:
                direction = "down"
            if event.key == pg.K_ESCAPE:
                pass
    
    # Logic
    pacman.move(direction)
    #pacman2.move()

    screen.fill("black")

    # Draw
    pacman.draw(screen)
    #pacman2.draw(screen)
    print("pacman.x", pacman.x)
    print("pacman.y", pacman.y)
    #print("pacman2.x", pacman2.x)
    #print("pacman2.y", pacman2.y)
    
    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)