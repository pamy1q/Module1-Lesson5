sal_price = int(input("What is the sales price in £:"))
mark_cost= int(input("What is the original price of item in £:"))
if sal_price == mark_cost:
    print("No profit")
elif sal_price > mark_cost :
    print("Profit")
else:
    print("LOSS")


 