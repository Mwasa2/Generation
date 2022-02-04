user_input = 1
while user_input > 0 :
    print("Main Menu")
    print("1: Products")
    print("2: Couriers")
    print("3: Orders")
    user_input = int(input("Enter an option  or 0 to exit "))
    
    if user_input == 0:
        break
    if user_input == 1:
        
        import product

    if user_input == 2:
        import courier

    if user_input == 3:
        import order

