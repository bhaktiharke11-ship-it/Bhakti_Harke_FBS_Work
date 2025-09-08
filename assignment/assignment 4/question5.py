## WAP to print Fibonacci series upto n 

# The Fibonacci series is a special sequence of number
# (F0) =-1
# (F1) = 1
# (F2 = F1 + F0) , (F3 = F2 + F1) , (F4 = F3 + F2).....


n = int(input("Enter number of n terms:"))

F0 = -1 
F1 = 1
i = 0

print("Fibonacci series:")

while i< n:
    print(F0 ,end=" ")

    F3 =F0 + F1 
    F0 = F1
    F1 = F3 
    i += 1


## using for loop


# a = -1
# b = 1
# i = 0
# for i in range (n):
#     c = a + b
#     print(c ,end ="  ")
#     a = b 
#     b = c 