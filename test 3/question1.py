## WAP to print first n prime number 

n = int(input("Enter n number:"))

i = 2

while i < n and n % i != 0:
    i += 1


if i == n :
    print(n, "is prime number")
else:
    print(n, "is not prime number")