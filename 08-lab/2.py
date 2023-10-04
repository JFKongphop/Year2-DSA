def bubbleSort_card(alist):
  print("Original list: ", alist, "\n")
  no_compare = 0
  no_exchange = 0

  suit_order = {'♣': 0, '♦': 1, '♥': 2, '♠': 3}
  rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

  print("Original list: ", alist, "\n")
  no_compare = 0
  no_exchange = 0
  count=0

  n = len(alist)
  for pass_num in range(n):
    for i in range(n-1,pass_num,-1):
      key1 = str(alist[i-1])[-1]
      value1 = str(alist[i-1])[:-1]
      key2 = str(alist[i])[-1]
      value2 = str(alist[i])[:-1]

      no_compare += 1
      if (rank_order[value1] > rank_order[value2]) or (rank_order[value1] == rank_order[value2] and suit_order[key1] > suit_order[key2] ):
        no_exchange += 1
        alist[i], alist[i - 1] = alist[i - 1], alist[i]



  print("Sorted list: ", alist)
  print("Number of Comparisons: ", no_compare)
  print("Number of Exchanges: ", no_exchange)

# inputList = ['4♣','A♣','10♥','K♦','4♠','10♣','3♦','7♥','4♦']
# bubbleSort_card(inputList)
# print(inputList)

def selectionSort_card(alist):
  print("Original list: ", alist, "\n")
  suit_order = {'♣': 0, '♦': 1, '♥': 2, '♠': 3}
  rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

  print("Original list:", alist, "\n")

  no_compare = 0
  no_exchange = 0
  count=0
  n = len(alist)

  for i in range(n - 1):
    min_index = i
    key_min = str(alist[i])[-1]
    value_min = str(alist[i])[:-1]

    for j in range(i + 1, n):
      key_min = str(alist[min_index])[-1]
      value_min = str(alist[min_index])[:-1]
      key = str(alist[j])[-1]
      value = str(alist[j])[:-1]

      no_compare += 1

      if ((rank_order[value_min] > rank_order[value] ) or (rank_order[value_min]) == rank_order[value] and suit_order[key_min] > suit_order[key] ) :
        min_index = j

      if i != min_index:
        no_exchange += 1
        alist[i], alist[min_index] = alist[min_index], alist[i]

  print("Number of Comparisons: ", no_compare)
  print("Number of Exchanges: ", no_exchange)

# inputList = ['4♣','A♣','10♥','K♦','4♠','10♣','3♦','7♥','4♦']
# selectionSort_card(inputList)
# print(inputList)

def insertionSort_card(alist):
  suit_order = {'♣': 0, '♦': 1, '♥': 2, '♠': 3}
  rank_order = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

  print("Original list:", alist, "\n")
  no_compare = 0
  no_exchange = 0
  count = 0
  n = len(alist)

  for i in range(1, n):
    key = alist[i]
    key_suit = key[-1]
    key_rank = key[:-1]

    j = i - 1
    while j >= 0 and ((rank_order[key_rank] == rank_order[alist[j][:-1]] and (suit_order[key_suit] < suit_order[alist[j][-1]])) or (rank_order[key_rank] < rank_order[alist[j][:-1]])):
      no_compare += 1
      no_exchange += 1
      alist[j + 1] = alist[j]
      j -= 1

    alist[j + 1] = key

    # print('Round:', count + 1)
    # print('Position to insert:', i)
    # print('Current List:', alist)
    # count += 1

  print("Sorted list:", alist)
  print("Number of Comparisons:", no_compare)
  print("Number of Exchanges:", no_exchange)



inputList = ['4♣','A♣','10♥','K♦','4♠','10♣','3♦','7♥','4♦']
insertionSort_card(inputList)
print(inputList)