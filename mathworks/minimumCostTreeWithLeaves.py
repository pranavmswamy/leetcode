class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            min_idx = arr.index(min(arr))
            if 0 < min_idx < len(arr)-1:
                res += min(arr[min_idx+1], arr[min_idx-1])*arr[min_idx]
            elif min_idx == 0:
                res += arr[0]*arr[1]
            else:
                res += arr[-1]*arr[-2]
            arr.pop(min_idx)
        
        return res
