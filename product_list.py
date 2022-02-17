with open("product_list.txt") as file:
    
    print("Products Main Menu Options")
    print("**************************")

    user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
    while user_input_main > 0:    
        if user_input_main == 0:   
            break
    #-----------------------------------Product list menu  
        print("////////////////////")
        print("Product Menu Options")
        print("/////////////////////")
        print("0: Exit App")
        print("1: Print Products List")
        print("2: Add")
        print("3: Update")
        print("4: Delete")       
        user_input = int(input("Enter the product option "))
    #------------------------------------------------- All options below
        if user_input == 0:
            exit ()
        
        elif user_input == 1:  #--------------Print menu
            with open("product_list.txt","r")as file:
                contents = file.readlines()
                print("\n",contents)
        
        elif user_input == 2: #--------------Create new product
            with open("product_list.txt","a")as file:
                user_input=input("Enter New Product Name ")
                #for line in file:
                file.write(user_input)
                file.write('\n')
                    
        elif user_input == 3: #-------------------Update
            with open("product_list.txt","r+")as file:
                contents = file.read()
                print(contents)
                
                user_input_name = str(input("Enter name of product "))
                user_input_value = int(input("Enter the product value "))
                
                for line in file:   
                    if line == user_input_value[line]:
                        updated_product = (contents[line]) = user_input_name
#-------------------------------------------------------writing to screen/file                        
                        file.write(updated_product)
                        print(user_input_name, user_input_value)

