temp = int(input("enter temparature  in celcous:"))
humid  = int (input("enter  humidty   in pervetge :"))
if temp>=30and humid>=90:
  print("hot  and humid")
elif temp>=30and hummid<90:
  print("hot")
elif temp<30and humid>=90:
  print("cold  and humid")
else:
  print("cold")
  