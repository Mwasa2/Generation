user_input = 1
while user_input > 0 :
    print("Main Menu")
    print("*********")
    print("1: Products")
    print("2: Couriers")
    print("3: Orders")
    user_input = int(input("Enter an option  or 0 to exit "))
    
    if user_input == 0:
        exit()
    if user_input == 1:
        import product_list

    if user_input == 2:
        import courier_list

    if user_input == 3:
        import order_list

