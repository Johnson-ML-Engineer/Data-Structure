class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def  pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def remove_element(self,value):
        if self.length == 1 and self.head.value == value:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        temp = self.head    
        while temp and temp.value != value:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp.next = None
        self.length -= 1

    def reverse_list(self):
        
        temp = self.head
        prev = None

        while temp:
            nextnode = temp.next
            temp.next = prev
            prev = temp
            temp = nextnode
        self.head = prev

        

    

        


         

my_list = linkedlist(3)

print("------performaning reverse---------")
my_list.reverse_list()
my_list.print_list()


