## WAP to accept 3 digit number . if first digit is double of second digit and half of thord digit then display 
# "yes, you have done it ", ottherwise display :"please try next time"


num = int(input("Enter three digit number :"))

d1 =  num // 100
d2 = (num // 10 ) % 10
d3 = num % 10 
 

if(d1 == 2 * d2 and d1 * 2 == d3):
    print("yes, you have done it")
else:
    print("please try next time")


