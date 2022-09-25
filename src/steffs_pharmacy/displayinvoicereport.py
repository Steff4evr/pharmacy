import openpyxl
import pandas as pd
import clearing
from rich import print
from rich.console import Console
from rich.table import Table

# Function to display the Salesreport to terminal


def display_invoice_report():
    console = Console()
    # clear screen
    clearing.clear()
    # Read the invoices  report
    sales_report = pd.read_excel("src/steffs_pharmacy/data/invoices.xlsx")
    table_stock = Table(show_header=False, header_style="bold blue")
    table_stock.add_row(
        "-----------------------------------SALES REPORT-----------------------------------")
    console.print(table_stock)
    # print the report to terminal
    print(f"{sales_report.to_string()}\n")
    print("-"*36, "END-OF-REPORT", "-"*36)
    # Hit enter key to return
    enter_key = input("Press 'Enter' to continue.")
