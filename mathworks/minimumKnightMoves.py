# bidirectional search

def isValid(n, visited, i, j):
	return i >= 0 and j >= 0 and i < n and j < n and visited[i][j] == -1

def minKnightMoves(n, startRow, startCol, endRow, endCol):
	dx = [2, 2, -2, -2, 1, 1, -1, -1]
	dy = [1, -1, 1, -1, 2, -2, 2, -2]

	visited1 = [[-1]*n for _ in range(n)]
	visited2 = [[-1]*n for _ in range(n)]

	frontier1 = [(startRow, startCol, 0)]
	frontier2 = [(endRow, endCol, 0)]
	visited1[startRow][startCol] = 0
	visited2[endRow][endCol] = 0

	is_start = True
	frontier = []
	children = []
	
	if is_start:
		frontier = frontier1
	else:
		frontier = frontier2


	while frontier1 or frontier2:
		children1 = list()
		children2 = list()

		if is_start:
			frontier = frontier1
		else:
			frontier = frontier2

		for i, j, depth in frontier:
			
			print(i,j,depth)
			if is_start:
				print("start-")
				print('visited1:')
				for i in range(len(visited1)):
					print(visited1[i])
			else:
				print("end-")
				print('visited2:')
				for i in range(len(visited2)):
					print(visited2[i])
			
			if visited1[i][j] != -1 and visited2[i][j] != -1:
				return visited1[i][j] + visited2[i][j]
			
			for x, y in zip(dx, dy):
				next_i = i + x
				next_j = i + j

				if is_start:
					if isValid(n, visited1, next_i, next_j):
						visited1[next_i][next_j] = depth
						children1.append((next_i, next_j, depth+1))
				else:
					if isValid(n, visited2, next_i, next_j):
						visited2[next_i][next_j] = depth
						children2.append((next_i, next_j, depth+1))

		if frontier:
			frontier.pop(0)

		if is_start:
			frontier1.extend(children1)
		else:
			frontier2.extend(children2)


		is_start =  not is_start

	print('visited1:')
	for i in range(len(visited1)):
		print(visited1[i])

	print('visited2:')
	for i in range(len(visited2)):
		print(visited2[i])

print(minKnightMoves(10,2,3,1,6))

