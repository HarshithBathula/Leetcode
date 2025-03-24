class MinStack(object):

    def __init__(self):
        self.stack = []
        self.temp = []   

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.temp or val <= self.temp[-1]: 
            self.temp.append(val)

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if self.temp and val == self.temp[-1]:
            self.temp.pop()    

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.temp[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()