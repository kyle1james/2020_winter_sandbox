import random, pprint

def make_matrix(col, row):
    matrix = [[random.randint(0,10) for x in range(col)] for y in range(row)]
    pprint.pprint(matrix)
    return matrix

def get_neighbors(x,y,matrix,block):
    row = len(matrix)
    col = len(matrix[0])
    n = ((x+1,y), (x-1,y), (x,y-1), (x, y+1), (x-1,y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1))
    neighbors = ((x,y) for x,y in n if 0<= x < row and 0 <= y < col and matrix[x][y] < block)
    return neighbors

def bfs(matrix, start=None, end=None, block=float('inf')):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path

        x,y = node
        neighbors = get_neighbors(x,y,matrix,block)
        for cx,cy in neighbors:
            if (cx,cy) not in visited:
                visited.append((cx,cy))
                new_path = list(path)
                new_path.append((cx,cy))
                queue.append(new_path)
    return False


matrix = make_matrix(5,5)
print(bfs(matrix,(0,0),(4,4)))



def bfs_adj(graph,start,end):
    visited = {v:False for v in graph}
    queue = [start]
    parent = {v:None for v in graph}
    parent[start]= start

    while queue:
        node = queue.pop(0)
        if node == end:
            while end != start:
                print(end)
                end = parent[end]
            print(end)

            return parent
        if not visited[node]:
            visited[node] = True
            for u in graph[node]:
                if parent[node] != u:
                    parent[u] = node
                queue.append(u)
    return False


graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}



"""
2 --- 0 --- 1 --- 5
  \   |
   \  |
      3 --- 4
"""
