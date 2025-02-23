#Ctreate a Linked List 1-2-3-4-5

class Node:
    def __init__(self, val=0):    
        self.value=val
        self.next=None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node is not None:            
            yield node
            node=node.next

#build linked list 1-2-3-4-5
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
MyLL=LL()
MyLL.head = node1
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5 #5.next=none; by default
MyLL.tail=node5
print("My Existing Linked List ", [node.value for node in MyLL])







