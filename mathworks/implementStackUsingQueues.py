# METHOD 1:

# ACTUALLY HAVE TO USE A LINKED LIST FOR 0(1) OPERATIONS. IN PYTHON, IT MIGHT BECOME O(N) BECAUSE YOU ARE POPPING THE 0TH ELEMENT.
class MyStack:
    # Approach 1:
    '''
    Keep two queues - q1 and q2
    
    PUSH:
    Insert new element to q2
    Add all elements from q1 to end of q2
    swap q1 and q2 references
    
    Top of stack - first elt of q1.
    
    POP:
    Just remove first elt from q1
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = list()
        self.q2 = list()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        if self.q1:
            while self.q1:
                self.q2.append(self.q1.pop(0))
        
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            return self.q1.pop(0)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.q1 else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()




class MyStack:
    # Approach 2:
    '''
    PUSH: (O(1))
    Just append to q2
    
    POP: (O(N)):
    - Add all elts except last element of q2 to q1.
    - then swap q1 and q2 to maintain invariant.
    
    TOP:
    last appended elt to q2
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = list()
        self.q2 = list()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q2) != 1:
            self.q1.append(self.q2.pop(0))
        
        # delete the elt:
        popped = self.q2.pop(0)
        
        self.q1, self.q2 = self.q2, self.q1
        
        return popped

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q2:
            return self.q2[-1]
        elif self.q1:
            return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.q1 and not self.q2 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyStack:
    # Approach 3:
    '''
    ONLY ONE QUEUE
    
    PUSH: (O(n))
    - add elelent to end of list
    - store size of array.
    - except for the last element, remove element from list and append to same list
    - this maintains the invariant of most recently inserted element at the beginning of the list
    
    POP:
    pop and return list[0]
    
    TOP:
    return list[0]
    
    
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = list() 

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        q1_size = len(self.q1)
        while q1_size != 1:
            self.q1.append(self.q1.pop(0))
            q1_size -= 1 
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop(0)
    
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.q1 else False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
