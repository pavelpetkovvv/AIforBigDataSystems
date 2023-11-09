import tkinter as tk
import maze as mz
import graph as gr
import networkx as nx

class UI:

    def __init__(self, width, height, maze):
        self.width = width
        self.height = height
        self.buttons_size = 4
        self.maze = maze
        self.current_action = "Border"

    def change_button_text(self, row, col, text):
        self.button_colors[row][col] = text
        self.buttons[row][col].config(text=text)

    def which_button(self, row, col):
        print ("Row :" + str(row), " Col: "+ str(col))
        self.change_button_text(row, col, self.current_action)
        if self.current_action == "Border":
            self.maze.set_border(row, col)
        elif self.current_action == "Finish\nPoint":
            self.maze.set_end(row, col)
        elif self.current_action == "Start\nPoint":
            self.maze.set_start(row, col)
        elif self.current_action == "":
            self.maze.set_empty(row, col)

    def select_starting_point(self):
        self.current_action="Start\nPoint"
        print("Select Start Point")

    def select_finish_point(self):
        self.current_action="Finish\nPoint"
        print("Select Finish Point")

    def place_border(self):
        self.current_action="Border"
        print("Place Border")

    def remove_element(self):
        self.current_action=""
        print("Remove element")

    def find_best_route(self):
        for r in mz.find_best_route(self.maze):
            if (self.buttons[r[0]][r[1]].cget("text") != "Start\nPoint") & (self.buttons[r[0]][r[1]].cget("text") != "Finish\nPoint"):
                self.buttons[r[0]][r[1]].config(text="route")

    def find_best_route_astar(self):
        pos = {}
        g = gr.build_graph(self.maze, pos)
        print(g)
        path = nx.astar_path(g, gr.Node(self.maze.start_cell[1], self.maze.start_cell[0]), gr.Node(self.maze.end_cell[1], self.maze.end_cell[0]))
        for n in path:
            self.buttons[n.col][n.row].config(text="route")

    def draw_maze(self):
        # Create a Tkinter window
        window = tk.Tk()
        window.title("Maze Solver")

        # global buttons, button_colors
        self.buttons = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.button_colors = [["white" for _ in range(self.width)] for _ in range(self.height)]

        # Create a grid of buttons
        for row in range(self.width):
            for col in range(self.height):
                button = tk.Button(window, width=self.buttons_size, height=self.buttons_size, text="   ", command=lambda r=row, c=col: self.which_button(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Create buttons for actions
        starting_point_button = tk.Button(window, text="Place\nStarting\nPoint", command=self.select_starting_point, width=self.buttons_size, height=self.buttons_size)
        starting_point_button.grid(row=self.width, column=0)

        finish_point_button = tk.Button(window, text="Place\nFinish\nPoint", command=self.select_finish_point, width=self.buttons_size, height=self.buttons_size)
        finish_point_button.grid(row=self.width, column=1)

        place_border_button = tk.Button(window, text="Place\nBorder", command=self.place_border, width=self.buttons_size, height=self.buttons_size)
        place_border_button.grid(row=self.width, column=2)

        remove_element_button = tk.Button(window, text="Remove", command=self.remove_element, width=self.buttons_size, height=self.buttons_size)
        remove_element_button.grid(row=self.width, column=3)

        remove_element_button = tk.Button(window, text="Find\nbest\nroute", command=self.find_best_route_astar, width=self.buttons_size, height=self.buttons_size)
        remove_element_button.grid(row=self.width, column=4)

        # Start the Tkinter event loop
        window.mainloop()
