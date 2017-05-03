"""
How many days from yyyy mm dd until the next mm dd
Authors: yuanw
Credits:  None
  of this code, credit them here.  You don't have to credit the course
  instructor,  GTFs, or tutors / helpers in office hours. 

CIS 210 assignment 3, Winter 2014
Usage example: python days_till.py  2012 09 24 06 14
    (first day of fall classes until end of spring finals)
"""

import sys  # For exit with a message
import argparse # Fancier command line parsing

def leap_year(year):
    """
    Checking for the leap year when the input is.
    Args:
    """
    if year % 4 == 0:
        leap_year_2 = 29
        if year % 100  == 0:
            leap_year_2 = 29
            if year % 400 == 0:
                leap_year_2 = 29
    else:
        leap_year_2 = 28
        
   

    return leap_year_2 
 


def month_day(year,start_month):
    """
    Find out each month days between leap year and not leap year.
    Args:
    """
    day_month = [0,31, leap_year(year) ,31,30,31,30,31,31,30,31,30,31]
    months_days = day_month[start_month]
    return months_days
    

def is_valid(year, month, day):
    """
    Checking for the valid date before we counts days. if stard on a non-
    existent date. return an error message "...".
    Args:
    """
    valid = False
    if year >= 1800 and year <= 2500:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= month_day(year, month):               
                valid = True
    return valid


def days_between(year, start_month, start_day, end_month, end_day):
    """
    we input four integers, if the valid date in the range, the program
    will print out how many days between two dates.
    Args:
    """
    print("Days_between：")
    month = start_month + 1
    emonth = end_month + 1
    secondyear = year + 1
    months = 0
    if month > emonth:
        while month > end_month and month <= 12:
            months += (month_day(year,month))
            if month == 12:
                month = 0
                while month < end_month:
                    months += (month_day(secondyear,month))
                    month +=1
                break
            month += 1
        Remind_start_day = month_day(year,start_month) - start_day
        total_day = months + Remind_start_day + end_day
        return total_day
    if month < emonth:       
        while month < end_month:
            months += (month_day(year,month))
            month += 1
        Remind_start_day = month_day(year,start_month) - start_day
        total_day = months + Remind_start_day + end_day
        return total_day

    elif month == emonth:
        if start_day <= end_day:
            total_day = end_day - start_day
            return total_day
        elif start_day > end_day:
            while month <= 12:
                months += (month_day(year,month))
                if month == 12:
                    month = 0
                    while month < end_month:
                        months += (month_day(secondyear,month))
                        month +=1
                    break
                month += 1 
        Remind_start_day = month_day(year,start_month) - start_day
        total_day = months + Remind_start_day + end_day
        return total_day
      
   
def main():
    
   
    ## The standard way to get arguments from the command line, 
    ##    make sure they are the right type, and print help messages
    parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
    parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
    parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
    parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
    parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
    parser.add_argument('end_day', type=int, help="Ending day, integer 1..12")
    args = parser.parse_args()  # will get arguments from command line and validate them
    year = args.year
    start_month = args.start_month
    start_day = args.start_day
    end_month = args.end_month
    end_day = args.end_day
    
    #FIXME: The first print commands below are just for debugging, and will need
    #  be be removed or commented out. Calls to is_valid can be uncommented when
    #  you have written a function to check validity. 
    print("Checking date ", str(year) + "/" + str(start_month) + "/" + str(start_day))
    if not is_valid(year, start_month, start_day) :
        sys.exit("Must start on a valid date between 1800 and 2500")
    if not is_valid(2000, end_month, end_day):
        sys.exit("Ending month and day must be part of a valid date")
    #print("Days in starting month:", days_in_month(start_month, year))
    print(days_between(year, start_month, start_day, end_month, end_day))   


if __name__ == "__main__":
    main()
        
