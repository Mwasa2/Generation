import csv
#with open("courier_list.csv","r") as file:
    
print("Courier Main Menu Options")

user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
while user_input_main > 0:    
    if user_input_main == 0:   
        import main_menu
        
         
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
        import main_menu
        
                   
    elif user_input == 1:  #--------------Print List
        with open("courier_list.csv","r")as file:
            reader = csv.DictReader(file, delimiter = ',')
            for index,rows in enumerate(reader):
                print(index, rows)        
    
    elif user_input == 2: #--------------Create new Courier
            user_input_name = input("Enter New Courier Name ")
            user_input_courier_phone = input("Enter New Courier Phone Number ")
            
            courier_dict = {'courier_name':user_input_name,         
                            'courier_phone_number':user_input_courier_phone
                            }
            with open("courier_list.csv","a") as file:
                
                fieldnames =['courier_name','courier_phone_number'] 
                writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter = ',')
                writer.writerow(courier_dict)       
    
    
    
    
   # elif user_input == 3: #--------------Update courier
   #  with open("courier_list.csv","r+") as file:
                
                
                    