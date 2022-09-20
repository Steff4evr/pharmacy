import time
import os
from searchdrugs_excel import search_drugs
from placingcustomerorder import placing_customer_order
from billing import billing_invoice_generation
from inventoryupdate import inventory_update
from invoiceupdate import invoice_update

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
        print("4. Clear cart")
        print("5. Exit to main menu")
        # capture user input
        try:
            user_option = int(input("Choose an option .. "))
        # Catch  any invalid input
        except ValueError:
            print("Invalid Option !")
            time.sleep(1)
        if user_option == 1:
            search_drugs()
            time.sleep(1)
        elif user_option == 2:
            cart = placing_customer_order(cart)
            time.sleep(1)
        elif user_option == 3:
            print(f"Cart Items : {cart}")
            invoice_number=billing_invoice_generation(cart)
            if invoice_number is not None:
                inventory_update(cart)
                invoice_update(cart,invoice_number)
            time.sleep(1)
        elif user_option == 4:
            cart.clear()
            print("Cart Emptied !")
            time.sleep(1)
        elif user_option == 5:
            exit()

customer_order()
