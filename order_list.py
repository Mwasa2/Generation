import csv
import os 
from dataclasses import field
with open("order_list.csv") as file:
    
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
            
        with open("courier_list.txt","r") as file:
                content = file.readlines()
                for index in enumerate(content):
                    print(index)  
                    
        with open("order_list.csv","a") as file:
        
                
            fieldnames =['customer_name','customer_address','customer_phone','courier','order_status'] 
            writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter=',')    
            writer.writeheader()
                
            dictToPass = ({
            'customer_name':user_input_name,
            'customer_address':user_input_address,
            'customer_phone':user_input_phone})

            if fieldnames == False:
                writer.writeheader()
            elif fieldnames == True:
                writer.writerow(dictToPass)
                


             
            #----------------------------------------------------------------------                
'''' with open("courier_list.txt","r") as file:
                content = file.readlines()
                for index in enumerate(content):
                    print(index)'''
                
                        #------------------------below find the courier through the value
                
                        
                        
                        
       