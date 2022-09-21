from rich import print
from rich.console import Console
from rich.table import Table

import time
from searchdrugs import search_drugs
from customerorder import customer_order


def main():
    console = Console()
    cart = []
    while True:
        print("*****************************")
        table = Table(show_header=False, header_style="bold blue",
                      title="MENU", title_justify="center")
        table.add_row("1. Search for Medicine")
        table.add_row("2. Customer Order")
        table.add_row("3. Stock In Hand Report")
        table.add_row("4. Sales Report")
        table.add_row("5. Exit")
        console.print(table)
        print("*****************************")

        try:
            choice = int(input("Choose your Option :"))
        except ValueError:
            print("Invalid Option !")
            time.sleep(2)
            continue
        if choice == 1:
            search_drugs()
        elif choice == 2:
            cart = customer_order(cart)
        elif choice == 3:
            # Function for stock in hand report
            pass
        elif choice == 4:
            # Function for Sales Report
            pass
        elif choice == 5:
            exit()
        else:
            # invalid choice
            print(f'Choice {choice} is invalid')
            continue


main()
