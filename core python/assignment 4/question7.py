## WAP to print all integers upto n that aren’t divisible by 2 and 3.


n = int(input("Enter the value of n:"))

i =1 
print("number not divsible by 2 and 3 up to" , n ,"is:")

while i <= n:
    if i %2 != 0 and i % 3 != 0:
        print(i , end=' ')
    i += 1


## using for loop

# for i in range (n): 
#     if( i % 2 != 0 and i % 3 != 0):
#         print(i , end =" ")