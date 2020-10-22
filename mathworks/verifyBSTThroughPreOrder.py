
'''
O(n^2) recursive soln

Find the first greater value on right side of current node. 
   Let the index of this node be j. Return true if following 
   conditions hold. Else return false
    (i)  All values after the above found greater value are 
         greater than current node.
    (ii) Recursive calls for the subarrays pre[i+1..j-1] and 
         pre[j+1..n-1] also return true. 
'''

# O(n)
def verifyBSTThroughPreOrder(preorder):

	last_popped = float('-inf')
	stack = list()
	for num in preorder:
		# if number less than last popped, then the number cannot be there since its ancestor is greater than it, and it should actually be in the left subtree of the ancestor.
		if num < last_popped:
			return False

		# keep popping stack and updating last_popped
		# until stack is empty or stack.top  > num
		# assumes that all nums are distinct. so only > and not >=
		while stack and num > stack[-1]:
			last_popped = stack.pop()

		# add to stack
		stack.append(num)

	# all valid, so return true
	return True


print(verifyBSTThroughPreOrder([5, 2, 6, 1, 3]))
print(verifyBSTThroughPreOrder([5, 2, 1, 3, 6]))
print(verifyBSTThroughPreOrder([40, 30, 35, 80, 100]))
print(verifyBSTThroughPreOrder([40, 30, 35, 20, 80, 100]))
print(verifyBSTThroughPreOrder([5, 2, 1, 3, 6]))

# https://www.youtube.com/watch?v=0kkVobZ6Ebc&ab_channel=NerdsInABarrel
