def linear_search(data, target):
  for i in range (len(data)):
    if data[i] == target:
      print(i)
      return True
  return False

data = [10,20,40,50]
linear_search(data,40)


def binary_search_iterative(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + low) // 2

    if x > arr[mid]:
      low = mid + 1

    elif x < arr[mid]:
      high = mid - 1
    else:
      print(mid)
      return True

  return False

binary_search_iterative(data,40)
binary_search_iterative(data,100)