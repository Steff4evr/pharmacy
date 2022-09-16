from rich import print
from rich import console
from searchdrugs import searchdrugs
import time


def main():
    while True:
        print("****************************************************************")
        print("***************************MENU*********************************")
        print("****************************************************************")
        print("1. Search for Medicine")
        print("2. Customer Order")        
        print("3. Stock In Hand Report")
        print("4. Sales Report")
        print("5. Purchase Report")
        print("6. New Stock Order")
        print("7. Exit")

        try:
            choice = int(input("Choose your Option :"))            
        except ValueError:
            print("Invalid Option !")
            time.sleep(2)
            continue
        if choice == 1:
            searchdrugs()             
        elif choice == 2:
            #Function for customer order
            pass
        elif choice == 3:
            #Function for stock in hand report
            pass
        elif choice == 4:
            #Function for Sales Report
            pass
        elif choice == 5:
            #Function for purchase report
            pass 
        elif choice == 6:
            #Function for New Stock Order
            pass
        elif choice == 7:
            exit()
        else:
            #invalid choice
            print(f'Choice {choice} is invalid')
            continue


main()