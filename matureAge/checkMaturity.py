from date import Date

def Before_date():

    BeforeD = Date(1,1,2003)

    date = Date_before_date()
    while date is not None :
        if date <= BeforeD:
            print("You are not mature enough to think about voting")
        else:
            print("Voting is either your right and your duty")
        date = Date_before_date()

def Date_before_date():
    print("Enter Your birth Date: ")
    mouth =int(input("Your B. mouth: "))
    day = int(input("Your B. Day:     "))
    year = int(input("Your B. Year:  "))

    if mouth == None or day == None or year == None :
        return None
    else:
        return Date(mouth,day,year)
Before_date()


    
