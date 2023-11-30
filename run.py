import gspread
import pandas as pd
import numpy as np
import os
from tabulate import tabulate

from google.oauth2.service_account import Credentials
from colorama import Fore,Style,Back

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("rent")

sales = SHEET.worksheet('value')

#data = sales.get_all_values()

#print(data)
"""
Colorama colours for the terminal
"""
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

def get_house_data():
    """Get the data from the houses/inflation/costs/year/month"""
    while True:
        print("Please enter the values of the house in whole numbers")
        house_number = input("Enter your house number:\n")
        value_house = input("Enter the value of your house:\n")
        monthly_inflation = input("Enter the monthly_inflation:\n")
        cost = input("Enter the cost you had to invest in the house:\n")
        year = input("Enter the year:\n")
        month = input("Enter the month:\n")
        data_str = house_number,value_house,monthly_inflation,cost,year,month
        

        if validate_data(data_str):
            break
    
    return data_str

def validate_data(values):
        try:
            [int(value)for value in values]
            if len(values) !=6:
                raise ValueError(
                    f"Exactly 6 values are required,you provided{len(values)}"
                )

        except ValueError as e:
            print(f"Invalid data: {e},please try again\n")
            return False

        return True


def update_worksheet(new_row,worksheet):
          """
          Update the specified worksheet,
          adding a new row with the list data provided.
          """ 
          print(f"Updating{worksheet}worksheet..\n")
          worksheet_to_update = SHEET.worksheet(worksheet)

          #adds new row to the end of the current data
          worksheet_to_update.append_row(new_row)

          print(f"{worksheet}worksheet updated successfully\n")

def calculate_rent(data):
         """ 
         Get the input data of the value_house and multiply it with 0.8 plus the inflation and the cost cost
         """
         house_number = data[0]
         house_value = data[1]
         monthly_inflation = data[2]
         cost_house = data[3]
         year = data[4]
         month = data[5]
         inflation = (monthly_inflation/100)
         rent_simple = house_value * 0.008
         rent = rent_simple + cost_house + (rent_simple * inflation)
         income = rent/0.3
         rent_data = house_number,rent,income,year,month
         rent_int = [int(value)for value in rent_data]
         return (rent_int)


def houses_rented():
    while True:
         print("Please enter  the data  of the rented house ")
         house_number = input("Enter your house number:\n")
         month_rented = input("Enter the month the house was rented\n")
         year_rented = input("Enter the year the house was rented:\n")
         sales_data = house_number,month_rented,year_rented
         if validatedata(sales_data):
            break
    
    return sales_data


def validatedata(values):
        try:
            [int(value)for value in values]
            if len(values) !=3:
                raise ValueError(
                    f"Exactly 6 values are required,you provided{len(values)}"
                )

        except ValueError as e:
            print(f"Invalid data: {e},please try again\n")
            return False

        return True      

def main():
            """
            Run all program functions.
            """
            #data = get_house_data()
            #sales_data = [int(num) for num in data]
            #update_worksheet(sales_data,"value")
            #rent = calculate_rent(sales_data)
            #update_worksheet(rent,"cost")
            #housrented = houses_rented()
            #update_worksheet(housrented,"rent_house")


#stock_data = main()
def valuehouse():
    stock = SHEET.worksheet("value").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))
 
def maxrent():
    rentmax = SHEET.worksheet('cost').get_all_values()
    df = pd.DataFrame(rentmax[1:],columns = rentmax[0])
    max_value = df['rent'].max()
    print(f"The maximum rent is {max_value}.")

def renthouse():
    stock = SHEET.worksheet("rent_house").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))

def rent_income():
    stock = SHEET.worksheet("cost").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))

def clear_screen():
    if os.name == "posix":
        _=os.system("clear")
    else:
        _os.system("cls")

def welcome():
    clear_screen()
    first_selection()

def goodbye():
    print("Good bye")
    clear_screen()
    exit()


def first_selection():
    """
      The user chooses between the different options
    """
    selection = 0
    clear_screen()
    while selection !=1 and selection !=2:
        try:
            print(BLUE + BRIGHT + "Main Menu" + RESET)
            print(WHITE + BRIGHT + "Select an option:\n")
            print("1 - Input data houses")
            print("2 - Input data rented houses")
            print("3 - Show value houses")
            print("4 - Show houses rented")
            print("5 - Show rent house income necesary")
            print("6 - Show the highest rent ")
            print("7 - Exit")
            selection = int(input(YELLOW + BRIGHT + "Enter your choice:" + RESET))
            if selection !=1 and selection !=2 and selection !=3 and selection !=4 and selection !=5 and selection !=6:
                #clear_screen()
                print(RED + "Invalid input,please enter a valid number"+ RESET)
        except ValueError:
            print("Invalid input")
        if selection == 1:
            data = get_house_data()
            sales_data = [int(num) for num in data]
            update_worksheet(sales_data,"value")
            rent = calculate_rent(sales_data)
            update_worksheet(rent,"cost")
            clear_screen()
            first_selection()
        elif selection == 2:
            houserented = houses_rented()
            update_worksheet(houserented,"rent_house")
            clear_screen()
            first_selection()
        elif selection == 3:
            valuehouse()
        elif selection == 4:
            renthouse()
        elif selection == 5:
            rent_income()  
        elif selection == 6:
            maxrent()
        elif selection == 7:
            goodbye()
welcome()



