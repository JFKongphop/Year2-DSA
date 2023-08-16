class NumberNode:
  def __init__(self, element, next):
    self._element = element
    self._next = next

class Empty(Exception):
  """ Error attempting to access an element from an empty container. """
  pass

class LinkedStack:
  class _Node:
    def __init__(self, element, next_node=None):
      self._element = element
      self._next = next_node

  def __init__(self):
    """ Create an empty stack. """
    self._head = None
    self._size = 0

  def __len__(self):
    """ Return the number of elements in the stack. """
    return self._size

  def is_empty(self):
    """ Return True if the stack is empty."""
    return self._size == 0

  def push(self, e):
    """ Add element e to the top of the stack as a new head node. """
    new_node = self._Node(e, self._head)
    self._head = new_node
    self._size += 1

  def top(self):
    """ Return (but not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
        raise Empty("Stack is empty")
    return self._head._element

  def pop(self):
    """ Remove and return the element from the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
        raise Empty("Stack is empty")
    popped_element = self._head._element
    self._head = self._head._next
    self._size -= 1
    return popped_element

  def printStack(self):
    current = self._head

    if current is None:
      print("Stack is empty")
      return
    while current._next:
      print(current._element, end=" -> ")
      current = current._next
    print(current._element)

S = LinkedStack()
S.push(7)
S.push(5)   
print(f'Number of elements: {len(S)}')

print(f'Remove item: {S.pop()}')          
print(f'Is stack empty?: {S.is_empty()}') 
print(f'Remove item: {S.pop()}')         
print(f'Is stack empty?: {S.is_empty()}')