def isIntersect_1(a, b, c):
  s = []
  for i in a:
    for j in b:
      for k in c:
        if i == j == k:
          s.append(i)
  return len(set(s)) != 0

print(isIntersect_1([50,30], [30,40],[20,40]))


def isIntersect_2(a, b, c):
  d = set(a).intersection(set(b))
  s = []
  for i in d:
    for j in c:
      if i == j:
        s.append(i)
  return len(set(s)) != 0

print(isIntersect_2([50,30], [30,40],[30,40]))