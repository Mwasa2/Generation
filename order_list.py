import csv
from pprint import pp
with open("order_list.csv") as file:
    
    
    print("Orders Main Menu Options")

    user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
    while user_input_main > 0:    
        if user_input_main == 0:   
            break
    #-----------------------------------Order list menu  
        print("////////////////////")
        print("Order Menu Options")
        print("////////////////////")
        print("0: Exit App")
        print("1: Print Orders List")
        print("2: Add")
        print("3: Update")
        print("4: Delete")       
        user_input = int(input("Enter the order option "))
    #------------------------------------------------- All options below
        if user_input == 0:
            exit ()
        
        elif user_input == 1:  #--------------Print orders dictionary
            with open("order_list.csv","r")as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    print(row)
                    
        
        elif user_input == 2: #--------------Create new order                
            user_input_name=input("Enter New Customer Name ")
            user_input_address=input("Enter New Customer Address ")
            user_input_phone=input("Enter New Customer Phone Number ")
            
        
            with open("orders_courier.csv","r")as file:
                reader = csv.DictReader(file, delimiter=',')
                
                for index, row in enumerate(reader):
                    print(index, row)
                        
            user_input_courier_id = int(input("Enter index to select courier "))
            
            creating_dict = {
                            'customer_name':user_input_name,
                            'customer_address':user_input_address,
                            'customer_phone':user_input_phone,
                            'order_status': 'Preparing',
                            'courier':user_input_courier_id
                            }
            
            with open("order_list.csv","a") as file:
                fieldnames =['customer_name','customer_address','customer_phone','courier','order_status'] 
                writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter =',')
                writer.writerow(creating_dict)
                
                
        elif user_input == 3: #--------------Print Order Status with INdex update
            status_list = []
            
            with open("order_list.csv","r")as file:
                orders = list(csv.DictReader(file, delimiter=','))
                for index,row in enumerate(orders):
                   pp([index,row])
                user_id_order = int(input("Enter ID Of Order You Want To Change "))
   
                '''for index,order in enumerate(reader):
                   #for index, order in enumerate(file):
                    if index == user_id_order:'''
            with open("order_status_list.csv","r")as contents:
                statuses = list(csv.DictReader(contents, delimiter=','))
                for index,row in enumerate(statuses):
                    pp([index,row])
                
            user_input_status_id = int(input("Enter ID to Change Status In Order "))                    
            orders[user_id_order]['order_status'] = statuses[user_input_status_id]['status']   
                
            with open("order_list.csv","w",newline='') as file:
                fieldnames =['customer_name','customer_address','customer_phone','courier','order_status'] 
                writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter =',')
                writer.writeheader()
                writer.writerows(orders)
                
                
                
                
                
                
                
                
                
                
                
                