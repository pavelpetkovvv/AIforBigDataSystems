import maze as mz
import ui as u
import networkx as nx
import matplotlib.pyplot as plt
import graph as gr

if __name__ == "__main__":
    # width = int(input("Enter maze width: "))
    # height = int(input("Enter maze height: "))

    width = 5
    height = 5

    maze = mz.Maze(width, height)
    ui = u.UI(width, height, maze)
    ui.draw_maze()
    print(maze)

    pos = {}

    g = gr.build_graph(maze, pos)
    print(g)

    path = nx.astar_path(g, gr.Node(maze.start_cell[1], maze.start_cell[0]), gr.Node(maze.end_cell[1], maze.end_cell[0]))
    print(path)

    nx.draw(g, pos, with_labels=True, font_weight='bold')
    plt.show()
