import os # is our module for manipulating acces files get info about operatng system
import ast


# def loud_balance():
    # try: 
    #     with open("balance.txt", "r") as file: #open file in a reading mode 
    #         balance = float(file.read()) # read the conted adn save in balance variable.
    #     return balance
    # except:
    #     print("File not found\nReturning default balance.")
    #     return 1000



def load_balance():
    if os.path.isfile("balance.txt"):
        with open("balance.txt", "r") as file: #open file in a reading mode 
            balance = float(file.read()) # read the conted adn save in balance variable.
        return balance
    else:
        print("File not found\nReturning default balance.")
        return 1000


def save_balacnce(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))  #str = converting in to strings
        print("Balance Saved !")
    



def load_inventory():
    inventory = {}
    if os.path.isfile("inventory.txt"):
        with open("inventory.txt", "r") as file:
            inventory = ast.literal_eval(file.read())
            return inventory
    else:
        print("File not found\nReturning default inventory.")
        return {
"Laptops": {"price £": 800, "quantity in stock": 10},
"Phones": {"price £": 500, "quantity in stock": 15},
"Monitors": {"price £": 300, "quantity in stock": 10,},
}

def save_inventory(inventory):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory))
        print("Inventory saved !")


        
def load_history():
    if os.path.isfile("history.txt"):
        with open("history.txt", "r" ) as file:
            history = ast.literal_eval(file.read())
            return history
    else:
        print("File not found\nReturning default history.")
        return []

def save_history(history):
    with open("history.txt", "w") as file:
        file.write(str(history))
        print("History saved !")



#literal_eval : 
     #https://www.geeksforgeeks.org/create-an-empty-file-using-python/   
    #https://www.educative.io/answers/what-is-astliteralevalnodeorstring-in-python