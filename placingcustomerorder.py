
import re
import openpyxl
import time


def placing_customer_order():
    search_results = []
    found_med_flag = False
    qty_available_flag = False
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
        try:
            med_qty_user_input = int(
                input("Enter the quantity to add to cart.. To discontinue, enter 0 "))
        except ValueError:
            print("Invalid Quantity !")
            time.sleep(2)            
        if med_qty_user_input == 0:
            return None
        #Open inventory
        medicine_inventory = openpyxl.load_workbook("MEDICINE_INVENTORY.xlsx")
        mi = medicine_inventory.active
        # Search Inventory for the Medicine
        for i in range(2, mi.max_row+1):                            
            med_id = mi.cell(row=i, column=1)
            med_name = mi.cell(row=i, column=2)
            med_qty = mi.cell(row=i, column=4)               
            if (med_id_user_input == int(med_id.value)):
                found_med_flag = True
                available_med_qty = med_qty.value
                if (med_qty_user_input <= int(med_qty.value)):
                    qty_available_flag = True             
                    search_results.append({med_id.value,med_name.value,med_qty.value})
                    print(f" Medicine Id : {search_results}", end="\n")
        if found_med_flag is False:
            print("Medicine Not Found")
        if qty_available_flag is False:
            print(f"There is not enough quantity available for this medicine in the inventory. Only {available_med_qty} available")
        # Enter the qty needed
        # Check if the med id the qty is available
        # if yes then add to  invoice
        # if qty not available then do not add to invoice
        # loop this process until order is completed
