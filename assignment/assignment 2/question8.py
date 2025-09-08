##Write a program to swap two numbers using third variable.


a = int(input("Enter a number A :"))
b = int(input("Enter a number B :"))

temp = a
a = b 
b = temp 


print(f'a:{a} , b:{b} , temp:{temp}')