import openpyxl
import pandas as pd
import clearing
from rich import print
from rich.console import Console
from rich.table import Table

# Function to display the stock report to terminal


def display_stock_report():
    console = Console()
    # clear screen
    clearing.clear()
    # read the inventory data from  the xls file
    stock_report = pd.read_excel(
        "src/steffs_pharmacy/data/medicine_inventory.xlsx")
    table_stock = Table(show_header=False, header_style="bold blue")
    table_stock.add_row(
        "---------------------------------------STOCK REPORT---------------------------------------")
    # display the heading
    console.print(table_stock)
    # display the stock report
    print(f"{stock_report}\n")
    print("-"*39, "END-OF-REPORT", "-"*39)
    # press
    enter_key = input("Press 'Enter' to continue.")
