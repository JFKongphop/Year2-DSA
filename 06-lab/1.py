class BST_Node:
  def __init__(self, key, val, left=None, right=None, parent=None):
    self._key = key
    self._value = val
    self._leftChild = left
    self._rightChild = right
    self._parent = parent

  def hasLeftChild(self):
    return self._leftChild

  def hasRightChild(self):
    return self._rightChild

  def isLeftChild(self):
    return self._parent and self._parent._leftChild == self

  def isRightChild(self):
    return self._parent and self._parent._rightChild == self

  def isRoot(self):
    return not self._parent

  def isLeaf(self):
    return not (self._rightChild or self._leftChild)

  def hasAnyChildren(self):
    return self._rightChild or self._leftChild

  def hasBothChildren(self):
    return self._rightChild and self._leftChild

  def replaceNodeData(self, key, value, lc, rc):
    self._key = key
    self._value = value
    self._leftChild = lc
    self._rightChild = rc
    if self.hasLeftChild():
      self._leftChild._parent = self
    if self.hasRightChild():
      self._rightChild._parent = self



class BinarySearchTree:
  def __init__(self):
    self._root = None
    self._size = 0

  def length(self):
    return self._size

  def __len__(self):
    return self._size
  
  def __iter__(self):
    return self._root.__iter__()

  def is_empty(self):
    return self._size == 0
  
  def treeSearch(self, target):
    if not self.is_empty():
      result = self._treeSearch(self._root, target)
      return result._value
    else:                                         
      return None

  def _treeSearch(self, currentNode, target):
    if currentNode == None:
      return None
    elif target == currentNode._key:
      return currentNode
    elif target < currentNode._key:
      return self._treeSearch(currentNode._leftChild, target)
    elif target > currentNode._key:
      return self._treeSearch(currentNode._rightChild, target)
    
  def findMin(self):
    if not self.is_empty():
      return self.findMin_re(self._root)

    else:
      return None    

  def findMax(self):
    if not self.is_empty():
      return self.findMax_re(self._root)

    else: 
      return None  

  def findMin_re(self, root):
    while root._leftChild is not None:
      root = root._leftChild
    return (root._key,root._value)                     
  
  def findMax_re(self, root):
    while root._rightChild is not None:
      root = root._rightChild
    return(root._key, root._value)

  def treeInsert(self, key, value):
    if not self.is_empty():                        
      self._treeInsert(key, value, self._root) 

    else:
      self._root = BST_Node(key,value) 

    self._size = self._size + 1
  
  def _treeInsert(self, key, value, currentNode):
    if key < currentNode._key:
      if currentNode._leftChild is None:
        currentNode._leftChild = BST_Node(key, value, parent=currentNode)
      else:
        self._treeInsert(key, value, currentNode._leftChild)
    elif key > currentNode._key:
      if currentNode._rightChild is None:
        currentNode._rightChild = BST_Node(key, value, parent=currentNode)
      else:
        self._treeInsert(key, value, currentNode._rightChild)
    else:
      currentNode.u = value
  
  def insertList(self,list):
    for l in list:
      self.treeInsert(l[0],l[1])
    
  def preorder(self, root):
    if root != None:
      print("->",root._key, end = " ")
      self.preorder(root._leftChild)
      self.preorder(root._rightChild)

  def inorder(self, root):
    if self:
      if root._leftChild:
        self.inorder(root._leftChild)

      print("->",str(root._key), end = ' ')

      if root._rightChild:
        self.inorder(root._rightChild)

  def postorder(self, root):
    if self:
      if root._leftChild:
        self.postorder(root._leftChild)

      if root._rightChild:
        self.postorder(root._rightChild)

      print("->",str(root._key), end = ' ')

  def traverse(self):
    if self.is_empty():
      print("This is an empty tree.")
    else:
      print("Preorder: ")
      self.preorder(self._root)
      print("\nInorder: ")
      self.inorder(self._root)
      print("\nPostorder: ")
      self.postorder(self._root)
      print("")
  
  
  def deleteNode(self, key):  
    if self._size > 1:                     
      node = self._treeSearch(self._root, key)
      if node is not None:
        self._deleteNode(node)
        self._size = self._size-1
      else:
        raise KeyError('Key not found')
      
    elif self._size == 1 and self._root._key == key:
      self._root = None
      self._size = 0

    else:
        raise KeyError('Key not found')
  
  def _deleteNode(self, currentNode):
    ########################
    ## Add your code here
    ########################
    pass

BST_test = BinarySearchTree()

BST_test.treeInsert(5, 'Middle Earth')
BST_test.treeInsert(7, 'Shire')
BST_test.treeInsert(9, 'Rohan')
BST_test.treeInsert(2, 'Gondor')

# Search for key, return the found value
print(BST_test.treeSearch(5))
print(BST_test.treeSearch(9))
print(BST_test.traverse())
print(BST_test.findMin())
print(BST_test.findMin_re(BST_test._root))
print(BST_test.findMax_re(BST_test._root))

print(BST_test._root._key)

myBST = BinarySearchTree()
myBST.insertList([
  [14,'Frodo'], 
  [23,'Samwise'], 
  [7,'Merry'], 
  [10,'Pippins'], 
  [33,'Arwen'], 
  [5,'Galadriel'], 
  [20,'Sauron']]
)

myBST.traverse()

print("Min: ", myBST.findMin())
print("Max: ", myBST.findMax())