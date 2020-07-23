"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node    
        
    def get_value(self):
        return self.value    
        
    def get_next(self):
        return self.next_node    
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            self.tail = None
            x = 2
            while x is not self.length:
                self.tail = self.head.get_next()
                x += 1
            self.length -= 1
            return value

class Queue:
    def __init__(self):
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             pass
#         else:
#             self.size -= 1
#             return self.storage.pop(0)
