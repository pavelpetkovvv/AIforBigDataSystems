import maze as mz
import ui as u
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Node):
            return False
        return self.row == __value.row and self.col == __value.col
    
    def __hash__(self) -> int:
        return hash(self.row) + hash(self.col)
    
    def __str__(self):
        return "(" + str(self.col) + ", " + str(self.row) + ")"
    
    def __repr__(self):
        return self.__str__()



def build_graph(maze:mz.Maze, pos):
    # global pos
    G = nx.Graph()
    grid = [[Node(w, h) for w in range(maze.width)] for h in range(maze.height)]
    for i in range(maze.width):
        for j in range(maze.height):
            curr_node = grid[i][j]
            if(str(maze.grid[i][j]) == "0" and curr_node.visited == False):
                curr_node.visited = True
                G.add_node(curr_node)
                pos[curr_node] = (j, -i)

    for i in range(maze.width-1):
        for j in range(maze.height):
            curr_node = grid[i][j]
            neighbour = grid[i+1][j]
            if(str(maze.grid[i][j]) == "0" and str(maze.grid[i+1][j]) == "0"):
                G.add_edge(curr_node, neighbour)

    for i in range(maze.width):
        for j in range(maze.height-1):
            curr_node = grid[i][j]
            neighbour = grid[i][j+1]
            if(str(maze.grid[i][j]) == "0" and str(maze.grid[i][j+1]) == "0"):
                G.add_edge(curr_node, neighbour)
    return G