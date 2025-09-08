## Find the sum of three-digit number.

num = int(input("Enter a number:"))

hunderds =  num // 100
tens = (num // 10 ) % 10
ones = num % 10 
 
digit_sum = hunderds +  tens + ones 

print("total three digits_sum", digit_sum)