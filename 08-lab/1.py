def bubbleSort(alist):
  print("Original list: ", alist, "\n")
  no_compare = 0
  no_exchange = 0

  n = len(alist)

  for i in range(n - 1):
    swapped = False

    for j in range(0, n - i - 1):
      no_compare += 1

      if alist[j] > alist[j + 1]:
        alist[j], alist[j + 1] = alist[j + 1], alist[j]
        no_exchange += 1
        swapped = True

    print(f"Round {i + 1}: {alist}")

    if not swapped:
      break

  print("Number of Comparisons: ", no_compare)
  print("Number of Exchanges: ", no_exchange)



inputList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(inputList)
print(inputList)


def selectionSort(alist):
  print("Original list: ", alist, "\n")
  no_compare = 0
  no_exchange = 0

  n = len(alist)

  for i in range(n):
    min_index = i

    for j in range(i + 1, n):
      no_compare += 1
      if alist[j] < alist[min_index]:
        min_index = j

    alist[i], alist[min_index] = alist[min_index], alist[i]
    no_exchange += 1

    print(f"Round {i + 1}:")
    # print(f"  - Position to insert: {i}")
    # print(f"  - Position of selected item: {min_index}")
    print(f"  - Current list: {alist}\n")

  print("Number of Comparisons: ", no_compare)
  print("Number of Exchanges: ", no_exchange)

# inputList = [54,26,93,17,77,31,44,55,20]
# selectionSort(inputList)
# print(inputList)

def insertionSort(alist):
  print("Original list: ", alist, "\n")
  no_compare = 0
  no_exchange = 0

  n = len(alist)

  for i in range(1, n):
    current_value = alist[i]
    position = i

    # Find the correct position for the current value in the sorted part
    while (position > 0) and (alist[position - 1] > current_value):
      no_compare += 1
      alist[position] = alist[position - 1]
      position -= 1
      no_exchange += 1

    # Insert the current value into the sorted part
    print(current_value)
    alist[position] = current_value

    # Print round number, positions, and current list
    print(f"Round {i}:")
    # print(f"  - Current selected/drew value: {current_value}")
    # print(f"  - Position of current selected/drew value in unsorted area: {i}")
    # print(f"  - Position of inserted item into sorted area: {position}")
    print(f"  - Current list: {alist}")

  print("Number of Comparisons: ", no_compare)
  print("Number of Exchanges: ", no_exchange)

# inputList = [54,26,93,17,77,31,44,55,20]
# insertionSort(inputList)
# print(inputList)

# bubble sort
# https://youtu.be/xli_FI7CuzA?si=G9k5pZ446J9nU4Sq
# selection sort
# https://youtu.be/g-PGLbMth_g?si=eCryrMP5htSNWlOY
# insertion sort
# https://youtu.be/JU767SDMDvA?si=CEo0Dhr8lGf-_0in