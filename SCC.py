import time, sys
def main():
    sys.setrecursionlimit(100000)
    start = time.time()

    size = 875714

    g = Graph(size)
    g.getGraph()
    g.resetExploration()
    g.dfsLoop()
    g.reverseEdge()
    g.resetExploration()
    g.LargestSCC()

    
    print(f'----------------------------{time.time() - start}--------------------')

class Graph:
    graph = {}  #  graph with same direction
    grev = {}   #  graph with reverse direction


    def __init__(self, size):
        for i in range(size):
            self.graph[i + 1] = []
            self.grev[i + 1] = []

        self.vertices = size

    def getGraph(self):
        f = open(r"E:\Summer 2019\Algorithms\Kosaraju's Two Pass Algorithm\SCC.txt")
        content = f.read().splitlines()

        for line in content:
            line = [int(i) for i in line.split()]
            self.addEdge(self.graph, line[0], line[1])
                
        f.close()

    # directed edge u -----> v
    def addEdge(self, g, u, v): 
        if u != v:
            g[u].append(v)
        
    
    def resetExploration(self):
        self.visited = [False] * self.vertices


    def dfsLoop(self):
        # finishing time for 1st pass
        self.t = 0
        self.finishingOrder = []

        #counter from max to low
        node = self.vertices

        while node:
            if self.visited[node - 1] == False:
                self.dfs(node)

            node -= 1


    def dfs(self, node):
        self.visited[node - 1] = True
        for item in self.graph[node]:
            if self.visited[item - 1] == False:
                self.dfs(item)

        self.t += 1
        self.finishingOrder.append(node)


    def reverseEdge(self):
        
        for item in self.graph:
            for node in self.graph[item]:
                self.addEdge(self.grev, node, item)



    def LargestSCC(self):
        self.counter = [0] * 5

        while self.finishingOrder :
            node = self.finishingOrder.pop()
            self.miniCounter = 0
            if self.visited[node - 1] == False:
            
                self.helper(node)
            
            if min(self.counter) < self.miniCounter:
                self.counter[self.counter.index(min(self.counter))] = self.miniCounter

        print(self.counter)


    def helper(self, node): 
        self.visited[node - 1] = True
        for item in self.grev[node]:
            if self.visited[item - 1] == False:
                self.helper(item)

        self.miniCounter += 1


if __name__ == "__main__":
    main()