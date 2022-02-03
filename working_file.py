#printing product list----------------- 

#user_input = input("Enter 1  ")
#if user_input == 1:
   # with open("product.txt","r")as file:
with open('product.txt') as file:
        lines = file.readlines()
# Remove whitespace characters like '\n' at the end of each line
        lines = [x.strip() for x in file]
        print(lines)      
    