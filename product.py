from os import remove

import sys 

product_list  = ["Lemon Juice", "Lime Juice", "Apple Juice"]
print("Main Menu Options")
#user_input_main = 1
user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
while user_input_main > 0:    
    if user_input_main == 0:   
        break
     
    print("Product Menu Options")
    print("0: Exit App")
    print("1: Print Products List")
    print("2: Add")
    print("3: Update")
    print("4: Delete")       
    user_input = int(input("Enter option from product menu "))
 #exiting product list-----------------
    if user_input == 0:
        exit()

    #printing product list----------------- 
    elif user_input == 1:
        print(product_list) 

    #adding new product to list
    elif user_input == 2:
        user_input = (input("Enter item you want to add "))
        product_list.append(user_input)

    # updating product list-------------------
    elif user_input == 3:
        print(product_list)         
        user_input_value = int(input("Enter Product Index Value "))
        user_input_name = input("Enter Product Name ")     
        product_list[user_input_value] = user_input_name      
        print (product_list)

    #Deleting element by index-----------------
    elif user_input == 4:
        print(product_list)  
        user_input = int(input("Enter the index value(integer) of the product you want to delete ")) 
        product_list.remove(product_list[user_input])
        print(product_list)
                            
