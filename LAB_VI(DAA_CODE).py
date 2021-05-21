print("Coded by Sahil\n")
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['5'],
    '4': ['3'],
    '5': ['6'],
    '6': []
}
t=1
pr={}
po={}
check=[]
visited = set()

def dfs(visited, graph, node):
    global t
    if node not in visited:
        print(node,end=" ")
        pr[node] = t
        t += 1
        check.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("THE DFS(Inorder Traversal) is as below :")
dfs(visited, graph, '1')
post=pr.copy()
print("\n")
for i in check[::-1]:
    po[i]=t
    t+=1
for i in pr:
    print("Pre number :",pr[i]," Post Number :",po[i],"for Node ",i)

v = []
q = []

def bfs(v, graph, node):
  v.append(node)
  q.append(node)

  while q:
    d = q.pop(0)
    print(d)
    for neighbour in graph[d]:
      if neighbour not in v:
        v.append(neighbour)
        q.append(neighbour)

print("The BFS TRAVERSAL IS AS BELOW :")
bfs(v, graph, '1')
class Gra:
	def __init__(self, e, N):

		self.adjList = [[] for _ in range(N)]
		for (src, dest) in e:
			self.adjList[src].append(dest)
def DFS(gr, v, visited):
    visited[v] = True
    for u in gr.adjList[v]:
        if not visited[u]:
            DFS(gr, u, visited)


def check(gr, N):

	for i in range(N):
		visited = [False] * N
		DFS(gr, i, visited)
		for b in visited:
			if not b:
				return False

	return True

e = [(1, 2), (1, 3), (2, 4), (4, 3), (3, 5), (5, 6)]
N = 6
gr = Gra(e, N)
if check(gr, N):
    print("Graph is also Connected here :")
else:
    print("Graph is also Connected here :")
