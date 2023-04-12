import collections

import pygame
import math

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self, dist, color):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            color,
            (
                dist,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self, dist, color):
        pygame.draw.rect(
            SCREEN,
            color,
            (
                dist,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point] = []  # [(x1, y1), (x2, y2)]

    def draw(self, *args, **kwargs):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)



class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self, *args, **kwargs):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self,  *args, **kwargs):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.circle(
            SCREEN,
            WHITE,
            (
                start_pos_x, start_pos_y,
            ),
            math.sqrt((end_pos_y - start_pos_y)**2 + (end_pos_x - start_pos_x)**2),           
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Rhombus(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self,  *args, **kwargs):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE,
            (
                (start_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
                (start_pos_x + (end_pos_x - start_pos_x) // 2, start_pos_y)
            ),           
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Equilateral_Triangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self,  *args, **kwargs):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE,
            (
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y),
                (start_pos_x, start_pos_y)
            ),           
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Right_Triangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self,  *args, **kwargs):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            WHITE,
            (
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y),
                (start_pos_x, start_pos_y)
            ),           
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen
    button_rect = Button(dist = 20, color = 50)
    button_circle = Button(dist = 80, color = 70)
    button_pen = Button(dist = 140, color = 90)
    button_rhombus = Button(dist = 200, color = 110)
    button_equilateral_triangle = Button(dist = 260, color = 130)
    button_right_triangle = Button(dist = 320, color = 150)
    objects = [
        button_rect, button_circle, button_pen, button_rhombus, button_equilateral_triangle, button_right_triangle
    ]

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                if button_circle.rect.collidepoint(event.pos):
                    current_shape = Circle
                if button_pen.rect.collidepoint(event.pos):
                    current_shape = Pen
                if button_rhombus.rect.collidepoint(event.pos):
                    current_shape = Rhombus
                if button_equilateral_triangle.rect.collidepoint(event.pos):
                    current_shape = Equilateral_Triangle
                if button_right_triangle.rect.collidepoint(event.pos):
                    current_shape = Right_Triangle
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object

        for number, obj in enumerate(objects):
            obj.draw(dist = 20 + number*60, color = (0,  50 + number * 20, 0))

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()