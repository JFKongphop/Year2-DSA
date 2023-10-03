class Hashtable:
  def __init__(self, n_buckets):
    self.buckets = [None] * n_buckets

  def __setitem__(self, key, val):
    bidx = hash(key) % len(self.buckets)
    self.buckets[bidx] = [key, val]

  def __getitem__(self, key):
    bidx = hash(key) % len(self.buckets)
    if self.buckets[bidx] is not None:
      print(self.buckets[bidx][1]) 
    else:
      raise KeyError(key)

  def __contains__(self, key):
    try:
      _ = self[key]
      print(True)
    except:
      print(False)

  def insertData(self, key, val):
    bidx = hash(key) % len(self.buckets)
    base = bidx
    collisions = 0
    while self.buckets[bidx] is not None:
      if self.buckets[bidx][0] == key:
        self.buckets[bidx][1] = val
        print()
      collisions += 1
      bidx = (base + collisions) % len(self.buckets)
      if collisions == len(self.buckets):
        print("Bucket is Full") 
    self.buckets[bidx] = [key, val]
    print("Index = ",bidx)

  def searchData(self, key):
    collisions = 0
    bidx = hash(key) % len(self.buckets)
    base = bidx

    while self.buckets[bidx] is not None:
      if self.buckets[bidx][0] == key:
        print(self.buckets[bidx][1],"at",bidx)
        print(True) 
      collisions += 1
      bidx = (base + collisions) % len(self.buckets)
      if collisions == len(self.buckets):
        print(False) 
    print(False) 
        
ht = Hashtable(75)
ht.insertData(175, 'Tony Stark')
ht.insertData(100, 'Steve Rogers')
ht.insertData(275, 'Peter Parker')

ht.searchData(175)
ht.searchData(100)
ht.searchData(275)
ht.searchData(300)