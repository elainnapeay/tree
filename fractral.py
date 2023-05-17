#https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Frac Tree")
screen = pygame.display.get_surface()


x1 = 300
y1 = 600
angle = -90
depth = 9

def drawTree(x1, y1, angle, depth):
    fork_angle = 20
    base_len = 10.0
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle))* depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle))*depth * base_len)
        pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - fork_angle, depth -1)
        drawTree(x2, y2, angle + fork_angle, depth -1)

def input(event):
    if event.type == pygame.QUIT:
	    exit(0)

pygame.display.flip()

clock = pygame.time.Clock()
while True:
     for event in pygame.event.get():
        input(event)

        screen.fill((0, 0, 0))
        y1 -= 1
        drawTree(x1,y1,angle,depth)
        pygame.display.update()
        clock.tick(60)
