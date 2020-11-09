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
		# even result[i] = result[i >> 1] + 1 works! since you are essentially just getting counting the number of ones in the num without the last digit.
             
        
        return result



# Counting set bits in a number:
def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

'''
2. Brian Kernighan’s Algorithm:
Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit.
for example :
10 in binary is 00001010
9 in binary is 00001001
8 in binary is 00001000
7 in binary is 00000111
So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit. If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.
'''
def countSetBits(n): 
  
    count = 0
    while (n): 
        n &= (n-1)  
        count+= 1
      
    return count 