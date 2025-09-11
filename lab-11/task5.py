class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_edge(self, u, v):
        # Add an edge from u to v (undirected by default)
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        # Breadth-First Search traversal from the start node
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)  # Dequeue the first node
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Enqueue all unvisited neighbors
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_recursive(self, start, visited=None, result=None):
        # Recursive Depth-First Search traversal
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(start)
        result.append(start)
        # Visit all unvisited neighbors recursively
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
        return result

    def dfs_iterative(self, start):
        # Iterative Depth-First Search traversal using a stack
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()  # Pop the last node (LIFO)
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Add all unvisited neighbors to the stack
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("BFS:", g.bfs(1))  # Output: BFS traversal order
    print("DFS Recursive:", g.dfs_recursive(1))  # Output: DFS (recursive) order
    print("DFS Iterative:", g.dfs_iterative(1))  # Output: DFS (iterative) order