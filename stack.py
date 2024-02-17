class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("Stack is empty. Cannot pop.")
            return None

        self.top = self.top.next
        self.length -= 1
            
# Example usage:
stack = Stack(1)
stack.push(2)
stack.push(3)
print("---------Elements in the stack----------")
stack.print_stack()
stack.pop()
print("---------Elements in the stack after pop----------")
stack.print_stack()
print("--------- Insert Elements in the stack----------")
stack.push(21)
stack.print_stack()