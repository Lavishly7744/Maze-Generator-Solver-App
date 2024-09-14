from collections import deque

class MazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.visited = set()

    def solve(self):
        path = self._dfs(self.start[0], self.start[1])
        return path if path else None

    def _dfs(self, x, y):
        if (x, y) == self.end:
            return [(x, y)]
        self.visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == ' ' and (nx, ny) not in self.visited:
                path = self._dfs(nx, ny)
                if path:
                    return [(x, y)] + path
        return None

    def print_path(self, path):
        for x, y in path:
            self.maze[x][y] = '.'
        for row in self.maze:
            print(''.join(row))

# Main to solve the maze
if __name__ == "__main__":
    # Example maze (replace with generated maze)
    maze = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', '#', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]
    start = (1, 1)
    end = (3, 5)

    solver = MazeSolver(maze, start, end)
    path = solver.solve()

    if path:
        print("Solution found!")
        solver.print_path(path)
    else:
        print("No solution exists.")
