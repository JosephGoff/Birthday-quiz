"""
birthday.py
Author: Joseph Goff
Credit: Morgan Gardner
Assignment: Birthday Problem

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name?")
birthmonth = input("Hi " + name + ", what was the name of the month you were born in?")
birthyear = int(input("And what year were you born in, " + name + "?"))
birthday = int(input("And the day?"))

months = ["" "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ""]
month = months[todaymonth]


if birthmonth=="October" and birthday==31:
    print("You were born on Halloween!")
elif birthmonth==month and birthday==todaydate:
    print("Happy birthday!")
    
elif birthmonth in ["March", "April", "May"] and birthyear>=2010 and birthyear<= 2018:
    print(str(name + ", you are a spring baby of the two thousand tens."))
elif birthmonth in ["June", "July", "August"] and birthyear>=2010 and birthyear<= 2018:
    print(str(name +", you are a summer baby of the two thousand tens."))
elif birthmonth in ["September", "October", "November"]  and birthyear>=2010 and birthyear<= 2018:
    print(str(name + ", you are a fall baby of the two thousand tens."))
elif birthmonth in ["December", "January", "February"] and birthyear>=2010 and birthyear<= 2018:
    print(str(name + ", you are a winter baby of the two thousand tens."))
    
elif birthmonth in ["March", "April", "May"] and birthyear>=2000: 
    print(str(name + ", you are a spring baby of the two thousands."))
elif birthmonth in ["June", "July", "August"] and birthyear>=2000:
    print(str(name +", you are a summer baby of the two thousands."))
elif birthmonth in ["September", "October", "November"]  and birthyear>=2000:
    print(str(name + ", you are a fall baby of the two thousands."))
elif birthmonth in ["December", "January", "February"] and birthyear>=2000:
    print(str(name + ", you are a winter baby of the two thousands."))
    
elif birthmonth in ["March", "April", "May"] and birthyear>=1990 and birthyear<= 2000:
    print(str(name + ", you are a spring baby of the nineties."))
elif birthmonth in ["June", "July", "August"] and birthyear>=1990 and birthyear<=2000:
    print(str(name + ", you are a summer baby of the nineties."))
elif birthmonth in ["September", "October", "November"]  and birthyear>=1990 and birthyear<=2000:
    print(str(name + ", you are a fall baby of the nineties."))
elif birthmonth in ["December", "January", "February"] and birthyear>=1990 and birthyear<= 2000:
    print(str(name + ", you are a winter baby of the nineties."))
    
elif birthmonth in ["March", "April", "May"] and birthyear>=1980 and birthyear<= 1990:
    print(str(name + ", you are a spring baby of the eighties."))
elif birthmonth in ["June", "July", "August"] and birthyear>=1980 and birthyear<=1990:
    print(str(name + ", you are a summer baby of the eighties."))    
elif birthmonth in ["September", "October", "November"]  and birthyear>=1980 and birthyear<=1990:
    print(str(name + ", you are a fall baby of the eighties."))
elif birthmonth in ["December", "January", "February"] and birthyear>=1980 and birthyear<= 1990:
    print(str(name + ", you are a winter baby of the eighties."))
    
elif birthmonth in ["March", "April", "May"] and birthyear<=1980: 
    print(str(name + ", you are a spring baby of the Stone Age."))
elif birthmonth in ["June", "July", "August"] and birthyear<=1980:
    print(str(name +", you are a summer baby of the Stone Age."))
elif birthmonth in ["September", "October", "November"] and birthyear<=1980:
    print(str(name + ", you are a fall baby of the Stone Age."))
elif birthmonth in ["December", "January", "February"]  and birthyear<=1980:
    print(str(name + ", you are a winter baby of the Stone Age."))
    
    
    
    
    
    
    