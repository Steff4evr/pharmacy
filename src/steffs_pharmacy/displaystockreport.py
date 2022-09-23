import openpyxl
import pandas as pd
import clearing
from rich import print
from rich.console import Console
from rich.table import Table

def display_stock_report():
    console = Console()
    clearing.clear()    
    stock_report = pd.read_excel("./data/medicine_inventory.xlsx")
    table_stock = Table(show_header=False, header_style="bold blue")
    table_stock.add_row(
        "---------------------------------------STOCK REPORT---------------------------------------")
    console.print(table_stock)
    print(f"{stock_report}\n")
    print("-"*39, "END-OF-REPORT", "-"*39)
    enter_key = input("Press 'Enter' to continue.")
