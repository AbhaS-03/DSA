class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head  # Fixed typo: nexr -> next
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos - 1 and temp:
                temp = temp.next
                p += 1
            if temp is None:
                print("Position out of bounds")
                return
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head  # Fixed typo: tem -> temp
        
        if temp is None:
            print("List is empty")
            return

        # Case 1: The node to delete is the head node
        if temp.data == value:
            self.head = self.head.next
            return

        # Case 2: The node to delete is further down the list
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next  # Removed duplicate temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

     
        prev.next = temp.next

    def print_list(self):  # Renamed from print to avoid overriding built-in print()
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        

list1 = SLL()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original list:")
list1.print_list()

print("\nDeleting 30:")
list1.delete(30)
list1.print_list()
