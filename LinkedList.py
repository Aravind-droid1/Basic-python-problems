class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def prepend(self,data):
        new_node=Node(data)
        current=self.head
        if(current is None):
            self.head=new_node
            self.tail=new_node
            
        else:
            self.head=new_node
            new_node.next=current

    def search(self,data):
        current=self.head
        while current:
            if(current.data==data):
                return "Yes",current
            else:
                current=current.next
        return "No"
    
    def delete(self,data):
        current=self.head
        prev=None
        while current:
            if(current.data==data):
                if self.head.next is None:
                    self.head=None
                    self.tail=None
                elif current==self.head:
                    self.head=current.next
                elif current.next==None:
                    prev.next=None
                    self.tail=prev
                else:
                    prev.next=current.next
                return
            prev=current
            current=current.next

    def rev(self):
        current=self.head
        prev=None
        self.tail=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    def middle(self):
        current=self.head
        count=0
        while current:
            current=current.next
            count+=1

        current=self.head
        n=count//2
        for i in range(n):
            current=current.next
        return current
        
    def __str__(self):
        result="Head->"
        current=self.head
        while current:
            result+=str(current.data)+"->"
            current=current.next
        return result+"None"

l1=LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
print(l1)
l1.prepend(0)
print(l1)
print(l1.search(2))
print(l1.search(6))
l1.delete(2)
print(l1)
l1.rev()
print(l1)
mid=l1.middle()
print(mid.data)
