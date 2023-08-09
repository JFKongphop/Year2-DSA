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


class ArrayQueue:
  DEFAULT_CAPACITY = 10   # moderate capacity for all new queues

  def __init__(self):
    """ Create an empty queue with specified size. """
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0
    self._rear = 0
  
  def __len__(self):
    """ Return the number of elements in the queue. """
    return self._size
  
  def is_empty(self):
    """ Return True if the queue is empty. """
    return self._size == 0
  
  def first(self):
    """ Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]
  
  def dequeue(self):
    """ Remove and return the first element of the queue.
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None          # Reclaiming unused space
    self._front = (self._front + 1) % len(self._data) # shift the location of the front index rightward
    self._size -= 1
    return answer
  
  def enqueue(self, e):
    """ Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2*len(self._data))    # double the array size when all slots are occupied.
    if self._rear == 0 and self._data[0] == None: # For the first case of rear = 0 and no data in Q[0] - Empty Queue
      self._data[self._rear] = e
    else:
      self._rear = (self._rear + 1) % len(self._data) # shift the location of the rear index rightward
      self._data[self._rear] = e
    self._size += 1                     # Keep track of number of elements in ArrayQueue

  
  def _resize(self, cap):               # Assume cap >= len(self)
    """ Resize to a new list of capacity >= len(self). """
    old = self._data                    # keep track of existing list
    self._data = [None] * cap           # allocate list with new capacity
    walk = self._front
    for k in range(self._size):         # consider existing elements
      self._data[k] = old[walk]         # Shift indices to start at 0
      walk = (1 + walk) % len(old)      # use old size as modulus
    self._front = 0                     # front has been realigned
    self._rear = self._size - 1         # rear has been realigned
  

  def deQueueAll(self):
    self._data = []
    pass

  def printQueue(self):
    return self._data

def copyStackToQueue(stack1: ArrayStack, queue2: ArrayQueue):
  while (len(queue2.printQueue()) != 0):
    queue2.dequeue()
  i = 0
  while i != stack1.__len__():
    try:
      queue2.enqueue(stack1.top())
      stack1.pop()
      i += 1

    except:
      break  

  p = []
  a = list(filter(lambda x: x is not None, queue2.printQueue()))

  for i in range(len(a) -1, -1, -1):
    p.append(a[i])


  print(p)


stack1 = ArrayStack(); stack1.push(10); stack1.push(20); stack1.push(30)    
queue2 = ArrayQueue(); 
queue2.enqueue(99)


copyStackToQueue(stack1, queue2)