class MyQueue(object):

    def __init__(self):
        self.stack_push =[]
        self.stack_pop =[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.x = x
        self.stack_push.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

        return self.stack_pop.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

        element = self.stack_pop[-1]
        return element
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack_pop and not self.stack_push :
            return True
        else : return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()