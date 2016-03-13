#find a person whose birthday is just after 1**6.1.26 which is a leap year and a Monday
from datetime import *
def isleap(year):
    try:
        date(year,2,29)
        return True
    except ValueError: return False

for i in range(1006,2000,10) :
    if isleap(i) and date(i,1,26).weekday()==0 :
        print i