# Calculating Rent


![responsive](https://github.com/Charly1357/rent/assets/93468053/56a88358-1154-4c27-a400-47cf2cd9757f)


This python project calculates the rent from the value of the houses its
costs and the inflation <br>
It displays its value and the amount of money necesary to rent the house 
as well as the hightest<br> rent paid.<br>
All the values are taken or saved in the google sheets and the highest 
rent is calculated from the<br> sheet.

The project can be viewed :
https://renting-eeafc7b2d4e6.herokuapp.com/

## Table of Contents
1. [User Experience](#user-experience-ux)
    - [Project Goals](#project-goalse)
    - [User Stories](#user-stories)
    - [Data Model](#data-model)
    - [Flowchart](#flowchart)
2. [Features](#features)
    - [Main Menu](#main-menu)
    - [House Data](#house-data)
    - [Rented Houses](#rented-houses)
    - [View Result](#view-result)
    - [Exit Screen](#exit-screen)
3. [Technologies Used](#technologies-used)
    -[Languages](#languages)
    -[Frameworks,Libraries  Programms](#frameworks-libraries-programms)
4. [Testing](#testing)
    -[Testing User Stories](#testing-user-stories)
    -[Code Validation](#code-validation)
    -[Feature Testing](#feature-testing)
5. [Deployment](#deployment)
6. [Credit](#credit)
    -[Content](#content)
    -[Media](#media)
    -[Code](#code)
7. [Acknowledgements](#acknowledgements)
    
## User experience (UX)

### Project Goals
- Collect data from user
- Store data in a Google sheet.
- Show result
- Implement data validation for all inputs.

### User Stories
-As a user,I would like that the program helps me to earn more money
-I would like to choose whether to input data or see the results or exit
-As a user, I would like to see my results filtered according to my needs

### Data Model

The program uses a Google sheet to store the information collected from 
the input.

A pandas data frame is used to filter the highest rent

The user can select between two input once for the value of the house<br>
the other for the house rented<br>



![spreadsheets1](https://github.com/Charly1357/rent/assets/93468053/b892dd6a-0ff4-461c-a937-71c6d350d8a6)


![spreadsheet2](https://github.com/Charly1357/rent/assets/93468053/17382cac-5f5e-412d-a99f-831bf68d6270)



![spreadsheet3](https://github.com/Charly1357/rent/assets/93468053/917e65cf-1a38-4b21-bc82-fa275e0764a9)


### Flowchart

![rentflowchart](https://github.com/Charly1357/rent/assets/93468053/4a4b7981-b883-497d-a9ef-d3fde0ed8eb9)


## Features

![mainmenurent](https://github.com/Charly1357/rent/assets/93468053/a8cf0439-f909-459d-8af7-c8f8c1a907f3)


### Main Menu


- This screen shows the survey main menu that gives the user six<br>
options:
    - Input data houses
    - Input data rented houses
    - Show value houses
    - Show houses rented
    - Show rent house income necesary
    - Show the highest rent
    - Exit
- By adding multiple options the user always has a more complete<br>
experience allowing him to performe various actions in each menu.
  

### Input of Data 

- This part of the program shows all the questions with the options below<br>
and the message "Enter your choice:"
- Option 1  The rent is calculated by taking the value of the house
multiply it with 0.008 add the inflation/100 and the costs/month and you have the
rent and the necesary income is calculated by rent/0.3 this means that only
30% of your income should be used for the rent.
In all the input data option the data is always validated if it is correct
- In the first option Input data houses the user will input the number of
the house:
   - The value of the house
   - The inflation per month
   - The cost per month of the house
   - The year
   - The month

![datahouse](https://github.com/Charly1357/rent/assets/93468053/580e2066-cf48-40e9-bb63-038f74662517)


- In the second option Input data house rented the user will input the number of 
the house:
   - The month rented
   - The year rented

![rentedhouse](https://github.com/Charly1357/rent/assets/93468053/14c7949f-7b0b-4bfd-bfda-82483f48210b)


- The third option shows te value of
the houses:
   - num/house the number of the house
   - v/house the value of the house
   - inflat/month the monthly inflations
   - cost/month
   - year
   - month
![showdatahouse](https://github.com/Charly1357/rent/assets/93468053/4328d065-1ed0-4b9c-bacd-80087c9c3c86)


- The fourth option shows the
houses rented:
    - house number of the house
    - month the month it is rented
    - year the year it is rented

![showrenthouse](https://github.com/Charly1357/rent/assets/93468053/c988c9a3-c16d-4e40-8234-bd0953ae034a)


- The fifth option shows the rent and
the necesary income:
    - house_number
    - rent
    - income
    - year
    - month

![show5](https://github.com/Charly1357/rent/assets/93468053/e33a7644-f5ad-4611-bed2-351a7615ea46)


- The sixth option shows the filter of the
highest rent:
     - house_number
     - rent
     - income
     - year
     - month
![highestrent](https://github.com/Charly1357/rent/assets/93468053/21778241-6bab-4230-973a-5595cc083cd9)


- The seventh option shows
the:
     - Exit
     - When the user choose exit it says
     - ***Thanks and Goodbye *** and leaves the program


## Technology Used

### languages

-Python

- [Diagrams](https://app.diagrams.net): this was used to create a flowchart in
the planning stage of the project.
- [Colorama](https://pypi.org/project/colorama/):this was used to add color to the terminal.
- [Tabulata](https://pypi.org/project/tabulate/):this was used to display data in tables.
- [Pandas](https://pypi.org/project/pandas/):this was used to store and analyse survey data
using data frames.
- [time](https://pypi.org/project/python-time/)This was used to work with time. This was used for waiting during code execution.
- [Gspread](https.//doc.gspread.org/en/v5.12.0/):this is the API for Google sheets,which stores
the survey data
- [Gitpod](https://www.gitpod.io):this was used to write,commit and push the code to GitHub
- [GitHub](https://github.com/):this was used to store the project
- [Heroku](https://id.heroku.com/login):this was used to host and deploy the finished project

## Testing

### Testing User Stories
- As a user ,I would like to understand the program purpose.
  - The program always shows readable instructions and maintains a smooth path through menus
  and questions.
  As a user ,I would like to be able to choose whether to input data ,show the data  or exit
  the program
  - The input data should be filtered by the highest return for the rent
  - As a user ,I would like to see all the information of the google sheets

## Code Validation
- This program was validated using the PEP8 tool provided by Code Institute 
   - 53: E501 line too long (82 > 79 characters)
   - 64: E117 over-indented
   - 65: E225 missing whitespace around operator
   - 70: E901 IndentationError
 
## Feature Testing

TEST      |  DESIRED RESULT  |   PASS/FAIL |<br>
Main Menu | The main menu has 7 options | Input data houses Input<br> 
data rented houses Show value houses Show rent house income necesary Show highest rent Exit Pass

- Input data house 6 questions are
asked:
   -  House number,Value of the house,Monthly inflation<br>
   maintenance cost, Year, Month .
   -  Validataion data
   -  Data transformed in int
   -  Data is updated in the google sheets value
   -  The rent is calculated from the House value monthly inflation
   maintenace cost.
   -  Data is updated in the google sheets cost
   -  clear screen
   -  return to the main menu
   
Everything worked pass

- Input data rented house 3 questions
    - Enter your house number(1,2,3)
    - Enter the month the house was rented
    - Enter the year the house was rented
    - clear_screen
    - validate
    - return to the main menu
      
Everything worked pass

- Show value houses option 3 main menu
   - clear_screen()
   - valuehouse() the data of the value tabel in the googlesheet rent
   it shows table data :
        - number house
        - value house
        - inflation/month
        - cost/month
        - year
        - month
    - time.sleep(5) it shows the data for 5 seconds
    - clear screen
    - first_selection it takes you back to the main menu

Everything worked pass

- Show houses rented option 4 main menu
   - clear-screen()
   - renthouse() the tabel cost in the googlesheet rent is
   shown table data:
        - house number
        - month
        - year
    - time.sleep(5) it shows the data for 5 seconds
    - clear_screen()
    - first_selection it takes you back to the main menu

Everything worked pass

- Show rent house income necesary option 5 main menu
   - clear_screen()
   - rent_income() it shows the data from the tabel cost in the
   googlesheet rent table data:
        - house_number
        - rent
        - income
        - year
        - month
    - time_sleep(5)
    - clear_screen()
    - first_selection() back to the main menu
 
  Everything worked pass

  - Show the highest rent option 6 main menu
     - clear_screen()
     - max_rent() calculates  with pd from pandas
     and idmax() shows highest rent in the table cost<br>
     table data:
         - house_number
         - rent
         - year
         - month
    - time_sleep(10) 10 seconds to see the data
    - clear_screen()
    - first_selection() it return to the main menu

   Everything worked pass

  - Exit stop the program option 7
     - Print *** Thanks and Goodbye ***
     - time.sleep(6)
     - clear_screen()
     - exit()
   
   Everything worked pass

  ## Bugs

  1. Lack of valuation of  data in every input:
     - In both input it only analize the input data once all the data is given
  2. In the Output of the highest rent value it prints information that is not necesary
  Name 1 dytype:object
  3. The input information needed should be better explained
  4. Once you see the data there should be an option if you want to came back to
  the main menu and not a time.sleep

  ## Deployment

  The program was developed in gitpod . It was then committed and pushed to Github.
  The finished project was deployed in Heroku
  The Deployment to Heroku was used in manual mode

  ### Code
  - Love Sandwiches 

  
    
    
      



 

 
  
  














     


















