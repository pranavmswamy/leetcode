# To go from X to Y
# Do BFS from that number
# Children will be num with all the operations
# if you find it, return true
# else, return false




# OR Go from Y -> X ( Possibly lower number of operations)

# Instead of multiplying by 2 or subtracting 1 from X, we could divide by 2 (when Y is even) or add 1 to Y.

# The motivation for this is that it turns out we always greedily divide by 2:

# If say Y is even, then if we perform 2 additions and one division, 
#	we could instead perform one division and one addition for less operations [(Y+2) / 2 vs Y/2 + 1].

# If say Y is odd, then if we perform 3 additions and one division,
	# we could instead perform 1 addition, 1 division, and 1 addition for less operations [(Y+3) / 2 vs (Y+1) / 2 + 1].

# Algorithm
# While Y is larger than X, add 1 if it is odd, else divide by 2. After, we need to do X - Y additions to reach X.


class Solution(object):
    def brokenCalc(self, X, Y):
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y /= 2

        return ans + X-Y
