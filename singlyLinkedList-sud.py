#overall TimeComplexity for CREATING new SLL- O(1); total can be O(n) where n is the lenght of Linked list
#Space complexity for CREATING new SLL - O(1); total can be O(n) where n is the lenght of Linked list
#overall TimeComplexity for INSERTING new SLL- O(n)
#Space complexity for INSERTING new SLL - O(1)


class Node:
    def __init__(self, value=None) -> None:
        #Step1- Create a Node and assign a value & assign null reference
        self.value=value   #T-O(1)
        self.next=None

class SLinkedList:
    #Step2 - Create head and Tail and assign null value to it.
    def __init__(self):
        self.head=None   #T-O(1)
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node  ##Q- search
            node=node.next
    
    #insert in Linked List; loc=0-begining, loc=-1-End,  otherwise-Mid 
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None: #if no node exist
            self.head=newNode
            self.tail=newNode
        elif location==0: #insert element in the begining
            newNode.next=self.head #store previous first element ref stored in head to new
            self.head = newNode
        elif location==-1: #insert at the end
            #newNode.next = None #already done as part of constructor
            self.tail.next=newNode #updated current last node ref from none to newNode ref - PTR(Points to remember):-tail.next-last node ref
            self.tail=newNode #update tail ref to newNode
        else: #update node at the loc provided.
            index=0 #var to trace the index pos 
            currNode=self.head 
            #trace until location is found; inde starts with 0, loc with 1; hence -1
            while index<location-1: # T- O(n)
                currNode=currNode.next
                index+=1
            #now curr node have the pos wher we need to insert new Node
            nextNode=currNode.next
            currNode.next=newNode
            newNode.next=nextNode
            #below 2 lines is same as above 3
            #newNode.next=currNode.next
            #currNode.next=newNode
            if currNode==self.tail: #last element
                self.tail=newNode

    ### SingleLINKED list Traversal
    def traverseSLL(self):
        if self.head is None:
            print('Single linked list does not exist')
        else:
            node = self.head
            while node: # same as (node!=None): # T-O(n)
                print(node.value)
                node=node.next

    ### Search node value in SLL
    def findElemSLL(self, val):
        if self.head is None:
            print('SLL is blank; Element does not exist')
            #return "SLL does not exist" #not working for me
            return
        else:
            node=self.head
            index=0
            while node is not None:
                if (node.value==val):
                    print('Node found at pos', index+1)
                    return 
                node=node.next
                index+=1
            print("Node value {} does not exist in the List".format(val))
            #return "Node value does not exist in the List"
            return
        
    ### DELETION - based on position specified
    # Case1. beg, 2. specified mid pos, 3. End 
    # Sub Case1.NO Node, 2.only one node, 3.many node 
    def deleteSLL(self, pos): #pos=1 -beg, pos=-1 -end 
        if self.head is None: #For all- sub Case1. NO Node
            print('Single Linked List does not Exist; Can not delete')
            return
        node = self.head #read head
        if pos==1: # Case1. DELETION - Beg;
            if self.head==self.tail: #sub case2. Only one Node
                self.head=None
                self.tail=None 
            else: #sub case3. SLL has many node 
                self.head=self.head.next #update head to skip one node
        elif pos==-1: #Case3. DELETION-end
            if self.tail==self.head: #sub case2. Only one Node 
                self.head=None
                self.tail=None 
            else: #sub case3. SLL has many node 
                while (node.next!=None): #node is not None
                    beforelast=node
                    node=node.next  
                    #print('printing', beforelast.value)  #one of the other way is to compare node.nest==self.tail            
                self.tail=beforelast
                beforelast.next = None
                print("Last element is deleted.")
                return
        else: #deleting anywhere but first or lAST
            index=1
            while node: #node is not None
                if (index==pos-1):                    
                    currNode=node.next #node that need to be deleted
                    node.next=currNode.next #assign prev node to next by skipping one     
                    print(' DELETING...', index+1 , ' node. and element ',currNode.value)               
                    return
                node=node.next
                index+=1
            print("Position specified to be deleted is out of range")
            return      

singlyLL = SLinkedList() # create an object with H & T
node1=Node(1)
node2=Node(2)
node3=Node(4)
#Step3 - Link all nodes. head and tail with created node
singlyLL.head=node1  #T-O(1)
node1.next=node2 #singlyLL.head.next=node2
node2.next = node3
singlyLL.tail=node3

print('My LL',[node.value for node in singlyLL])

#INSERTION - beg
singlyLL.insertSLL(0,0)
print('Inserted at beg',[node.value for node in singlyLL])

#INSERTION - end
singlyLL.insertSLL(5,-1)
print('Inserted at end',[node.value for node in singlyLL])

#INSERTION - mid - element 3 at loc 4
singlyLL.insertSLL(3,3)
print('Inserted at mid- element 3 at loc 3',[node.value for node in singlyLL])

# call Traversal
print("SLL traversal")
singlyLL.traverseSLL()

#call Linked List Search
print('Finding an element in the SLL')
singlyLL.findElemSLL(100)

print("DELETION SLL from ", [node.value for node in singlyLL] )
#DELETION - beg

singlyLL.deleteSLL(1)
print("Post Deletion  ", [node.value for node in singlyLL] )

#DELETION - any given node
singlyLL.deleteSLL(3)
print("Post Deletion  ", [node.value for node in singlyLL] )
#DELETION - at the end of the element
singlyLL.deleteSLL(-1)
print("Post Deletion  ", [node.value for node in singlyLL] )