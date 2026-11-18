def delfirst_last(self):
    temp1=self.head
    temp1=None
    prev=None
    temp = self.head= self.head.next
    while(temp.next):
        prev=temp
        temp=temp.next
    prev.next=None
    temp=None

    