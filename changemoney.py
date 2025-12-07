def getinput(promt, price=None):
  while True:
    try:
       val = float(input(promt))
       if price is not None and val <= price:
          print("เงินลูกค้าไม่พอ")
       else:
          return val
    except ValueError:
      print("try put num")

num1 = getinput("ราคาของ : ")
num2 = getinput("เงินลูกค้า : ", num1)

money_type = [1000, 500, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25]
allbank = {}

for i in money_type:
  if change >= i:
    xx = change // i
    allbank[i] = xx
    change %= i
  
print("\nChange breakdown:")
print(f"{num2 - num1} baht")
for money, xx in allbank.items():
  if money >= 20:
    print(f"{money} baht notes : {xx}")
  else:
    print(f"{money} baht coin : {xx}")
