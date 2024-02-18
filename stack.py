class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
#example usage
stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("stack:", stack.items)
print("pop:", stack.pop())
print("peek:", stack.peek())
print("stack size:", stack.size())

