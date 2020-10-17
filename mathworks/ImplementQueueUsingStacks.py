class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enter_stack = list()
        self.leave_stack = list()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.enter_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.leave_stack) == 0:
            while len(self.enter_stack) != 0:
                self.leave_stack.append(self.enter_stack.pop())
        
        return self.leave_stack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.leave_stack) == 0:
            while len(self.enter_stack) != 0:
                self.leave_stack.append(self.enter_stack.pop())
        
        return self.leave_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return not self.enter_stack and not self.leave_stack
        
# FASTER THAN 99.84%

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
