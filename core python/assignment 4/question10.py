## WAP to check if given number is perfect number 


n = int(input("Enter number :"))

i = 1
divisor = 0

while i < n:
    if n % i == 0: # if i is divisor
        divisor += i
    i += 1

if divisor == n:
    print(n, "is a perfecct number")

else:
    print(n," is not perfect number")

