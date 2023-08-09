class Empty(Exception):
  """ Error attempting to access an element from an empty container. """
  pass

class ArrayStack:
  def __init__(self):
    """ Create an empty stack. """
    self._data = []   # Initiate a nonpublic list instance
  
  def __len__(self):
    """ Return the number of elements in the stack. """
    return len(self._data)
  
  def is_empty(self):
    """ Return True if the stack is empty. """
    return len(self._data) == 0
  
  def push(self, element):
    """ Add an element to the top of the stack. """
    self._data.append(element) # new item stored at end of list
  
  def top(self):
    """ Return (but do not remove) the element at the top of the stack.
    Raise an exception if the stack is empty. """
    if self.is_empty():
      print('Stack is empty')
      raise Empty('Stack is empty') # Calling subclass Empty
    return self._data[-1] # the last item in the list

  def pop(self):
    """ Remove and return the element from the top of the stack.
    Raise an exception if the stack is empty. """
    if self.is_empty():
      print('Stack is empty')
      raise Exception('Stack is empty') # Alternate way to call subclass Empty
    return self._data.pop() # remove last item from the list
  
  def pop_all(self):
    while (len(self._data) != 0):
      self._data.pop()
    pass
  
  def printStack(self):
    print(str(self._data)
          .replace('[', '')
          .replace(']', '')
          .replace(',', '')
    )    
    pass


stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.pop_all()
stack.printStack()