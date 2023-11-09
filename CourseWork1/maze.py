class Cell:
    def __init__(self, is_border=False):
        self.is_border = is_border

    def __str__(self):
        return "X" if self.is_border else "0"

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]
        self.start_cell = None
        self.end_cell = None

    def set_border(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.grid[row][col].is_border = True

    def set_empty(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.grid[row][col].is_border = False

    def set_start(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.start_cell = (row, col)

    def set_end(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            self.end_cell = (row, col)

    def __str__(self):
        result = ""
        for row in self.grid:
            result += "".join(str(cell) for cell in row) + "\n"
        return result


def find_all_routes(maze, row, col, visited, route):
    if (row, col) == maze.end_cell:
        route.append((row, col))
        return [route]  # Found a route to the end

    possible_routes = []

    # Define all possible moves (up, down, left, right)
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

        if (
            0 <= new_row < maze.height
            and 0 <= new_col < maze.width
            and not visited[new_row][new_col]
            and not maze.grid[new_row][new_col].is_border
        ):
            visited[new_row][new_col] = True
            next_route = route + [(row, col)]
            possible_routes.extend(find_all_routes(maze, new_row, new_col, visited, next_route))
            visited[new_row][new_col] = False

    return possible_routes

def find_all_routes_in_maze(maze):
    if not maze.start_cell or not maze.end_cell:
        return []

    visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]
    visited[maze.start_cell[0]][maze.start_cell[1]] = True

    return find_all_routes(maze, maze.start_cell[0], maze.start_cell[1], visited, [])

def find_best_route(maze):
    routes = find_all_routes_in_maze(maze)
    for route in enumerate(routes):
        print(f"Route: {route}")

    sorted_routes = sorted(routes, key=lambda x: len(x))
    return sorted_routes[0]