## 10. Write a program to reverse three-digit number.

num = int(input("Enter a number :"))

hunderds =  num // 100
tens = (num // 10 ) % 10
ones = num % 10 
 

reverse_number = ones * 100 + tens * 10 + hunderds

print("revers three digits number: ", reverse_number )



