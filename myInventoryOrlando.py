'''
Assignment No.: 3
Course: PROG12974
Name: Orlando Companioni
Submission date: 2022/12/02
Instructor's name: Syed Tanbeer

#This program is an Inventory Management System with fruits, vegetables and dairy products
#I used a dictionary instead of a bunch of if statements to let the user choose the option
'''
import sys #This module provides access to some variables used or maintained by the interpreter.

#list of fruits, vegetables and dairy products that willbe updated in the inventory
#The dictionary is global so that i dont have to put it as a parameter in every function
inventory={"F01":["Orange","Fruit",2.99,1000],"F02":["Apple","Fruit",1.99,5000],\
        "F03":["Banana","Fruit",1.5,490],"D01":["Milk","Dairy",7.5,500],\
        "D02":["Cheese","Dairy",15,840],"D03":["Yogurt","Dairy",5.5,700],\
        "V01":["Carrot","Vegetable",3.8,890],"V02":["Celery","Vegetable",3.99,990],\
        "V03":["Bean","Vegetable",4.5,1500],"V04":["Potato","Vegetable",6,1000]}

def main(): #This function will control the program's flow
    process()

def menu(): #This function will display the menu options
    print()
    print("-------Inventory Database Operations--------")
    print(f"1. Show all items")
    print(f"2. Look up at the inventory")
    print(f"3. Add an item to the inventory")
    print(f"4. Change an item")
    print(f"5. Delete an item")
    print(f"6. Find items given category")
    print(f"7. Item count, average price by category")
    print(f"8. Most expensive item by category")
    print(f"9. Total price by item")
    print(f"10. Quit the program")
    print()

def menu_selection(): #This function will ask the user to select an option from the menu
    menu()
    #User input validation
    while True:
        try:
            option=int(input("Enter your option: "))
            if option not in range(1,11):
                print("ERROR: Enter a valid option") #if its a number but not in the range of 1 to 10
                continue
            break
        except ValueError:
            print("ERROR: Enter a numeric value") #if its not a number the program will ask the user to enter a number
            continue
    return option

def category_validation(category): #This function will validate the category
    if category=="Fruit" or category=="Dairy" or category=="Vegetable":
        return True
    else:
        return False

def idValidation(itemId): #This function will validate the item Id entered by the user
    if itemId in inventory.keys():
        return True
    else:
        return False

def idCategory_Validation(itemId,type): #This function will validate if the item id and category are correct together
    if itemId.startswith("F") and type=="Fruit" or itemId.startswith("D") and type=="Dairy" or itemId.startswith("V") and type=="Vegetable":
        return True
    else:
        return False

