##Write a program to enter P, T, R and calculate Compound Interest.\

Principal = int(input("Enter principal:"))
rate = float(input("Enter rate:"))
Time = float(input("Enter Time:"))

compound_interst = Principal * (1 + rate / 100) ** Time - Principal
print("compound_interst:",compound_interst)

