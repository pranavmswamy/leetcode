

def threeSumSmaller(nums, target):

	# edge cases:
	if len(nums) < 3:
		return 0

	# sort nums, cause when we sort it, to find idxes, all distinct indexes that satisfy the contition of nums[i] + nums[j] + nums[k] < target will
	# end up in the same index range.
	nums.sort()

	count = 0
	# start threesum 

	for i in range(0, len(nums)-2, 1): # i
		
		j = i+1
		k = len(nums)-1
		while j < k:
			if nums[i] + nums[j] + nums[k] < target:
				count += k-j
				j += 1 # start from next j
			else:
				k -= 1 # nums[i+j+k] too high, decrease k

	return count


print(threeSumSmaller([-2,0,1,3], 2)) # 2
print(threeSumSmaller([5, 1, 3, 4, 7], 12)) # 4
#print(threeSumSmaller())


