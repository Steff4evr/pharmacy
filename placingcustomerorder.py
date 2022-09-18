
import re
import openpyxl
import time


def placing_customer_order():
    search_results = []
    found = False
    # Enter the med id
    while True:
        print("\n")
        print("****************************************************************")
        print("********************Placing Customer Order**********************")
        print("****************************************************************")
        try:
            med_id_user_input = int(
                input("Enter the med id to add to cart.. To discontinue, enter 0 "))
        except ValueError:
            print("Invalid med id !")
            time.sleep(2)
        if med_id_user_input == 0:
            return None
        #Open inventory
        medicine_inventory = openpyxl.load_workbook("MEDICINE_INVENTORY.xlsx")
        mi = medicine_inventory.active
        # Search Inventory for the Medicine
        for i in range(2, mi.max_row+1):            
            for j in range(1, 2):                
                med_id = mi.cell(row=i, column=j)                
                if (med_id_user_input == int(med_id.value)):
                    found = True
                    search_results.append(med_id.value)
                    print(f" Medicine Id : {search_results}", end="\n")
        if found is False:
            print("Medicine Not Found")

        # Enter the qty needed
        # Check if the med id the qty is available
        # if yes then add to  invoice
        # if qty not available then do not add to invoice
        # loop this process until order is completed
