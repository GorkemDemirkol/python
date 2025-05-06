# from queue import LifoQueue

# stack= LifoQueue(maxsize=5)
 
# stack.put("Gorkem")
# stack.put("Mete") 
# stack.put("Gokce")
# stack=stack.get()
# print(stack)

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def size(self):
        return len(self.items)
    
def is_balanced(expression):
    stack= Stack()
    opening = "({["
    closing = ")}]"
    matches = {")": "(", "}": "{", "]": "["}
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False
    return stack.is_empty()
experession = "{[()]}"

if is_balanced(experession):
    print("İfade dengelidir")
else:
    print("İfade dengeli değildir")
    