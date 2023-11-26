import gspread
from google.oauth2.service_account import Credentials

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

data = sales.get_all_values()

print(data)

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