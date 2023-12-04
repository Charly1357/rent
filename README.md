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
![Show house data]()

- The fourth option shows the
houses rented:
    - house number of the house
    - month the month it is rented
    - year the year it is rented
![Show house rented]()

- The fifth option shows the rent and
the necesary income:
    - house_number
    - rent
    - income
    - year
    - month
![Show rent and income house]()

- The sixth option shows the filter of the
highest rent:
     - house_number
     - rent
     - income
     - year
     - month
![Show highest rent]()

- The seventh option shows
the:
     - Exit
     - When the user choose exit it says
     - ***Thanks and Goodbye *** and leaves the program
![Exit]()

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

 

 
  
  














     


















