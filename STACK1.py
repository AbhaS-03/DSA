class Node:
    def __init__(self, value):  # Fixed: Double underscores
        self.data = value
        self.next = None

class Stack:                    # Capitalized for standard naming conventions
    def __init__(self):
        self.top = None
        
    def isempty(self):
        return self.top is None
        
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        temp = self.top
        print("Popped element:", temp.data)
        self.top = self.top.next
        return temp

    def reverse(self):
        # In-place linked list reversal logic
        prev = None
        current = self.top
        while current:
            next_node = current.next  # Save next
            current.next = prev       # Reverse pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        self.top = prev               # Update top pointer

    def display(self):               # Renamed from 'print' to avoid built-in conflicts
        temp = self.top
        print("Stack elements (Top -> Bottom):")
        if not temp:
            print("Empty")
            return
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# --- Testing Execution ---
st = Stack()
st.push(Node(10))
st.push(Node(87))
st.push(Node(100))
st.push(Node(110))
st.push(Node(1099))
st.push(Node(12))

st.display()

st.pop()
st.display()

print("\n--- Reversing Stack ---")
st.reverse()
st.display()
