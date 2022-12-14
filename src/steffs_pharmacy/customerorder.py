import time
import clearing
from rich import print
from rich.console import Console
from rich.table import Table
from searchdrugs import search_drugs
from placingcustomerorder import placing_customer_order
from billing import billing_invoice_generation
from inventoryupdate import inventory_update
from invoiceupdate import invoice_update

# Function for customer order


def customer_order(cart):
    console = Console()
    while True:
        clearing.clear()
        # Menu for getting customer order
        print("*"*50)
        table = Table(show_header=False, header_style="bold blue",
                      title="CUSTOMER ORDER", title_justify="center")
        table.add_row("1. Search for medicine for customer")
        table.add_row("2. Add to cart")
        table.add_row("3. Billing and Invoice")
        table.add_row("4. Clear cart")
        table.add_row("5. Exit to main menu")
        console.print(table)
        print("*"*50)
        # capture user input
        try:
            user_option = int(input("Choose an option .. "))
        # Catch  any invalid input
        except ValueError:
            print("Invalid Option !")
            time.sleep(2)
            continue
        # user options
        if user_option == 1:
            # Call function to  search for medicine
            search_drugs()
            time.sleep(1)
        elif user_option == 2:
            # Call function for placing customer order
            cart = placing_customer_order(cart)
            time.sleep(1)
        elif user_option == 3:
            if cart:
                # Invoice generation
                invoice_number = billing_invoice_generation(cart)
                if invoice_number is not None:
                    # call function to update inventory
                    inventory_update(cart)
                    # call function to update invoice
                    invoice_update(cart, invoice_number)
                    # clear the cart after the order is complete
                    cart.clear()
            else:
                # ALert that the cart is empty
                print("Cart is empty !")
            time.sleep(1)
        elif user_option == 4:
            # Empty the cart
            cart.clear()
            print("Cart Emptied !")
            time.sleep(1)
        elif user_option == 5:
            # return to  the main menu
            return cart
        else:
            # Invalid user option
            print(f'Choice {user_option} is invalid')
            time.sleep(2)
            continue
