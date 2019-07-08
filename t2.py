import time
f = open(r"E:\Summer 2019\Algorithms\Kosaraju's Two Pass Algorithm\SCC2.txt")
content = f.read().splitlines()
i = 1
size = 875714
graph = {(i+1):[] for i in range(size)}
for line in content:
    line = [int(i) for i in line.split()]
    graph[line[0]] = line[1]

f.close()
text = open(r"E:\Summer 2019\Algorithms\Kosaraju's Two Pass Algorithm\result.txt", 'w')


print(graph)