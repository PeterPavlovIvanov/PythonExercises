import datetime


# Constants
DIFFERENCE = "Difference: "
WELCOME_MESSAGE = "Enter two dates separated by a comma,to get the difference between them. " \
                  "\n Format YEAR MONTH DAY: "  # Example 2022-12-23,2023-01-18


# User Input
dates = input(WELCOME_MESSAGE)
dates_tuple = tuple(dates.split(','))

first_date_tuple = tuple(dates_tuple[0].split('-'))
second_date_tuple = tuple(dates_tuple[1].split('-'))

f_date = datetime.datetime(int(first_date_tuple[0]), int(first_date_tuple[1]), int(first_date_tuple[2]))
s_date = datetime.datetime(int(second_date_tuple[0]), int(second_date_tuple[1]), int(second_date_tuple[2]))
r_date = f_date - s_date

print(f'{DIFFERENCE} {r_date}')
