import heapq
import networkx as nx
import matplotlib.pyplot as plt
import math
import string
import itertools

# Node class to store information about each node
class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
    
    def __lt__(self, other):
        return self.heuristic < other.heuristic

# Greedy Best-First Search for Hierarchical Routing
def greedy_best_first_search_hierarchical(graph, start, goal, heuristic, region_map):
    # Priority queue to hold nodes to explore, sorted by heuristic value
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, heuristic[start]))

    visited = set()  # To keep track of visited nodes

    # Path dictionary to track the explored paths
    path = {start: None}

    while priority_queue:
        current_node = heapq.heappop(priority_queue).name

        # If the goal is reached, reconstruct the path
        if current_node == goal:
            return reconstruct_path(path, start, goal)

        visited.add(current_node)

        # Explore neighbors in the same region first, then move to other regions
        current_region = region_map[current_node]
        for neighbor in graph[current_node]:
            if neighbor not in visited and region_map[neighbor] == current_region:
                heapq.heappush(priority_queue, Node(neighbor, heuristic[neighbor]))
                if neighbor not in path:
                    path[neighbor] = current_node

        # Explore neighbors in other regions after same-region neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited and region_map[neighbor] != current_region:
                heapq.heappush(priority_queue, Node(neighbor, heuristic[neighbor]))
                if neighbor not in path:
                    path[neighbor] = current_node

    return None  # If no path is found

# Helper function to reconstruct the path from start to goal
def reconstruct_path(path, start, goal):
    current = goal
    result_path = []
    while current is not None:
        result_path.append(current)
        current = path[current]
    result_path.reverse()
    return result_path

# Function to visualize the graph and the path
def visualize_graph(graph, path, pos, region_map):
    G = nx.Graph()

    # Add edges to the graph
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Plot the graph
    plt.figure(figsize=(10, 8))
    node_colors = []
    for node in G.nodes:
        if obstacle_nodes and node in obstacle_nodes:
            node_colors.append("black")  # Obstacles in black
        elif path and node in path:
            node_colors.append("lightgreen")  # Path nodes in green
        else:
            node_colors.append("skyblue")  # Default color
    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color=node_colors, font_size=15,node_shape='s', font_weight='bold', edge_color='gray')

    # Highlight the path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='black', width=2.5)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen',node_shape='s')
    
         

    # Display region information on the graph
    for node, region in region_map.items():
        plt.text(pos[node][0], pos[node][1] - 0.2, f" {region}", fontsize=8, color='grey')

    plt.title("Greedy Best-First Search for Hierarchical Routing", size=20)
    plt.show()
    plt.axis("equal")



# Complex graph with hierarchical regions




# Define regions for the hierarchical routing (nodes belonging to different regions)


def generate_region_map(pos, rows, cols, region_rows, region_cols):
    region_map = {}
    region_count = 1

    for key, (x, y) in pos.items():
        # Determine the region based on rows and columns
        region_x = x // region_cols
        region_y = y // region_rows
        region_number = region_y * (cols // region_cols) + region_x + 1
        region_map[key] = region_number

    return region_map

# Define region dimensions (e.g., 5x5 cells per region)
region_rows, region_cols = 5, 5

# Generate the region map

# Define positions for better visualization layout (can be modified) 510 cm x 580 cm
def generate_coordinates(rows, cols):
    pos = {}
    letters = list(string.ascii_uppercase)  # A-Z

    # Extend keys beyond Z (e.g., AA, AB, ...)
    keys = []
    for length in range(1, 3):  # Support up to 2-character column names
        keys.extend([''.join(k) for k in itertools.product(letters, repeat=length)])

    # Generate the coordinates
    for y in range(rows):
        for x in range(cols):
            pos[keys[y*cols+x]] = (x, y)

    return pos
def generate_graph(pos, rows, cols):
    graph = {}

    for key, (x, y) in pos.items():
        neighbors2 = []

        # Check for valid neighbors (left, right, top, bottom)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                neighbor_key = next(k for k, v in pos.items() if v == (nx, ny))
                neighbors2.append(neighbor_key)

        graph[key] = neighbors2

    return graph
    
pos = generate_coordinates(24, 29)

graph=generate_graph(pos,24,29)

# Generate a 20x29 coordinate map
rows, cols = 25, 29

region_map = generate_region_map(pos, 25, 29, region_rows, region_cols)
# Heuristic values (assumed for this example)

obstacle_nodes = set()
x1,y1=6,26
x2,y2=18,29
for x,y in pos.items():
    
    if y1-1<=y[0]<=y2-1 and x1-1<=y[1]<=x2-1:
        
        obstacle_nodes.add(x)

x1,y1=13,6
x2,y2=23,20
for x,y in pos.items():
    
    if y1-1<=y[0]<=y2-1 and x1-1<=y[1]<=x2-1:
        
        obstacle_nodes.add(x)

#add_obstacles(obstacle_nodes, pos, 3, 26, 14, 29)
  # Prints the nodes added as obstacles

def dynamic_obstacle_recognition(obstacles):
    # Example: Simulate new obstacles (replace with real LiDAR processing logic)
    dynamic_updates = {}
    obstacle_nodes.update(dynamic_updates)
    return 
#move_motors(forward_speed, forward_speed)
#move_motors(-forward_speed, -forward_speed)
#move_motors(forward_speed, -forward_speed)
#move_motors(-forward_speed, forward_speed)
#stop_motors()    #DEFINE MOVEMENT
def move_to_node(current_node, next_node, node_positions):
    x1, y1 = node_positions[current_node]
    x2, y2 = node_positions[next_node]

    # Determine the direction of movement
    if x2 > x1:
        print("Moving right")
        move_motors(forward_speed, -forward_speed)
    elif x2 < x1:
        print("Moving left")
        move_motors(-forward_speed, forward_speed)
    elif y2 > y1:
        print("Moving up")
        move_motors(forward_speed, forward_speed)
    elif y2 < y1:
        print("Moving down")
        move_motors(-forward_speed, -forward_speed)
    stop_motors()

def execute_path(path, node_positions):
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        move_to_node(current_node, next_node, node_positions)

start_node = 'BF'
goal_node = 'TL'

def get_coordinates(goal_node, pos):
    return pos.get(goal_node, None)
target_point=get_coordinates(goal_node,pos)

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
heuristic = {
     point: (float('inf') if point in obstacle_nodes else round(euclidean_distance(coord, target_point), 2))
    for point, coord in pos.items()
}
   

obstacles=set(obstacle_nodes)
dynamic_obstacles=dynamic_obstacle_recognition(obstacles)
# Perform Greedy Best-First Search for hierarchical routing
print("RADI")
result_path = greedy_best_first_search_hierarchical(graph, start_node, goal_node, heuristic, region_map)
print(result_path)
# IMPLEMENT LIDAR DYNAMIC OBSTACLE RECOGNITION
print("Path from {} to {}: {}".format(start_node, goal_node, result_path))

# Visualize the graph and the found path
visualize_graph(graph, result_path, pos, region_map)
