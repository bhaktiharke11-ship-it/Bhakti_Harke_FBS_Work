## Program to Find the Roots of a Quadratic Equation


a = int(input("Enter value A : "))
b = int(input("Enter value B : "))
c = int(input("Enter value C : "))

d = b * b - 4 * a * c

x1 = (-b + d**0.5 ) / 2 * a
x2 = (-b - d**0.5 ) / 2 * a

print(f'Quadratic roots x1 :{x1} ,Quadratic roots x2 :{x2} ')