import gspread
import pandas as pd
import numpy as np
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
        print("Please enter the house_number,value_house,monthly-inflation,cost per house,year,month")
        print("1,200000,12,1500,2023,11")
        data_str = input("Enter your data here:\n")
        
        sales_data = list(data_str.split(","))

        if validate_data(sales_data):
            break
    
    return sales_data

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

def first_selection():
    """
      The user chooses between the different options
    """
    selection = 0
    while selection !=1 and selection !=2:
        try:
            print(BLUE + BRIGHT + "Main Menu" + RESET)
            print(WHITE + BRIGHT + "Select an option:\n")
            print("1 - Input data houses")
            print("2 - Input data rented houses")
            print("3 - Show value houses")
            print("4 - Show houses rented")
            selection = int(input(YELLOW + BRIGHT + "Enter your choice:" + RESET))
            if selection !=1 and selection !=2:
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
        elif selection == 2:
            survey_result()
        elif selection == 3:
            goodbye()

first_selection()


