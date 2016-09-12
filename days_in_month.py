#!/usr/bin/env python3
'''days_in_month.py
This simple script finds the location of a selected month in one list and
days in that month at the corresponding location in another. Both items are
printed to the screen afterward.
Limitations:
This code will not work if the month is not in list of months.
Usage: ./days_in_month.py
Toni Luoto - 12.9.2016
'''

# Set the selected month
SelectedMonth = 'August'

# List of months
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',  'October', 'November', 'December']

# List of days in corresponding month
Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Find location of selected month
Index = Months.index(SelectedMonth)

# Print Month and days it has on screen
print('The number of days in', SelectedMonth, 'is', Days[Index])  
