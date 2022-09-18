import time
import os
from searchdrugs_excel import search_drugs
from placingcustomerorder import placing_customer_order


def customer_order():
    cart = []
    while True:
        # Menu for getting customer order
        print("****************************************************************")
        print("***********************CUSTOMER ORDER***************************")
        print("****************************************************************")            
        print("1. Search for medicine and add to customer order")
        print("2. Placing the customer order")
        print("3. Verify medicines in cart and confirm order")
        print("4. Exit to main menu")        
        # capture user input
        try:
            user_option = int(input("Choose an option .. "))
        # Catch  any invalid input
        except ValueError:
            print("Invalid Option !")
            time.sleep(2)
        if user_option == 1:
            search_drugs()
        elif user_option == 2:
            cart = placing_customer_order(cart)
        elif user_option == 3:
            print(f"Cart Items : {cart}")
        elif user_option == 4:
            exit()

customer_order()
