# BFS 遍历图的所有节点
def bfs(graph, s, target):
	visited = [False] * len(graph)
	q = deque([s])
	visited[s] = True
	step = 0

	while q:
		sz = len(q):
		for i in range(sz):
			cur = q.popleft()
			if cur == target:
				return step

			for to in neighborsOf(cur):
				if not visited[to]:
					q.append(to)
					visited[to] = True
		step += 1
	return -1
