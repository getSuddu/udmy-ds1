class Node:
    def __init__(self, val=0):
        self.value=val
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            #since it is circular; need to break when last node pointing back to first, by comparing last node ref against tail.next 
            if node==self.tail.next:  #last node ref == last stored in tail ref
                break
    
    #CREATION of circ singleLinkedList
    def create_csll(self, nodeval):
        node=Node(nodeval)        
        node.next=node
        self.head=node
        self.tail=node
        #print('CSLL is created')
        return 'CSLL is created'
    
    #INSERTION
    def insert_csll(self, nodeval, loc): #insert node based on a specified pos
        if self.head==None:
            return "CSLL does not exist"        
        newNode = Node(nodeval)
        #insert new node in the beg
        if loc==1: 
            newNode.next=self.head
            self.head=newNode
            self.tail.next=newNode #lastnode ref to first
        
        

    
circ_sing_LL = CSLL()
print(circ_sing_LL.create_csll(1))
print([node.value for node in circ_sing_LL])







        
