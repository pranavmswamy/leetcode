class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # CREATE A PRODUCTS[LEN1 + LEN2] ARRAY
        # REVERSE ITERATE:
        # FOR(NUM1-1, -1, -1):
        #   FOR (NUM2 -1, -1):
                # ADD (+=) PRODUCT OF I AND J TO PRODUCTS[I+J+1]
        # IT WILL POPULATE AN ARRAY OF PARTIAL PRODUCTS
        
        # CARRY OVER THE CARRYS AND RETURN LIST CONVERTED TO STRING.
        
        
        
        products = [0]*(len(num1) + len(num2))
        
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                # product of each digit.
                # each digit will be stored at pos i+j+1
                products[i+j+1] += int(num1[i])*int(num2[j])
        
        carry = 0
        for i in range(len(products)-1, -1, -1):
            ith_place = (carry + products[i]) % 10
            carry = (carry + products[i]) // 10
            products[i] = ith_place
        
        start_range = 0
        while start_range < len(products) and products[start_range] == 0: start_range+=1
        
        return "".join([str(i) for i in products[start_range:]]) if start_range < len(products) else '0'
