import math, datetime

import pygame
from math import *

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
clock = pygame.time.Clock()

def FindVerticesOfEquilateralTriangle(x0, y0, x, y):

    # Calculate the angle between the center and vertex
    theta1 = math.atan2(y - y0, x - x0)

    # Calculate the length of r using the formula we derived earlier
    r = math.sqrt((x - x0)**2 + (y - y0)**2) * 2 / math.sqrt(3)

    # Calculate the coordinates of the other two vertices using the polar coordinate formula
    # with angles of theta1 + 120 degrees and theta1 - 120 degrees
    x1 = x0 + r * math.cos(theta1 + math.radians(120))
    y1 = y0 + r * math.sin(theta1 + math.radians(120))
    x2 = x0 + r * math.cos(theta1 - math.radians(120))
    y2 = y0 + r * math.sin(theta1 - math.radians(120))

    # Return the coordinates of all three vertices
    return [(x, y), (x1, y1), (x2, y2)]



def find_square_vertices(center_x, center_y, vertex_x, vertex_y):
    # calculate the distance between the center and the vertex
    dist = ((vertex_x - center_x)**2 + (vertex_y - center_y)**2)**0.5

    # calculate the length of one edge
    E = dist * (2**0.5)

    # calculate the angle between the center and the vertex
    angle = math.atan2(center_y - vertex_y, vertex_x - center_x)

    # calculate the coordinates of the other three vertices
    V1 = (center_x + E / 2 * math.cos(angle - math.pi / 2), center_y - E / 2 * math.sin(angle - math.pi / 2))
    V2 = (center_x + E / 2 * math.cos(angle), center_y - E / 2 * math.sin(angle))
    V3 = (center_x + E / 2 * math.cos(angle + math.pi / 2), center_y - E / 2 * math.sin(angle + math.pi / 2))
    V4 = (center_x + E / 2 * math.cos(angle + math.pi), center_y - E / 2 * math.sin(angle + math.pi))

    return [V1, V2, V3, V4]



class GameObject:
    def draw(self):
        return 

    def handle(self):
        return


