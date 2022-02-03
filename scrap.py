from os import remove
import sys 

with open("product.txt","r")as file:
        product_list = file.readlines()
    #    print(product_list)
        print("Main Menu Options")
user_input_main = input("Enter: 0 to Exit or 1 to continue ")
if user_input_main == 0:
    with open("product.txt","w")as file:
        (product_list)##############
elif user_input_main == 1:
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
