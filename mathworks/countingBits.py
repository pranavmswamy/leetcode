class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]*(num+1)
        
        # when the number is odd, then the last bit is 1
        # so the number of 1's in it are 1 + number if ones in number-1 since number-1 will be the even number that has same 1's except the last one.
        
        # when the number is even, the last bit is a zero.
        # so, the number of ones in it will be the same as the numbe r of ones in number >> 1. (number >> 1 is number/2)
        
        
        # side note - number & 1 will tell you if number is even or odd.
        # all even nums end with 0, od nums with 1
        # so num & 1 = 1 for odd and 0 for even.
        
        for i in range(1, num+1):
            if i % 2 == 0:
                result[i] = result[i >> 1]
            else:
                result[i] = result[i-1] + 1
             
        
        return result