def item_chart(itemId): #This function will display the inventory chart for specific item or items
    print()
    print(f"{'Product Id':<18}{'Product Name':<18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
    print(f"{itemId:<18}{inventory[itemId][0]:<18}{inventory[itemId][1]:<18}{inventory[itemId][2]:<18}{inventory[itemId][3]:<18}")
    print()

def price_quantityValidation(): #This function will validate the price and quantity until the user enters a valid input
    while True: #User input validation
        try:
            price=float(input("Enter the product price: "))
            break
        except ValueError:
            print("ERROR: Enter a numeric value")
            continue
    while True:
        try:
            quanity=int(input("Enter the product quantity: "))
            break
        except ValueError:
            print("ERROR: Enter a numeric value")
            continue
    return price,quanity

def process(): #This function will process the user's choice
    option=menu_selection() #The menu_selection function will return the user's choice as well as the menu
    while True:
        options={1:inventory_chart,2:item_LookUp,3:add_item,4:change_item,5:delete_item,6:find_items,7:item_count,8:most_expensive,9:total_price,10:quit}
        options[option]() #This will call the function that corresponds to the option chosen by the user
        option=menu_selection()

def quit(): #This function will quit the program
    print("Thank you for using the Inventory Management System")
    sys.exit()
    
def inventory_chart(): #This function will display the inventory chart
    #Print a table with all the inventory 
    print()
    print(f"{'Product Id':<18}{'Product Name':18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
    for key in inventory:
        print(f"{key:<18}{inventory[key][0]:<18}{inventory[key][1]:<18}{inventory[key][2]:<18}{inventory[key][3]:<18}")
    
def item_LookUp(): #This function will look up an item in the inventory
    while True: #User input validation
        itemId=input("Enter the product Id: ").capitalize() #capitalizes the first letter of the item id
        if idValidation(itemId): #compares if the item id is in the inventory
            item_chart(itemId)
            break
        else:
            print("Item Id not found")
            continue 
        #Repeats the loop as long as the users input is not valid
        
def add_item(): #This function will add an item to the inventory
    while True: #User input validation
        itemId=input("Enter the product Id: ").capitalize()
        if idValidation(itemId): #compares if the item id is in the inventory
            print("ERROR Product Id already exists")
            continue
        #Compares if the item id and the category are valid
        elif itemId[0] not in ["F","D","V"]:
            print("ERROR:Product Id must start with F, D or V")
            continue
        else:
            item_name=input("Enter the product name: ").capitalize() 
            while True:
                type=input("Enter the product type: ").capitalize()
                if idCategory_Validation(itemId,type): #compares if the item id and the category are valid
                    price,quanity=price_quantityValidation()
                    break
                else:
                    print("ERROR:Invalid category type")
                    print("Category type must be Fruit, Dairy or Vegetable depending on the product Id")
                    print()
                    continue
            inventory.update({itemId:[item_name,type,price,quanity]})
            item_chart(itemId)
            print("New item added to the inventory!")
            break

def change_item(): #This function will change an item in the inventory
    while True:
        itemId=input("Enter the product Id: ").capitalize()
        if idValidation(itemId): #compares if the item id is in the inventory
            item_name=input("Enter the product name: ").capitalize()
            while True:
                type=input("Enter the product type: ").capitalize()
                if not idCategory_Validation(itemId,type): #compares if the item id and the category are valid
                    print("ERROR Invalid item category")
                    continue
                else:
                    price,quanity=price_quantityValidation()
                    inventory.update({itemId:[item_name,type,price,quanity]})
                    item_chart(itemId)
                    print("Item Updated!")
                    break
            break
        else:
            print("Item Id not found or incorrect")
        continue
    
def delete_item(): #This function will delete an item from the inventory
    itemId=input("Enter the product Id: ").capitalize()
    if idValidation(itemId): #compares if the item id is in the inventory
        item_chart(itemId)
        del inventory[itemId]
        print("Item deleted!")
    else: print(f"Item Id {itemId} not found or incorrect")

def find_items(): #This function will find items given a category
    while True:
        type=input("Enter the category: ").capitalize()
        if category_validation(type):
            for key in inventory.keys():
                if inventory[key][1]==type:
                    print()
                    print(f"{'Product Id':<18}{'Product Name':<18}{'Product Type':<18}{'Price':<18}{'Quantity':<18}")
                    print(f"{key:<18}{inventory[key][0]:<18}{inventory[key][1]:<18}{inventory[key][2]:<18}{inventory[key][3]:<18}")
            break        
        else:
            print()
            print("Invalid category....")
            print("Valid categories are: Fruit, Vegetable, Dairy")
            continue #Repeats the loop as long as the users input is not valid
            
def item_count():
    #This function will count the number of items in the inventory
    #and the average price of the items in the inventory
    key_list=list(inventory.keys()) # list of keys in the dictionary
    fruit_count=0
    vegetable_count=0
    dairy_count=0
    fruit_price=0
    vegetable_price=0
    dairy_price=0
    for key in key_list:
        if inventory[key][1]=="Fruit":
            fruit_count+=1
            fruit_price+=inventory[key][2]
        elif inventory[key][1]=="Vegetable":
            vegetable_count+=1
            vegetable_price+=inventory[key][2]
        elif inventory[key][1]=="Dairy":
            dairy_count+=1
            dairy_price+=inventory[key][2]
    print(f"Total number of fruits: {fruit_count}")
    print(f"Average price of fruits: {fruit_price/fruit_count}\n")
    print(f"Total number of vegetables: {vegetable_count}")
    print(f"Average price of vegetables: {vegetable_price/vegetable_count}\n")
    print(f"Total number of dairy products: {dairy_count}")
    print(f"Average price of dairy products: {dairy_price/dairy_count}")

def most_expensive(): #This function will find the most expensive item in the inventory
    key_list=list(inventory.keys()) # list of keys in the dictionary
    #variables that will hold a value of the most expensive items in each category
    max_fruit=0 
    max_dairy=0
    max_vegetable=0
    expensive_fruit=""
    expensive_dairy=""
    expensive_vegetable=""
    for key in key_list: #This loop will find the most expensive item in each category
        if inventory[key][1]=="Fruit" and max_fruit<inventory[key][2]:
            max_fruit=inventory[key][2]
            expensive_fruit=inventory[key][0]
        elif inventory[key][1]=="Dairy" and max_dairy<inventory[key][2]:
            max_dairy=inventory[key][2]
            expensive_dairy=inventory[key][0]
        elif inventory[key][1]=="Vegetable" and max_vegetable<inventory[key][2]:
            max_vegetable=inventory[key][2]
            expensive_vegetable=inventory[key][0]
               
    print(f"-------Most Expensive Item By Category-------")
    print(f"{'Product Name':<18}{'Product Type':<18}{'Price':<18}")
    print(f"{expensive_fruit:<18}{'Fruit':<18}{max_fruit:<18}")
    print(f"{expensive_dairy:<18}{'Dairy':<18}{max_dairy:<18}")
    print(f"{expensive_vegetable:<18}{'Vegetable':<18}{max_vegetable:<18}")

def total_price(): #This function will find the total price of the inventory
    key_list=list(inventory.keys()) # list of keys in the dictionary
    print(f"-----------Total Price-----------")
    print(f"{'Product Id':<18}{'Product Name':<18}{'Total Price':<18}")  #prints the header
    for key in key_list:
        print(f"{key:<18}{inventory[key][0]:<18}{inventory[key][2]*inventory[key][3]:<18}") #Prints the product id, name and total price

try:
    if __name__ == "__main__": #This will run the main function
        main()
except KeyboardInterrupt:
    print("Program terminated by user") #This will catch a keyboard interrupt and print a message
