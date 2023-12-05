import gspread
import pandas as pd
import numpy as np
import os
import time
from tabulate import tabulate


from google.oauth2.service_account import Credentials
from colorama import Fore, Style, Back
"""
Library imports pandas for the data tabulate for the rows and columns of data et
"""
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


"""
Colorama colours for the terminal
"""
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
GREEN = Fore.GREEN
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL


def get_house_data():
        """Get the data from the houses/inflation/costs/year/month"""
        clear_screen()
        print("Please enter the values of the house in whole numbers 1,2,3 etc")
        while True:
            try:
                 house_number = int(input("Please enter your house number example[1,2,3,4,5 etc]:\n "))
            except ValueError:
              print("Sorry, int value")
              continue
            else:
               break

        while True:
            try:
                 value_house = int(input("Enter the value of your house: 200000 ,300000:\n"))
            except ValueError:
                print("Sorry, int value")
                continue
            else:
               break

        while True:
            try:
                monthly_inflation = int(input("Enter the monthly_inflation:in integer numbers (1,2,3)\n"))
            except ValueError:
                print("Sorry,int value")
                continue
            else:
                break

        while True:
            try:    
                cost = int(input("Enter the cost you had to invest in the house monthly cost:(200,300)\n"))
            except ValueError:
                print("Sorry, int value")
                continue
            else:
                break

        while True: 
            try:
                year = int(input("Enter the year:\n"))
            except ValueError:
                print("Sorry, int value")
                continue
            else:
                break

        while True:
            try:
                month = int(input("Enter the month:(1,2,3,4..12\n"))
            except ValueError:
                print("Sorry,value int value")
                continue
            else:
                break

        data_str = house_number, value_house, monthly_inflation, cost, year, month
        #print(data_str)
        clear_screen()

            #if validate_data(data_str):
               #break
    
        return data_str



        """ Validate the input data """


        
    

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
         Calculate rent get the input data of the value_house and multiply it with 0.8 plus the inflation cost
         and the cost to maintain the house.Calculate the necesary income for the rent only 30% of the income should be used 
         for the rent
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

""" Input data about the rented houses """

def houses_rented():
         clear_screen()
         #while True:
         print("Please enter  the data  of the rented house ")
         while True:
             try:
                house_number = int(input("Enter your house number:(1,2,3,4,5 ej\n"))
             except ValueError:
                print("Sorry int value")
                continue
             else:
                break
         while True:
             try:
                month_rented = int(input("Enter the month the house was rented( 1,2,3 ..\n"))
             except ValueError:
                print("Sorry int value")
                continue
             else:
                break
         while True:
             try:  
               year_rented = int(input("Enter the year the house was rented:\n"))
             except ValueError:
                print("Sorry int value")
                continue
             else:
                break
         sales_data = house_number,month_rented,year_rented
         clear_screen()
           #if validatedata(sales_data):
             #break
    
         return sales_data

""" validation of the rented houses """

def validatedata(values):
        try:
            [int(value)for value in values]
            if len(values) !=3:
                raise ValueError(
                    f"Exactly 3 values are required,you provided{len(values)}"
                )

        except ValueError as e:
            print(f"Invalid data: {e},please try again\n")
            return False

        return True      

""" Sheet with the data of the house number value of the house inflation/month cost/month year month """

def valuehouse():
    stock = SHEET.worksheet("value").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))

""" Calculation of the highest rent from the worksheet rent """

def maxrent():
    rentmax = SHEET.worksheet('cost').get_all_values()
    df = pd.DataFrame(rentmax[1:],columns = rentmax[0])
    max_index = df['rent'].idxmax()
    selected_row = df.iloc[max_index]
    print(selected_row)

""" All the data from the rented houses is printed """

def renthouse():
    stock = SHEET.worksheet("rent_house").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))

""" All the data from the house is printed """

def rent_income():
    stock = SHEET.worksheet("cost").get_all_values()
    print(tabulate(stock,headers='firstrow',tablefmt='grid'))

""" The screen is cleared otherwise the screen would have to much information """

def clear_screen():
    if os.name == "posix":
        _=os.system("clear")
    else:
        _os.system("cls")

def welcome():
    clear_screen()
    first_selection()

def goodbye():
    print("\n *** Thanks and Goodbye ***\n")
    time.sleep(6)
    clear_screen()
    exit()
    
""" The main area of the programm where the user selects his area of interest """

def first_selection():
    """
      The user chooses between the different options
    """
    selection = 0
    clear_screen()
    while selection !=1 and selection !=2 and selection !=3 and selection !=4 and selection !=5 and selection !=6 and selection !=7:
        try:
            # print(BLUE + BRIGHT + "\n*** PROGRAMM FOR RENTING HOUSES ***\n" + RESET)
            print(BLUE + BRIGHT + "........*** Main Menu ***........\n" + RESET)
            print(WHITE + BRIGHT + "Select an option:\n")
            print(GREEN + BRIGHT + "1 - Input data houses" + RESET)
            print(GREEN + BRIGHT +"2 - Input data rented houses" + RESET)
            print(GREEN + BRIGHT +"3 - Show value houses" + RESET)
            print(GREEN + BRIGHT +"4 - Show houses rented" + RESET)
            print(GREEN + BRIGHT +"5 - Show rent house income necesary" + RESET)
            print(GREEN + BRIGHT +"6 - Show the highest rent " + RESET)
            print(RED + BRIGHT + "7 - Exit\n" + RESET)
            selection = int(input(YELLOW + BRIGHT + "Enter your choice:" + RESET))
            if selection !=1 and selection !=2 and selection !=3 and selection !=4 and selection !=5 and selection !=6 and selection !=7:
                clear_screen()
                print(GREEN + BRIGHT + "\n ****Invalid input,please enter a valid number 1.2.3...7****\n "+ RESET)
        except ValueError:
            clear_screen()
            print("Invalid input")
        if selection == 1:
            data = get_house_data()
            #print(data)
            #sales_data = [int(num) for num in data]
            sales_data = data
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
            clear_screen()
            valuehouse()
            time.sleep(5)
            clear_screen()
            first_selection()
        elif selection == 4:
            clear_screen()
            renthouse()
            time.sleep(5)
            clear_screen()
            first_selection()
        elif selection == 5:
            clear_screen()
            rent_income() 
            time.sleep(5)
            clear_screen()
            first_selection()
        elif selection == 6:
            clear_screen()
            maxrent()
            time.sleep(10)
            clear_screen()
            first_selection()
        elif selection == 7:
            goodbye()
welcome()



