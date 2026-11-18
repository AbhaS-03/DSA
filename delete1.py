class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# --- Test Run ---
list1 = SLL()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

print("Original:")
list1.print()          # 10 -> 20 -> 30 -> 40 -> None

list1.delete_first()
print("After Deleting First:")
list1.print()          # 20 -> 30 -> 40 -> None

list1.delete_last()
print("After Deleting Last:")
list1.print()          # 20 -> 30 -> None
