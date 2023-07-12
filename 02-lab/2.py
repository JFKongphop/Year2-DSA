import numpy as np
import time
import matplotlib.pylab as plt

def linear_search1(lst:list, x:int):
  return x in lst

def linear_search2(lst:list, x:int):
  for i in (lst):
    if x == i:
      return True
  return False


ns2 = np.linspace(1000, 10000, 100, dtype=int)
ts2 = []
for n in ns2:
    nd = list(range(n))
    start = time.time()
    linear_search2(nd, 3)
    end = time.time()
    ts2.append(end - start)

plt.plot(ns2, ts2, 'or')
plt.show()