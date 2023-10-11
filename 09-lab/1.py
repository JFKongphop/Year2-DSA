def coinExchange(amount, coinValueList = None, coinQuantityList = []):
  value = list(coinValueList.keys())
  quant = list(coinValueList.values())
  max_far = 0
  for i in range(len(value)):
    max_far += value[i] * quant[i]
  for i in range(len(value)):
    if amount > max_far:
      print("Not enough")
      break
    used = amount // value[i]#No. of coin
    if used > quant[i]:
      used = quant[i]
    amount -= used * value[i]
    if used != 0:
      coinQuantityList.append(used)
  for i in range(len(coinQuantityList)):
    if i == len(coinQuantityList):
      break
    print("value",value[i],"no.",coinQuantityList[i])

coinDict = {10:10, 5:10, 2:10, 1:10}
coinExchange(117, coinDict)

coinExchange(249, coinDict)