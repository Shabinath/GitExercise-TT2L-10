import random
import turtle
import tkinter as tk

wn = turtle.Screen()
wn.title("Maze Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

maze_width = 30
maze_height = 30
cell_size = 20

class Maze:
    def init(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[1] * width for _ in range(height)]
        self.visited = set()

        self.generate_maze(0, 0)

    def generate_maze(self, x, y):
        self.grid[y][x] = 0
        self.visited.add((x, y))
        neighbors = self.get_unvisited_neighbors(x, y)
        while neighbors:
            nx, ny = random.choice(neighbors)
            self.grid[ny][nx] = 0
            self.visited.add((nx, ny))
            if ny > y:
                self.grid[ny - 1][nx] = 0
            elif ny < y:
                self.grid[ny + 1][nx] = 0
            elif nx > x:
                self.grid[ny][nx - 1] = 0
            elif nx < x:
                self.grid[ny][nx + 1] = 0
            self.generate_maze(nx, ny)

    def get_unvisited_neighbors(self, x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in self.visited:
                neighbors.append((nx, ny))
        return neighbors

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    t.begin_fill()
                    t.fillcolor("black")
                    t.goto(x * self.cell_size, y * self.cell_size)
                    t.pendown()
                    for _ in range(4):
                        t.forward(self.cell_size)
                        t.left(90)
                    t.penup()
                    t.end_fill() 
class Player(turtle.Turtle):
    def init(self):
        super().init()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(0, 20)
        self.direction = "stop"

    def move(self):
        if self.direction == "up":
            self.sety(self.ycor() + cell_size)
        elif self.direction == "down":
            self.sety(self.ycor() - cell_size)
        elif self.direction == "left":
            self.setx(self.xcor() - cell_size)
        elif self.direction == "right":
            self.setx(self.xcor() + cell_size)

    def is_collision(self, maze):
        about_x = self.xcor() // cell_size

turtle.done()