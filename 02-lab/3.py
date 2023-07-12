import time, random
import matplotlib.pyplot as plt
import numpy as np

def isinter1(a, b, c):
  inter1 = []
  for i in a:
    for j in b :
      for k in c:
        if i == k == j:
          inter1.append(k)
  if len(set(inter1)) == 0:
    return False
  return True

ns3 = np.linspace(10, 1000, 100, dtype=int)
ts3 = []

for n in ns3:
  a = [random.randint(0, 100) for _ in range(random.randint(0,n))]
  b =[random.randint(0, 100) for _ in range(random.randint(0,n))]
  c = [random.randint(0, 100) for _ in range(random.randint(0,n))]
  start = time.time()
  isinter1(a, b,c)
  end = time.time()
  ts3.append(end - start)
plt.plot(ns3,ts3,"or")
plt.show()