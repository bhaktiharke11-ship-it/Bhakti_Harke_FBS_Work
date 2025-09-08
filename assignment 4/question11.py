# WAP to check if  given number  strong number

n = int(input("Enter number:"))

temp = n
sum_of_fact = 0

while temp > 0 :
    digit = temp % 10 # extract last digit
    fact = 1
    i = 1
while i<= digit :
    fact *= i
    i += 1
sum_of_fact += fact 
temp //= 10

if sum_of_fact == n :
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")
