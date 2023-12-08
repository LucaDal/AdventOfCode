from math import lcm

def get_step_to_node_z(directions,node,actual_node_dir):
    counter: int = 0
    while actual_node_dir[-1] != 'Z':
        for direction in directions:
            counter+=1
            if direction == "L":
                actual_node_dir = node.get(actual_node_dir)[0]
            else:
                actual_node_dir = node.get(actual_node_dir)[1]
    return counter


def node_iteration(directions, nodes, starting_nodes):
    steps = []
    for actual_node_dir in starting_nodes:
        print(actual_node_dir)
        steps.append(get_step_to_node_z(directions,nodes,actual_node_dir))
    return steps

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

directions = lines.pop(0)
starting_nodes = []
nodes = {}

lines.pop(0)
for line in lines:
    nodes[line[:3]] = [line[7:10],line[12:15]]
    if line[2] == 'A':
        starting_nodes.append(line[:3])

steps = node_iteration(directions, nodes, starting_nodes)
print(lcm(*steps))
