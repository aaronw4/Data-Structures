"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.tail = new_node
        else:
            new_node = ListNode(value, None, self.head)
            self.head.set_prev(new_node)
        
        self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.next
            self.head = value
            self.head.prev = None
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
        else:
            new_node = ListNode(value, self.tail, None)
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.prev
            self.tail = value
            self.tail.next = None
            self.length -= 1
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        new_head = node
        self.delete(node)
        new_head.set_next(self.head)
        self.head.set_prev(new_head)
        self.head = new_head  
        self.length += 1    
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        new_tail = node
        self.delete(node)
        new_tail.set_prev(self.tail)
        self.tail.set_next(new_tail)
        self.tail = new_tail 
        self.length += 1  

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.set_prev(None)
        elif node == self.tail:
            self.tail = node.prev
            self.tail.set_next(None)
        else:
            node.prev.set_next(node.next)
            node.next.set_prev(node.prev) 
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        
        cur_node = self.head
        cur_max = self.head.value

        while cur_node is not None:
            if cur_node.value is None:
                return cur_max
            elif cur_node.value > cur_max:
                cur_max = cur_node.value
            cur_node = cur_node.next

        return cur_max