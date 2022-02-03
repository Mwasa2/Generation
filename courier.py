#couriers_list  = ["Jake", "Malachy", "Travis"]
with open("courier.txt","r")as file:
    for i in file:
        print(i)
user_input = int(input("Enter option from courier menu "))

#exiting product list-----------------
if user_input == 0:
    exit()
with open("courier.txt","r")as file: 

#printing product list-----------------
elif user_input == 1:
        print(file) 

#adding new product to list
elif user_input == 2:
    user_input = (input("Enter item you want to add "))
    couriers_list.append(user_input)

# updating product list-------------------
elif user_input == 3:
    print(couriers_list)         
    user_input_value = int(input("Enter Product Index Value "))
    user_input_name = input("Enter Couriers Name ")     
    couriers_list[user_input_value] = user_input_name   
    print(couriers_list,couriers_list[couriers_list])          
    print (couriers_list)

#Deleting element by index-----------------
elif user_input == 4:
    print(couriers_list)  
    user_input = int(input("Enter the index value(integer) of the courier you want to delete ")) 
    couriers_list.remove(couriers_list[user_input])
print(couriers_list)
                        
