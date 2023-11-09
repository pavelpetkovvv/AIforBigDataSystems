import tkinter as tk
import maze as mz

current_action = "Border"

buttons_size = 4
maze = None

def change_button_text(row, col, text):
    button_colors[row][col] = text
    buttons[row][col].config(text=text)

def which_button(row, col):
    print ("Row :" + str(row), " Col: "+ str(col))
    change_button_text(row, col, current_action)
    if current_action == "Border":
        maze.set_border(row, col)
    elif current_action == "Finish\nPoint":
        maze.set_end(row, col)
    elif current_action == "Start\nPoint":
        maze.set_start(row, col)
    elif current_action == "":
        maze.set_empty(row, col)

def select_starting_point():
    global current_action
    current_action="Start\nPoint"
    print("Select Start Point")

def select_finish_point():
    global current_action
    current_action="Finish\nPoint"
    print("Select Finish Point")

def place_border():
    global current_action
    current_action="Border"
    print("Place Border")

def remove_element():
    global current_action
    current_action=""
    print("Remove element")

def draw_maze(width: int, height: int):
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Maze Solver")

    global buttons, button_colors
    buttons = [[None for _ in range(height)] for _ in range(width)]
    button_colors = [["white" for _ in range(height)] for _ in range(width)]

    # Create a grid of buttons
    for row in range(width):
        for col in range(height):
            button = tk.Button(window, width=buttons_size, height=buttons_size, text="   ", command=lambda r=row, c=col: which_button(r, c))
            button.grid(row=row, column=col)
            buttons[row][col] = button
    
    # Create buttons for actions
    starting_point_button = tk.Button(window, text="Place\nStarting\nPoint", command=select_starting_point, width=buttons_size, height=buttons_size)
    starting_point_button.grid(row=width, column=0)

    finish_point_button = tk.Button(window, text="Place\nFinish\nPoint", command=select_finish_point, width=buttons_size, height=buttons_size)
    finish_point_button.grid(row=width, column=1)

    place_border_button = tk.Button(window, text="Place\nBorder", command=place_border, width=buttons_size, height=buttons_size)
    place_border_button.grid(row=width, column=2)

    remove_element_button = tk.Button(window, text="Remove", command=remove_element, width=buttons_size, height=buttons_size)
    remove_element_button.grid(row=width, column=3)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    # width = int(input("Enter maze width: "))
    # height = int(input("Enter maze height: "))

    maze = mz.Maze(10, 10)
    draw_maze(10, 10)
    print(maze)
    routes = mz.find_all_routes_in_maze(maze)
    for route in enumerate(routes):
        print(f"Route: {route}")

    sorted_routes = sorted(routes, key=lambda x: len(x))
    n_shortest_routes = sorted_routes[:3]

    print("3 shortest routs: ")

    for route in enumerate(n_shortest_routes):
        print(f"Route: {route}")