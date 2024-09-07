#£5,£20,£50,£10
#£380
#£385 385//50 125//50
user1 = int(input("Please enter your balance: £")) 
count = user1 in range (1,6)
note50 = user1//50
note20 = (user1%50)//20
balance20 = user1%50

note10 =(balance20%50)//10
balance10 = user1%5
note5 = (balance10%5)
    
print(f"Your {user1}money requires,{note50},£50 {note20},£20 {count},£10 {note5},£5")