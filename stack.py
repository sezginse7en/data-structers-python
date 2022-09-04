class Stack:
    def __init__(self,stack_array = []):
        self.stack_array = stack_array

    def push(self,value):
        self.stack_array.append(value)
    
    def pop(self):
        if(self.isEmpty()):
            return "stack is empty"
        return self.stack_array.pop()

    def isEmpty(self):
        return len(self.stack_array) == 0

    def size(self):
        return len(self.stack_array)


stack = Stack()

#
4
3
2
1
#

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

for s in range(stack.size()):
    print(stack.pop())



