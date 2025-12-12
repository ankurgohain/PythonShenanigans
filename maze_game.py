import random
import pygame
import tkinter as tk
from tkinter import simpledialog

def generate_solvable_maze(width, height):
    # Initialize the maze with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Recursive backtracking to carve out a solvable path
    def carve_path(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                maze[y + dy][x + dx] = ' '  # Carve path
                maze[ny][nx] = ' '
                carve_path(nx, ny)

    # Ensure the maze is fully connected
    def connect_unreachable():
        for y in range(1, height, 2):
            for x in range(1, width, 2):
                if maze[y][x] == '#':
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == ' ':
                            if 0 <= y - dy < height and 0 <= x - dx < width:
                                maze[y][x] = ' '
                                maze[y - dy][x - dx] = ' '
                            break

    # Start carving from the top-left corner
    maze[0][0] = 'S'
    carve_path(0, 0)
    connect_unreachable()
    maze[height - 1][width - 1] = 'E'
    return maze

def generate_maze(width, height):
    return generate_solvable_maze(width, height)

def draw_maze(screen, maze, cell_size):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = (0, 0, 0) if cell == '#' else (255, 255, 255)
            if cell == 'S':
                color = (0, 255, 0)
            elif cell == 'E':
                color = (255, 0, 0)
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

def player_design_maze(width, height):
    print("Design your maze. Use '#' for walls and ' ' for paths.")
    maze = []
    for i in range(height):
        row = input(f"Row {i + 1}/{height}: ")
        maze.append(list(row))
    return maze

def move_player(maze, player_pos, direction):
    x, y = player_pos
    if direction == 'UP' and y > 0 and maze[y - 1][x] != '#':
        y -= 1
    elif direction == 'DOWN' and y < len(maze) - 1 and maze[y + 1][x] != '#':
        y += 1
    elif direction == 'LEFT' and x > 0 and maze[y][x - 1] != '#':
        x -= 1
    elif direction == 'RIGHT' and x < len(maze[0]) - 1 and maze[y][x + 1] != '#':
        x += 1
    return x, y

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    mode = simpledialog.askstring("Maze Game", "Choose a mode:\n1. Computer generates a maze for you to solve.\n2. You design a maze for the computer to solve.")

    if mode == '1':
        width = simpledialog.askinteger("Maze Dimensions", "Enter maze width:")
        height = simpledialog.askinteger("Maze Dimensions", "Enter maze height:")
        maze = generate_maze(width, height)

        pygame.init()
        cell_size = 20
        screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Maze Game")

        player_pos = (0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        player_pos = move_player(maze, player_pos, 'UP')
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        player_pos = move_player(maze, player_pos, 'DOWN')
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        player_pos = move_player(maze, player_pos, 'LEFT')
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        player_pos = move_player(maze, player_pos, 'RIGHT')

            screen.fill((0, 0, 0))
            draw_maze(screen, maze, cell_size)
            pygame.draw.rect(screen, (0, 0, 255), (player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size))
            pygame.display.flip()

        pygame.quit()

    elif mode == '2':
        width = simpledialog.askinteger("Maze Dimensions", "Enter maze width:")
        height = simpledialog.askinteger("Maze Dimensions", "Enter maze height:")
        maze = player_design_maze(width, height)

        pygame.init()
        cell_size = 20
        screen = pygame.display.set_mode((width * cell_size, height * cell_size))
        pygame.display.set_caption("Maze Game")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            draw_maze(screen, maze, cell_size)
            pygame.display.flip()

        pygame.quit()

    else:
        print("Invalid choice. Exiting game.")

if __name__ == "__main__":
    main()