class Button:
    def __init__(self):
        pass

    def draw(self):

        self.rect = pygame.draw.rect(
            SCREEN,
            'black',
            (WIDTH // 2, 20, 40, 40),
            width = 10
        )
        self.rect2 = pygame.draw.rect(
            SCREEN,
            'red',
            (WIDTH // 2 + 40, 20, 40, 40),
            width = 10
        )
        self.rect3 = pygame.draw.rect(
            SCREEN,
            'blue',
            (WIDTH // 2 - 40, 20, 40, 40),
        )
        self.rect4 = pygame.draw.rect(
            SCREEN,
            'green',
            (WIDTH // 2 + 80, 20, 40, 40),
        )
        self.rect5 = pygame.draw.rect(
            SCREEN,
            'purple',
            (WIDTH // 2 - 80, 20, 40, 40),
        )
        self.rect6 = pygame.draw.rect(
            SCREEN,
            'purple',
            (WIDTH // 2 +120, 20, 40, 40),
        )
        self.rect7 = pygame.draw.rect(
            SCREEN,
            'yellow',
            (WIDTH // 2 - 120, 20, 40, 40),
        )
        self.switch_to_red = pygame.draw.rect(
            SCREEN,
            'red',
            (0, 0, 20, 20)
        )
        self.switch_to_blue = pygame.draw.rect(
            SCREEN,
            'blue',
            (0, 20, 20, 20)
        )
        self.switch_to_green = pygame.draw.rect(
            SCREEN,
            'green',
            (0, 40, 20, 20)
        )
        self.switch_to_black = pygame.draw.rect(
            SCREEN,
            'black',
            (0, 60, 20, 20)
        )
        self.eraser_rect = pygame.draw.rect(
            SCREEN,
            'black',
            (0, 80, 20, 20),
            width = 5
        )
class Pen(GameObject):
    def __init__(self, color, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]
        self.color = color

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=point,  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5,
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

class Circle(GameObject):
    def __init__(self, color, start_pos):
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        circle_center = self.start_pos
        Radius = (sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2))

        pygame.draw.circle(
            SCREEN,
            self.color,
            (self.start_pos[0], self.start_pos[1]),
            Radius,
            width = 5
        )
    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rectangle(GameObject):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width = 5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Equi(GameObject):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]

        end_pos_x = self.end_pos[0]
        end_pos_y = self.end_pos[1]

        pygame.draw.polygon(
            SCREEN,
            self.color,
            FindVerticesOfEquilateralTriangle(start_pos_x, start_pos_y, end_pos_x, end_pos_y)
            ,
            width = 5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class RightTriangle():
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        x = self.start_pos[0]
        y = self.start_pos[1]

        x1 = self.end_pos[0]
        y1 = self.end_pos[1]
        pygame.draw.polygon(
            SCREEN,
            self.color,
            ((x, y), (x1, y), (x1, y1)),
            width = 5
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Romb(GameObject):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]

        end_pos_x = self.end_pos[0]
        end_pos_y = self.end_pos[1]

        pygame.draw.polygon(
            SCREEN,
            self.color,
            ((start_pos_x + (end_pos_x-start_pos_x)/2, start_pos_y), (end_pos_x, start_pos_y + (end_pos_y-start_pos_y)/2),
             (start_pos_x + (end_pos_x-start_pos_x)/2, end_pos_y), (start_pos_x, start_pos_y + (end_pos_y-start_pos_y)/2))
            ,
            width = 5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


class Square(GameObject):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]

        end_pos_x = self.end_pos[0]
        end_pos_y = self.end_pos[1]

        pygame.draw.polygon(
            SCREEN,
            self.color,
            find_square_vertices(start_pos_x, start_pos_y, end_pos_x, end_pos_y)
            ,
            width = 5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos


def main():
    running = True
    active_obj = None
    button = Button()
    rect = pygame.Rect(0, 0, 800, 800)
    sub = SCREEN.subsurface(rect)

    objects = [
        button
    ]
    current_shape = 'pen'
    color = 'black'
    while running:
        SCREEN.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'rectangle'
                if button.rect2.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'pen'
                if button.rect3.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'circle'
                if button.rect4.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'square'
                if button.rect5.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'equi'
                if button.rect6.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'right'
                if button.rect7.collidepoint(pygame.mouse.get_pos()):
                    current_shape = 'romb'
                if button.switch_to_red.collidepoint(pygame.mouse.get_pos()):
                    color = 'red'
                if button.switch_to_blue.collidepoint(pygame.mouse.get_pos()):
                    color = 'blue'
                if button.switch_to_green.collidepoint(pygame.mouse.get_pos()):
                    color = 'green'
                if button.switch_to_black.collidepoint(pygame.mouse.get_pos()):
                    color = 'black'
                if button.eraser_rect.collidepoint(pygame.mouse.get_pos()):
                    color = 'white'
                    current_shape = 'pen'
                else:
                    if current_shape == 'pen':
                        active_obj = Pen(color, start_pos=event.pos)
                    elif current_shape == 'rectangle':
                        active_obj = Rectangle(color, start_pos=event.pos)
                    elif current_shape == 'square':
                        active_obj = Square(color, start_pos=event.pos)
                    elif current_shape == 'circle':
                        active_obj = Circle(color, start_pos=event.pos)
                    elif current_shape == 'equi':
                        active_obj = Equi(color, start_pos=event.pos)
                    elif current_shape == 'right':
                        active_obj = RightTriangle(color, start_pos=event.pos)
                    elif current_shape == 'romb':
                        active_obj = Romb(color, start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                # active_obj.points.append(pygame.mouse.get_pos())
                active_obj.handle(mouse_pos=pygame.mouse.get_pos())
                # active_obj.points => raise
                active_obj.draw()

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None
        for obj in objects:
            obj.draw()

        clock.tick(45)
        pygame.display.flip()


if __name__ == '__main__':
    main()