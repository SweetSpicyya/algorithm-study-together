class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.now,self.min_ele = self.stack[-1]
            if val < self.min_ele:
                self.stack.append((val,val))
            else :
                self.stack.append((val,self.min_ele))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        self.top_ele,self.min_ele = self.stack[-1]
        return self.top_ele
        
    def getMin(self):
        """
        :rtype: int
        """
        self.now,self.min_ele = self.stack[-1]
        return self.min_ele


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()