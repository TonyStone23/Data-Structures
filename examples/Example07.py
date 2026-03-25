class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
S = Stack()
print(S.isEmpty())
S.push('a');S.push('b');S.push('c')
print(S.isEmpty())
print(S.size());print(S.pop());print(S.size())