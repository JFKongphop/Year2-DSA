class Item:
  def __init__(self, name, price, weight):
    self.name = name
    self.price = price
    self.weight = weight

  def getName(self):
    return self.name

  def getPrice(self):
    return self.price

  def getWeight(self):
    return self.weight

  def getCost(self):
    return self.price / self.weight
  
def knapsack(amount, itemList):
  itemList.sort(key=lambda item: item.getCost(), reverse=True)#sort by getcost
  selected_items = []
  total_value = 0
  total_weight = 0

  for item in itemList:
    if total_weight + item.getWeight() <= amount:
      selected_items.append(item)
      total_value += item.getPrice()
      total_weight += item.getWeight()

  if not selected_items:
    return "No item taken, knapsack remains empty"
  else:
    return selected_items, total_value
    
item1 = Item('stereo', 3000, 3)
item2 = Item('laptop', 2000, 2)
item3 = Item('guitar', 1500, 1.5)
itemList = [item1, item2, item3]

result = knapsack(3.5, itemList)

print("Selected item:")
for i in result[0]:
  print(i.getName(), "->", i.getWeight(), "kg", "->", i.getPrice(), "THB")

item1 = Item('tablet', 7000, 0.5)
item2 = Item('perfume', 6000, 0.5)
item3 = Item('guitar', 9000, 1)
item4 = Item('air purifier', 9000, 2)
item5= Item('watch', 8000, 0.5)
itemList = [item1, item2, item3, item4, item5]
result = knapsack(3.5, itemList)

print("Selected item:")
for i in result[0]:
  print(i.getName(), "->", i.getWeight(), "kg", "->", i.getPrice(), "THB")