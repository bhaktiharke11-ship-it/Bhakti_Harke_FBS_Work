##Write a program to enter P, T, R and calculate simple Interest.

principal = int(input("Enter principal:"))
Time = int(input("Enter Time:"))
rate = int(input("Enter rate:"))
simple_int = principal * Time * rate /100
print("simple_int:",simple_int)