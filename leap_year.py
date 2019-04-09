print ("This program can calculate if a year is a leap year or not")
while True:
    year = input("enter the year: ") # ask the year
    # the calculation of a leap year (next # )
    #  https://m.wikihow.com/Calculate-Leap-Years
    year = int(year)
    yes_list = ["yes", "y", "yeah"]

    #it should be divisible by 4 
    # it shouldn't be divisible by 100 but if it is we must divide it by 400
    # if it is divisible by 400 and 100 when its a leap year
    
    if year%4==0 : # there shouldn't be any division remaning
        year = str(year) 
        print (year + " is definetly a leap year")
        
    elif year%100==0:
        if year%400==0:
                year = str(year)
                print (year + " is definetly a leap year")

    
    ask = input("do you want to calculate another year? ") # asking if the user want to repeat
    if ask in yes_list:
        pass
    else:
        break