import maze as mz
import ui as u

if __name__ == "__main__":
    # width = int(input("Enter maze width: "))
    # height = int(input("Enter maze height: "))

    maze = mz.Maze(10, 10)
    ui = u.UI(10, 10, maze)
    ui.draw_maze()
    print(maze)

    routes = mz.find_all_routes_in_maze(maze)
    for route in enumerate(routes):
        print(f"Route: {route}")

    sorted_routes = sorted(routes, key=lambda x: len(x))
    n_shortest_routes = sorted_routes[:3]

    print("3 shortest routs: ")

    for route in enumerate(n_shortest_routes):
        print(f"Route: {route}")