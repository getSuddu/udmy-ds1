
class avlNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hight = 1
    
    def preordertraversal(rootNd): #root-> l -> r
        if not rootNd: #rootNd!=None
            return
        print(rootNd.data)
        preordertraversal(rootNd.left)
        preordertraversal(rootNd.right)
    
    def inordertraversal(rootNd): # l -> root -> r 
        if not rootNd:
            return
        inordertraversal(rootNd.left)
        print(rootNd.data)
        inordertraversal(rootNd.right)

    def postordertraversal(rootNd): # l-> r -> root
        if not rootNd:
            return
        postordertraversal(rootNd.left)
        postordertraversal(rootNd.right)
        print(rootNd.data)

# Insertion in AVL tree -> 1. rotation - when hight is more than 1; 2. No rotation -> H =(-1, 0, 1)
# Rotation types -> know using path to Grandchild; if 2 GC; then pick one with more hight 
# a. LL condition --> Right rotation of imbalanced root node; make as child of its child to the right  
# b. LR condition --> Left rotation of leftchild -> result is now LL -> Do Right rotation
# c. RR condition --> Left rotation to bring root down to left
# d. RL condition --> Right rot to its right child --> result is now RR --> Do left rot to balance

def gethight(node):
    if not node:
        return 0
    return node.height

def rotateleft(imbalncednode): #RR condition - bring root down to left
    newroot = imbalncednode.right
    imbalncednode.right = imbalncednode.right.left
    newroot.left = imbalncednode
    imbalncednode.height = 1 + max(gethight(imbalncednode.left), gethight(imbalncednode.right))
    return newroot

def rotateright(imbalancenode): # LL condition - bring root down to right
    newroot = imbalancenode.left
    imbalancenode.left = imbalancenode.left.right
    newroot.right=imbalancenode
    imbalancenode.hight = 1 + max(gethight(imbalancenode.left), gethight(imbalancenode.right))
    return newroot

def calcBalance(node):
    if not node:
        return 0
    return gethight(node.left) - gethight(node.right)

def insertNode(Node, nodeval):
    if not Node: # create first node rootnode
        return avlNode(nodeval)
    elif nodeval < Node.data: #insert on leftside
        Node.left = insertNode(Node.left, nodeval) #add val to the left
    else:
        Node.right = insertNode(Node.right, nodeval)
    
    # Update hight of the inserted node
    Node.height = 1 + max(gethight(Node.left), gethight(Node.right))
    balance= calcBalance(Node) #check if hight is not o,-1,1; for imbalance tree and hence do rotation
    if balance > 1 and nodeval<Node.left.data: #left Heavy; and LL condition
        return rotateright(Node) # rotate right
    elif balance > 1 and nodeval>Node.right.data: #left Heavy; and LR condition
        rotateright(Node.)
        return 
    elif balance < -1 and nodeval>Node: #Right Heavy; and RR condition
    elif balance < -1 and nodeval<Node: #Right Heavy; and RL condition


