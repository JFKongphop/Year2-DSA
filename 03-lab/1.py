import time


def first(nums: list[int]):
  for n in nums:
    start = time.time()
    data = [] 
    for i in range(n):
      data.insert(0, 20)
    end = time.time()
    print(end - start)
  print('end')

def mid(nums: list[int]):
  for n in nums:
    start = time.time()
    data = []
    for i in range(n):
      l = len(data) // 2
      data.insert(l, 20)
    end = time.time()
    print(end - start)
  print('end')

def last(nums: list[int]):
  for n in nums:
    start = time.time()
    data = []
    for i in range(n):
      l = len(data)
      data.insert(l - 1, 20)
    end = time.time()
    print(end - start)
  print('end')


nums = [100, 1000, 10000, 100000, 1000000]
first(nums)
mid(nums)
last(nums)
