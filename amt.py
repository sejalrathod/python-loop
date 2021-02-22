amt=0
num=int(input("enter a electric unit"))
if num<=100:
    amt=0
    if num>100 and num<=200:
        amt=500+(num-200)*10
        print("amount to pay",amt)
        