import csv
with open("product_list.txt") as file:
    
    print("Products Main Menu Options")
    print("**************************")

    user_input_main = int(input("Enter: 0 to Exit or 1 to continue ")) 
    while user_input_main > 0:    
        if user_input_main == 0:   
            #break
            import main_menu
    #-----------------------------------Product list menu  
        print("////////////////////")
        print("Product Menu Options")
        print("/////////////////////")
        print("0: Exit App")
        print("1: Print Products List")
        print("2: Add")
        print("3: Update")
        print("4: Delete") 
        print("5: New Product")      
        user_input = int(input("Enter the product option "))
    #------------------------------------------------- All options below
        if user_input == 0:
            import main_menu
        
        elif user_input == 1:  #--------------Print menu
            with open("product_list.csv","r")as file:
                reader = csv.DictReader(file, delimiter = ',')
                for index,rows in enumerate(reader):
                    print(index, rows)
                    
        elif user_input == 2: #--------------Create new product
            #with open("product_list.csv","r+")as file:
                user_input_name = input("Enter New Product Name ")
                user_input_price = input("Enter New Product Price £")
                product_dict = {
                            'product_name':user_input_name,         
                            'product_price':user_input_price
                            }
                with open("product_list.csv","a") as file:
                    fieldnames =['product_name','product_price'] 
                    writer = csv.DictWriter(file,fieldnames=fieldnames, delimiter=',')
                    writer.writerow(product_dict)
            

                    
        elif user_input == 3: #-------------------Update
            with open("product_list.txt","r+")as file:
                contents = file.read()
                print(contents)
                
                user_input_name = str(input("Enter name of product "))
                user_input_value = int(input("Enter the product value "))
                
                for index,line in enumerate(file):   
                    if line == user_input_value[line]:
                        updated_product = (contents[line]) = user_input_name
#-------------------------------------------------------writing to screen/file                        
                        file.write(updated_product)
                        print(index, user_input_name, user_input_value)


        elif user_input == 4:# Delete 
            with open("product_list.csv","r", newline='') as delete_product:
                delete_product_row = delete_product.read()  #read the file
               # delete_product_content = delete_product 
                print(delete_product_row)
                user_input_ID = int(input("Enter Product ID "))          
                    
                for row in delete_product_row:

                    delete_product.append(row)

                    for field in row:

                        if field == user_input_ID:

                            delete_product.remove(row)

            with open("product_list.csv","w") as delete_product_row:

                writer = csv.writer(delete_product_row)

                writer.writerows(delete_product)
#----------------------------------------------------------------------------                        
'''lines = list()

    members= input("Please enter a member's name to be deleted.")

    with open('mycsv.csv', 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)       #csv file delete_product

            for field in row:

                if field == members:

                    lines.remove(row)

    with open('mycsv.csv', 'w') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)'''

