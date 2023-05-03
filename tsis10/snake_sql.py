import psycopg2
import csv
import random
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SCORE = 0
flag = False

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake v0')
font_small = pygame.font.SysFont("Verdana", 20)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y, weight):
        self.location = Point(x, y)
        self.weight = weight

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
                pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
                scores = font_small.render(str(self.weight), True, BLACK)
                SCREEN.blit(scores, (self.location.x * BLOCK_SIZE + 15, self.location.y * BLOCK_SIZE + 7))





class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]
        self.score = 0

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE:
            head.x = 0
        elif head.x < 0:
            head.x = WIDTH // BLOCK_SIZE - 1
        elif head.y > HEIGHT // BLOCK_SIZE:
            head.y = 0
        elif head.y < 0:
            head.y = HEIGHT // BLOCK_SIZE - 1

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True
    
    def check_self_collision(self):
        for body in self.points[1:]:
            if self.points[0].x == body.x and self.points[0].y == body.y:
                return True
        return False

    def add_point(self):
        self.score += 1

    def display_score(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'Score: {self.score}', True, WHITE)
        SCREEN.blit(text, (10, 10))


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y), width=1)


respawn_food = pygame.USEREVENT + 1
pygame.time.set_timer(respawn_food, random.randint(5000, 10000))


conn = psycopg2.connect(database="postgres", user="postgres", password="494641", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            current_level INT DEFAULT 1
        );
    """)
conn.commit()

cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(id),
            level INT NOT NULL,
            score INT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
conn.commit()

username = input("Enter your username: ")

cur.execute("SELECT * FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    print(f"Welcome back, {username}! Your current level is {user[2]}.")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    print(f"Welcome, {username}! You are starting at level 1.")
def main():
    running = True
    


    level = user[2] if user else 1

    snake = Snake()
    food = Food(5, 5, random.randint(0, 10))
    dx, dy = 0, 0
    global SCORE
    counter = 0
    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == respawn_food: 
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                food.weight = random.randint(1, 10)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                global flag
                flag = True
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0
                elif event.key == pygame.K_p:
                    score = 1000
                    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user[0], level, score))
                    conn.commit()
                    print("Progress saved!")

            
        snake.move(dx, dy)
        if flag and snake.check_self_collision():
            running = False
            print("Game over - self collision!")
        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            SCORE += food.weight
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            food.weight = random.randint(1, 10)

        

        food.update()
        snake.update()
        draw_grid()

        

        font = pygame.font.SysFont(None, 25)
        score_text = font.render("Score: " + str(SCORE), True, WHITE)
        SCREEN.blit(score_text, (WIDTH - 100, 10))

        pygame.display.flip()
        clock.tick(5)

if __name__ == '__main__':
    main()