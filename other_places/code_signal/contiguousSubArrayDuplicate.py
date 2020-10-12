
# O(n^2). Check if there are better DP solutions.

def numInterval(arr):
    ans = 0
    for end in range(len(arr)):
        mymap = dict()
        single = 0
        
        for start in range(end, -1, -1):
            if arr[start] not in mymap:
                mymap[arr[start]] = 0
            mymap[arr[start]] += 1
            
            if mymap[arr[start]] == 1:
                single += 1
            elif mymap[arr[start]] == 2:
                single -= 1
            if single == 0:
                ans += 1
    return ans
