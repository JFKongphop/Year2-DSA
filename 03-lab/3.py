import numpy as np
import time
import matplotlib.pyplot as plt

class ArrayList:
  def __init__(self):
    self.data = np.empty(1, dtype=object)
    self.size = 0


class ArrayList:
  def __init__(self):
      self.data = np.empty(1, dtype=object)
      self.size = 0


  def append(self, value, doubling=True):
    if len(self.data) == self.size and doubling == True:
      new_data = np.empty(2*self.size,dtype = object)
      for i in range(self.size):
        new_data[i]  = self.data[i]
      self.data = new_data
    elif len(self.data) == self.size and doubling == False:
      new_data = np.empty(1000+self.size,dtype = object)
      for i in range(self.size):
        new_data[i]  = self.data[i]
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
  

ns = np.linspace(10, 10000, 50, dtype=int)
t2 = []
ts1 = []

for i in ns:
  l1 = ArrayList()
  l2 = ArrayList()

  st_time1 = time.time()
  for _ in range(10):
    for a in range(i):
      l1.append(a, doubling=False)
  end_time1 = time.time()
  ts1.append(end_time1 - st_time1)
  
  st_time2 = time.time()
  for _ in range(10):
    for b in range(i):
      l2.append(a, doubling=True)
  end_time2 = time.time()
  t2.append(end_time2 - st_time2)
plt.plot(ns,t2,"or")
plt.plot(ns,ts1,"ob")
plt.show()

