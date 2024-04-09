from functions import load_balance, save_balacnce, load_inventory, save_inventory, load_history, save_history

products = load_inventory()

# Company's account balance
account_balance = load_balance()
Stock_count = {"quantity in stock"}
# Recorded sales and purchases
sales = []
purchases = []

history = load_history() 


               


while True:
    #display commands 
    print("\n\nWelcome\nChose one of the following options\n")
    print("(1)balance")
    print("(2)sale")
    print("(3)purchase")
    print("(4)account")
    print("(5)list")
    print("(6)warehouse")
    print("(7)review")
    print("(8)end\n")
   #prompt for command
   
   
    user_input = input("Enter command :  ")
    if user_input == 'balance':
        print(f"Your curent balance is :{account_balance}")
        prtint_action = (input("Do you want to add or substract?: "))
        amount_of_money = float(input("Enter amount : "))
        if prtint_action == 'add':
                account_balance = amount_of_money + account_balance
                history.append(f"Added amount of money.{amount_of_money}\nYour new Total balace :{account_balance}")
                print(f"Your new Total balace is={account_balance}")
                
        elif prtint_action == 'substract':
                account_balance = account_balance - amount_of_money
                print(f"Your new Total balace :{account_balance}")
                history.append(f"Substruct amount of money.{amount_of_money}\nYour new Total balace :{account_balance}")
        elif account_balance <= 0:
                print("Balance not enough add more!")
                break
        

    elif user_input == "sale":
        print(f"Your balance is {account_balance}")
        for item, details in products.items():
                print(f"\n{item.capitalize()}: ")
                for detail, value in details.items():
                        print(f"- {detail.capitalize()}: {value}")
        product_selected = input("\nEnter product name : ").capitalize()
        quantity_bought = int(input("Enter quantity : "))
        items_bought = quantity_bought * products[product_selected]["price £"]      
        if account_balance >= items_bought and account_balance >= items_bought:
                account_balance += items_bought
                products[product_selected]["quantity in stock"] -= quantity_bought
                print(f"\nYour order has ben placed\nTotal amount : {items_bought}£")
                print(f"Quantity left for {product_selected}: {products[product_selected]['quantity in stock']}")
                print(f"Your account balance: {account_balance}£")
                history.append(f"Total amount spend: {items_bought} Price: {products[product_selected]["price £"]} Quantity bought: {products[product_selected]['quantity in stock']}")
        elif items_bought > account_balance:
               print("Not enough money!") 
        elif items_bought < products[product_selected]["price £"]:
                print("Not enough items in stock")
        elif quantity_bought > details["quantity in stock"]:
                print("We don't have enough stock") 



    elif user_input == "purchase":
        print(f"Your balance is {account_balance}")
        for item, details in products.items():
                print(f"\n{item.capitalize()}: ")
                for detail, value in details.items():
                        print(f"- {detail.capitalize()}: {value}")
        product_selected = input("\nEnter product name : ").capitalize()
        quantity_bought = int(input("Enter quantity : "))
        item_price = int(input("Enter pricve per unit: "))
        if account_balance > item_price * quantity_bought:
               account_balance -= item_price * quantity_bought
               products[product_selected] = {"price £": item_price, "quantity in stock": quantity_bought}
               history.append(f"Name of product : {product_selected}, Total amount bought: {quantity_bought} Price: {item_price * quantity_bought}")
        else:
               print("Not enough money in the acount.")
                                     
    
    elif user_input == "account":
           print(f"Your account balance is: {account_balance} ")
    
    elif user_input == "list":
           for item, details in products.items():
                print(f"\n{item.capitalize()}: ")
                for detail, value in details.items():
                        print(f"- {detail.capitalize()}: {value}")

    elif user_input == "warehouse":
        item_name = input("Provode name of product : ").capitalize()
        if item_name in products.keys():  #keys = returns lists of keys from dictionary 
            for item in products.keys():
                   if item_name == item:
                          print(item_name)
                          print(f"Price: {products[item_name]['price £']}")
                          print(f"Quantity in stock: {products[item_name]['quantity in stock']}")
        else:
               print("Iteam not in inventory.")
        

           
        
    elif user_input == "review":
           for event in history:
                  print(event)
        


    elif user_input == "end":
        print("Exiting program")
        break
    else:
           print("Invailid command.Please try again")
         

save_balacnce(account_balance)
save_inventory(products)
save_history(history)
    
 
         