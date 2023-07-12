import time, random
import matplotlib.pyplot as plt
import numpy as np

def isinter1(a, b, c):
  inter1 = []
  for i in a:
    for j in b :
      for k in c:
        if i == k == j:
          return len(set(inter1)) != 0

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


def isinter2(a, b, c):
  inter2 = (set(a)& set(b))
  inter_used = []
  for i in inter2:
    for j in c :
        if i  == j:
          return len(set(inter_used)) != 0

a = [random.randint(0, 100) for _ in range(100)]
b =[random.randint(0, 100) for _ in range(100)]
c = [random.randint(0, 100) for _ in range(100)]
ns4 = np.linspace(10, 1000, 100, dtype=int)
ts4 = []
for n in ns4:
    th = list(range(n))
    start = time.time()
    isinter2(a, b,c)
    end = time.time()
    ts4.append(end - start)
plt.plot(ns4,ts4,"oc")
plt.show()