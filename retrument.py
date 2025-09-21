#Define the menu of restaurant

menu = {
     'PIZZA' : 40,
     'COFFE' : 80,
     'MEGGIE': 90,
     'PASTA' : 70,
     'SALAAD': 50,
}

#Greet
print("welcome to python retaurant")
print("PIZZA: Rs40\nCOFFE: Rs80\nMEGGIE: 90\nPASTA: Rs70\nSALAAD: Rs50 ")

order_total=0
#40 + 50


item_1 = input("Enter the name of item you want to oder =")
if item_1 in menu :
    order_total +=menu [item_1]#0 +50
    print(f"your item{item_1} has been added to your oder")

else :
    print(f"Ordered item {item_1} is not avilable yet!")

another_order = input("Do you want to add another item? (yes/no)")
if another_order == " yes ":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"ordered item{item_2}is not avaialable!")

print(f"The total amount of item to pay is{order_total}")

 
 
