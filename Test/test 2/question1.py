## WAP to accept year from user and check if it is leap year or not 

year = int(input("Enter year :"))

if(year % 4 == 0):

    if(year % 100 == 0):

        if(year % 400 == 0):
            print("leap Year ")
        else:
            print(" not leap Year")
        
    else:
        print("leap year")
else:
    print("not a leap year ")
