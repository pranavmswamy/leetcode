def verticalOrderTraversal(root):

	# keep track of dist wrt 0 for root node.
	# if you go left, do level-1
	# if you go right, do level+1
	# collect all nodes of the same level in the dict
	# print them.
	# keep track of min and max level so that it helps you to print later.
	vertical = dict()
	max_left = 0
	max_right = 0

	def vertical_traverse(node, level, vertical):
		if not node:
			return
		if level not in vertical:
			vertical[level] = [node.val]
		else:
			vertical[level].append(node.val)

		if level < 0:
			max_left = min(level, max_left)
		elif level > 0:
			max_right = max(level, max_right)

		vertical_traverse(node.left, level-1, vertical)
		vertical_traverse(node.right, level+1, vertical)

	vertical_traverse(root, 0, vertical)

	return vertical