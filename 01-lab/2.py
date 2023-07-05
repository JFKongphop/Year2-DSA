def is_even(k) -> bool:
  if k < 0: k *= -1
  while k > 1:
    k -= 2
  print(k == 0)
  
is_even(-1)
    
