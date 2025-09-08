# WAP to print all even numbers until n.

n = int(input("enter the all even number until n :"))

print("Even number up to", n, "are:")

i = 2
while(i <= n):
    print(i, end=' ')
    i += 2

## using for loop 


# for i in range ( 2 , n, 2):
#     print(i ,end=" ")