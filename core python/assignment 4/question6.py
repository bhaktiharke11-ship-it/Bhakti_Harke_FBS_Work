# WAP to check if a given number is prime number or not.
n = int(input("Enter number:"))

i = 2

while i < n and n % i != 0:
    i += 1

if i == n:
    print(n, "is a prime number ")
else:
    print(n, "is not prime number")