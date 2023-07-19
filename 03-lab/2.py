import numpy as np

class ArrayList:
  def __init__(self):
    self.data = np.empty(1, dtype=object)
    self.size = 0



  def append(self, value):
    if len(self.data) == self.size:
      new_data = np.empty(2 * self.size, dtype=object)
      for i in range(self.size):
        new_data[i] = self.data[i]
      self.data = new_data
    self.data[self.size] = value
    self.size += 1


  def __getitem__(self, idx):
    """Implements `x = self[idx]`"""
    assert isinstance(idx, int), 'Index must be an integer'
    if idx < 0:
        idx += self.size
    if idx < 0 or idx >= self.size:
        raise IndexError('list index out of range')
    return self.data[idx]


  def __setitem__(self, idx, value):
    """Implements `self[idx] = x`"""
    assert isinstance(idx, int), 'Index must be an integer'
    if idx < 0:
        idx += self.size
    if idx < 0 or idx >= self.size:
        raise IndexError('list index out of range')
    self.data[idx] = value


  def __delitem__(self, idx):
    """Implements `del self[idx]`"""
    assert isinstance(idx, int), 'Index must be an integer'
    if idx < 0:
      idx += self.size
    if idx < 0 or idx >= self.size:
      raise IndexError('list index out of range')
    for i in range(idx, self.size-1):
      self.data[i] = self.data[i+1]
    self.size -= 1


  def __len__(self):
    """Implements `len(self)`"""
    return self.size


  def __repr__(self):
    """Supports inspection"""
    return '[' + ','.join(repr(self.data[i]) for i in range(self.size)) + ']'
  

l1 = ArrayList()
for x in range(10):
  l1.append(x)
  print(l1.data)
