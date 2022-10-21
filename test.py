class stack():
    def __init__(self):
        self.new_stack=[]
    
    def add(self,value):
        self.new_stack.append(value)
    
    def remove(self):
        return self.new_stack.pop(-1)
    
    def __repr__(self) -> str:
        return f'{self.new_stack}'
stack1=stack()
print(stack1)
stack1.add(10)
stack1.add(20)
stack1.add(30)
print(stack1)
print(stack1.remove())
print(stack1)



class Queue():
    def __init__(self):
        self.new_stack=[]
    
    def add(self,value):
        self.new_stack.append(value)
    
    def remove(self):
        return self.new_stack.pop(0)
    
    def __repr__(self) -> str:
        return f'{self.new_stack}'
stack1=Queue()
print(stack1)
stack1.add(10)
stack1.add(20)
stack1.add(30)
print(stack1)
print(stack1.remove())
print(stack1)