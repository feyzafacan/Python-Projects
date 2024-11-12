# BASIC ARRAY EXERCISES

import array

my_array = array.array("i", [1,2,3,4,5])

# reverse
def reverse_array(arr):
    arr.reverse()
    return arr
    
print(reverse_array(my_array))

# max min
def max_min(arr):
    maximum = max(arr)
    minimum = min(arr)
    return maximum, minimum

min_val, max_val = max_min(my_array)
print("max: ", max_val)
print("min: ", min_val)

# rotate
my_array = array.array("i", [1,2,3,4,5])
def rotate(arr, n):
    n = n % len(arr)
    for i in range(n):
        last_elem = arr.pop()
        arr.insert(0,last_elem)
    return arr
print(rotate(my_array,2))
    
    
# LINKED LIST EXERCISES

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):   # print list
        current = self.head
        while current:
            print(current.data, end = "-> ")
            current = current.next 
        print("None")   
        
    def adding(self,data):  # add elements
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete_node(self,key): # delete node
        current =self.head
        
        # if we delete the node head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        # others
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        # not found
        if current is None:
            print("Not found.")
            return
        #delete node
        prev.next = current.next
        current = None
        
linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)

linked_list.head.next = second
second.next = third


linked_list.adding(4)  # added 4 to the head
linked_list.print_list() 

linked_list.delete_node(4) # delete node 4
linked_list.print_list() 