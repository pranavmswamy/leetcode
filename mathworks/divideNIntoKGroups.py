
class Solution:

	def __init__(self):
		self.ans = list()

	def n_into_k(self, n, k, current):
		if len(current) == k and sum(current) == n:
			self.ans.append(current)
			return True
		elif len(current) == k:
			return False


		for i in range(1, n+1):
			cur_sum = sum(current)
			if len(current) <= k and cur_sum + i <= n:
				if current and current[-1] <= i:
					self.n_into_k(n, k, current[:] + [i])
				elif not current:
					self.n_into_k(n, k, current[:] + [i])
			else:
				break # if cur_sum+i > n, cur_sum + (i+1) will be >>.

	def n_into_groups_of_k(self, n, k):
		self.ans = list()
		self.n_into_k(n, k, list())
		print(self.ans)
		print(len(self.ans))

s = Solution()
s.n_into_groups_of_k(8,4)
s.n_into_groups_of_k(24,5)



