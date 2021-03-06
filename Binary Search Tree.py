class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                insert(root.r_child, node)
                
def search(root, value):
    
    if node is None:
        return Node(value)

    if value < root.data:
        root.l_child = insert(root.l_child, value)
    else:
        root.r_child = insert(root.r_child, value)
    return root

def minimum(node):
    current = node
 
    while(current.l_child is not None):
        current = current.l_child 
 
    return current 

def delete(root, node):
    
    if root is None:
        return root 
 
    if (node < root.data):
        root.l_child = delete(root.l_child, node)
 
    elif(node > root.data):
        root.r_child = delete(root.r_child, key)
 
    else:
         
        if root.l_child is None :
            inorder_pred = root.r_child 
            root = None
            return inorder_pred
             
        elif root.r_child is None :
            inorder_pred = root.l_child
            root = None
            return inorder_pred
 
        inorder_pred = minimum(root.r_child)
 
        root.data = inorder_pred.data
 
        # Delete the inorder successor
        root.r_child = delete(root.r_child , inorder_pred.data)
 
 
    return root 
    
def traversal(root):
    left = root.l_child
    right = root.r_child
    while left != None:
        traversal(left)
        print left
    
    print root[0]
    
    while right != None: 
        traversal(right)
        print right

traversal(9)
