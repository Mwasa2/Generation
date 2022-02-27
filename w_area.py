import csv


'''with open("order_list.csv") as file:
    
    print("Orders Main Menu Options")

    user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
    while user_input_main > 0:    
        if user_input_main == 0:   
            break
    #-----------------------------------Product list menu  
        print("////////////////////")
        print("Order Menu Options")
        print("////////////////////")
        print("0: Exit App")
        print("1: Print Orders List")
        print("2: Add")
        print("3: Update")
        print("4: Delete")       
        user_input = int(input("Enter the courier option "))
    #------------------------------------------------- All options below
        if user_input == 0:
            exit ()
        
        elif user_input == 1:  #--------------Print orders dictionary
            with open("order_list.csv","r")as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    print(row)
                    
        
        elif user_input == 2: #--------------Create new courier
            with open("order_list.csv","a+")as file:
                
                user_input_name=input("Enter New Customer Name ")
                user_input_address=input("Enter New Customer Address ")
                user_input_phone=input("Enter New Customer Phone Number ")
                             #----------------print couriers list with index
            
        with open("order_list.csv","r")as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                print(row)
                  
        with open("order_list.csv","a") as file:
            fieldnames =['customer_name','customer_address','customer_phone','courier','order_status'] 
            writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter=',')            
            writer.writeheader()
            
            
            dictToPass = ({
            'customer_name':user_input_name,
            'customer_address':user_input_address,
            'customer_phone':user_input_phone})
           # writer.writerow(dictToPass)


            #if fieldnames == False:
                #1writer.writeheader()
            #elif fieldnames == True:
            #next(row)    
            with open("orders_courier.csv","r")as file:
                reader = csv.DictReader(file, delimiter=',')
                user_input_find = int(input("Enter index to select courier "))
            with open("orders_courier.csv","r")as file:
                for row in reader:
                    if row == user_input:
                        print(row)'''
                        
  #Orders List- Need to transfer it over to order_list                      
fifth_col = [] 
with open ("order_list.csv","r")as file:
    user_input_order_value = int(input("Enter Order Value "))
    for index, order_list in enumerate(file):
        if user_input_order_value == index:
            print(index,order_list)
            
            fifth_col.append(order_list)

    with open ("order_status_list.csv","r") as file:
        user_input_status = int(input("Enter Status Value ")) 
        for  index,status_row in enumerate(file):
            if user_input_status == index:
            # user_input_status 
                print(index,status_row)
                print(fifth_col)
            with open ("order_list.csv","a")as file:
                

                
                                                                   
                    
                        
                        
                        
