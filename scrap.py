from os import remove

import sys       #This is working need to put in working file for product

#product_list  = ["Lemon Juice", "Lime Juice", "Apple Juice"]
with open("product.txt") as f:
    
    print("Main Menu Options")

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
            with open("product.txt","r")as f:
                print(f.readlines())
            #print(product_list) 

        #adding new product to list
        elif user_input == 2:
                user_input = (input("Enter item you want to add "))
        with open("product.txt","a")as f:        
            #for input in user_input:
            f.write(str(user_input))
            f.write("\n")
            print(f)
                    
                    
            #product_list.append(user_input)
