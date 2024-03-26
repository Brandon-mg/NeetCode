class MinStack1Stack:

    def __init__(self):
        self.min_stack = []

    def push(self, val):
        if len(self.min_stack) == 0:
            self.min_stack.append([val,val])
            return
        last_min = self.min_stack[-1][1]
        self.min_stack.append([val,min(val,last_min)])

    def pop(self):
        self.min_stack.pop()
        

    def top(self):
        return self.min_stack[-1][0]

    def getMin(self):
        return self.min_stack[-1][1]
    
class MinStack2Stack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
        if len(self.stack)==0:
            self.min_stack.append(val)
            return
        self.min_stack.append(min(val,self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
    
if __name__ == '__main__':
    oneStack = MinStack1Stack()
    oneStack.push(-2)
    oneStack.push(0)
    oneStack.push(-3)
    print(oneStack.getMin)
    oneStack.pop()
    print(oneStack.top())
    print(oneStack.getMin())

    twoStack = MinStack2Stack()
    twoStack.push(-2)
    twoStack.push(0)
    twoStack.push(-3)
    print(twoStack.getMin)
    twoStack.pop()
    print(twoStack.top())
    print(twoStack.getMin())

                             
