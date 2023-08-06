import re
import pandas as pd

state_tax = {
    "Alabama" : 3.5,
    "Arizona" : 2.5, 
    "Arkansas" : 3.5,
    "California" : 7.5,
    "Colorado" : 4.4,
    "Connecticut" : 5,
    "Delaware" : 3.3,
    "Georgia" : 3,
    "Hawaii" : 6,
    "Idaho" : 3.5,
    "Illinois" : 4.95,
    "Indiana" : 3.23,
    "Iowa" : 4,
    "Kansas" : 4,
    "Kentucky" : 5,
    "Louisiana" : 3,
    "Maine" : 6,
    "Maryland" : 4,
    "Massachusetts" : 5,
    "Michigan" : 4.25,
    "Minnesota" : 7,
    "Mississippi" : 2.5,
    "Missouri" : 4.4,
    "Montana" : 3.5,
    "Nebraska" :  5,
    "New Hampshire" : 5,
    "New Jersey" : 5.5,
    "New Mexico" : 3,
    "New York" : 7,
    "North Carolina" : 4.99,
    "North Dakota" : 2,
    "Ohio" : 2,
    "Oklahoma" : 2.5,
    "Oregon" : 7,
    "Pennsylvania" : 3.07,
    "Rhode Island" : 5,
    "South Carolina" : 3.2,
    "Utah" : 4.65,
    "Vermont" : 5.5,
    "Virginia" :  4,
    "West Virginia" : 5,
    "Wisconsin" : 6

}

user_state = input("Hello! Please tell me your state you reside in: ")
user_state = user_state.capitalize()
user_income = input("Thank you! Now can you tell me how much money you make annually: ")
user_income = re.sub(r'[^\w\s]','',user_income)
monthly_income = 0
def calculator(user_income):
    monthly_income = (int(user_income) -  ( (state_tax[user_state] / 100) * float(user_income) ) )/ 12
    monthly_income = round(monthly_income, 2)
    return monthly_income

if user_state not in state_tax:
    print("Please enter a valid state: ")
    calculator(user_income)
    print("Your state does not have income tax! Your monthly income is $" + str((int(user_income) / 12)))
else:
    calculator(user_income)
    print("Your monthly income is $" + str(monthly_income))