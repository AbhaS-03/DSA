#Singly Linear linked list
class Node:
    def __init__(self, value):
        self.prev=None
        self.data = value
        self.next = None
class DDL:
    def __init__(self):
        self.head = None
    def append(self,new_node):
        if (self.head == None): #first node
            self.head= new_node
        else:
            temp = self.head
            while (temp.next):
                temp= temp.next
            temp.next = new_node
            new_node.prev = temp

    
    def insert(self,new_node, pos):
        if pos == 1: # insert node at first position
            new_node.next= self.head
            self.head = new_node
            self.head.prev = new_node
            self.head= new_node
        else:# at any postion
            p=1
            temp= self.head
            while(p != pos-1 and temp.next):
                temp = temp.next
                p+=1
            if temp.next: #last 
                temp.next.prev = new_node
            new_node.prev= temp
            new_node.next=temp.next
            temp.next=new_node
            #temp,next.prev =new_node
            #new_node.pre= temp
            
    def delete (self,value):
        temp = self.head
        if temp.data == value : # first node to delete
            self.head = temp.next
            self.head.prev = None
        else:
            while (temp.data != value and temp ):
                temp = temp.next
                if temp == None:
                    print("Value is not present")
                    return
            temp.prev.next = temp.next
            if temp.next: # not last node
                temp.next.prev = temp.prev
                temp = None
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def printrev(self):
        temp =self.head
        print("\n List elements in reverses order", end =" ")
        while temp.next:
            temp= temp.next
        while temp:
            print(temp.data, end = "")
            temp = temp.prev
    # to count occurence of a given no in ddl
    def count():
        
list1= DDL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()
list1.insert(Node(74),10)

list1.print()
list1.delete(174)
list1.print()
list1.printrev()

