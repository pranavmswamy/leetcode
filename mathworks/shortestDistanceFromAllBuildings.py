
buildings = [
[1,0,2,0,1]
[0,0,0,0,0]
[0,0,1,0,0]]

def shortestDistance(buildings):

	def isValid(i, j):
		return i>= 0 and i <= len(buildings) and j >= 0 and j<= len(buildings[0]) and buildings[i][j] == 0 and not visited[i][j]

	def bfs(buildings, distance, count, i, j):
		frontier = [(i,j,0)]

		while frontier:
			children = list()
			for i,j,depth in frontier:
				distance[i][j] += depth
				count[i][j] += 1
				if isValid(i, j+1):
					children.append(i,j+1, depth+1)
				if isValid(i+1, j):
					children.append(i+1, j, depth+1)
				if isValid(i-1, j):
					pass
				if isValid(i, j-1):
					pass

	distances = [[0]*__ for _ in __] # keeps sum of distances of all buildings that are reached at this point
	count = [[0]*__ for _ in __] # keeps count of buildings that can reach this point
	for i in range(len(buldings)):
		for j in range(len(buildings[0])):
			if buildings[i][j] == 1:
				bfs(buildings, distance, count, i, j)

	# find min dist val in distances 2d array, provided buildings[i][j] == 0
	# Also keep a count 2d array for counting if all buildings are reached.


