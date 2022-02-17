with open("courier_list.txt") as file:
    
    print("Courier Main Menu Options")

    user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
    while user_input_main > 0:    
        if user_input_main == 0:   
            break
    #-----------------------------------Product list menu  
        print("////////////////////")
        print("Courier Menu Options")
        print("////////////////////")
        print("0: Exit App")
        print("1: Print Courier's List")
        print("2: Add")
        print("3: Update")
        print("4: Delete")       
        user_input = int(input("Enter the courier option "))
    #------------------------------------------------- All options below
        if user_input == 0:
            exit ()
        
        elif user_input == 1:  #--------------Print menu
            with open("courier_list.txt","r")as file:
                contents = file.readlines()
                print("\n",contents)
        
        elif user_input == 2: #--------------Create new courier
            with open("courier_list.txt","a")as file:
                user_input=input("Enter New Product Name ")
                #for line in file:
                file.write(user_input)
                file.write('\n')
               
        elif user_input == 3: #--------------Update courier
            with open("courier_list.txt","r+") as file:
                 content = file.readline()
            for index in enumerate(content):
                   print(index)
                             
                    