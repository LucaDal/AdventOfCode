with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

directions = lines.pop(0)
lines.pop(0)

node = {}
for line in lines:
    node[line[:3]] = [line[7:10],line[12:15]]

actual_node_dir = list(node.keys())[0]
counter = 0
while actual_node_dir != 'ZZZ':
    for direction in directions:
        counter+=1
        if direction == "L":
            actual_node_dir = node.get(actual_node_dir)[0]
        else:
            actual_node_dir = node.get(actual_node_dir)[1]
print(counter)