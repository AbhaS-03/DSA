 # 4. Find Middle Node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)
            