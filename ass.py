
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        values = [10, 20, 30, 40, 50]

        for data in values:
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    # 2. Traverse Linked List
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


    # 3. Insert at Specific Position
    def insert(self, data, pos):
        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find Middle Node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)

    # 5. Delete Node at Specific Position
    def delete(self, pos):
        if self.head is None or pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # 6. Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 7. Sum of Every Two Consecutive Nodes
    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data, "+", temp.next.data, "=",
                  temp.data + temp.next.data)
            temp = temp.next


# Main Program
ll = LinkedList()

ll.create()

print("1. Original Linked List:")
ll.traverse()

print("\n2. Insert 25 at position 3:")
ll.insert(25, 3)
ll.traverse()

print("\n3. Middle Node:")
ll.middle()

print("\n4. Delete node at position 2:")
ll.delete(2)
ll.traverse()

print("\n5. Reverse Linked List:")
ll.reverse()
ll.traverse()

print("\n6. Sum of Consecutive Nodes:")
ll.pair_sum()
