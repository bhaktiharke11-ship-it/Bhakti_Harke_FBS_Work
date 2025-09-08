# WAP to print sum of series upto n.

n = int(input("Enter the number :"))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
    print (sum) 



## using for loop 
i = 1
sum = 0
for i in range (1,n+1):
    sum = sum + i
    i += 1
    print(sum)