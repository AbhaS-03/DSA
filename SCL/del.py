def delete(self,value):
    temp= self.head
    prev= None
    if temp.data == value:
        self.head= self.head.next
        while temp.next != self.head:
            temp=temp.next
        self.head= self.head.next
        temp.next = self.head
    else:
        while(temp.data != value and temp):
            prev = temp
            temp = temp.next
            if temp ==self.head:
                print("Value is not present in the list")
                return
            prev.next = temp.next
            temp=None