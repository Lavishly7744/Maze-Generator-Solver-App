import random

# Directions for moving in the maze (Up, Down, Left, Right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [['#' for _ in range(width)] for _ in range(height)]

    def generate(self):
        start = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
        self._dfs(start[0], start[1])
        return self.maze

    def _dfs(self, x, y):
        self.maze[x][y] = ' '  # Mark cell as open
        random.shuffle(DIRECTIONS)  # Randomize directions
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # Check bounds and whether the cell is surrounded by walls
            if 1 <= nx < self.height - 1 and 1 <= ny < self.width - 1 and self.maze[nx][ny] == '#':
                # Ensure we're not making loops (surrounding cells must be walls)
                if sum([self.maze[nx + dx][ny + dy] == ' ' for dx, dy in DIRECTIONS]) == 1:
                    self._dfs(nx, ny)

    def print_maze(self):
        for row in self.maze:
            print(''.join(row))

# Main to generate the maze
if __name__ == "__main__":
    width = int(input("Enter maze width: "))
    height = int(input("Enter maze height: "))
    maze_gen = MazeGenerator(width, height)
    maze = maze_gen.generate()
    maze_gen.print_maze()
