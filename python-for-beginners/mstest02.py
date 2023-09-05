from datetime import datetime, timedelta

"""
print(datetime.now())

yesterday = datetime.now() -  timedelta(days=1)

print(yesterday)

datestring=input('Please input date:')  
dateobject = datetime.strptime(datestring,'%d/%m/%Y')
oneweek = timedelta(weeks=1)
datenext = dateobject +oneweek
print(dateobject)
print(datenext)

name = 'Willie Mak'
print(name[1:3])

import colorama

colorama.init()
print(colorama.Fore.RED + 'This is red')

from colorama import *

init()
print(Fore.BLUE + 'This is blue')

from colorama import init, Fore
print(Fore.GREEN + 'This is green')
"""
import json

# Create a dictionary object
person_dict1 = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs to dictionary as needed
person_dict2 = {'first': 'Peter', 'last':'Wong'}

# create a staff dictionary
# assign a person to a staff position of program manager
staff_dict ={}
staff_dict['Program Manager']=person_dict1
staff_dict['HR Manager']=person_dict2

# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)