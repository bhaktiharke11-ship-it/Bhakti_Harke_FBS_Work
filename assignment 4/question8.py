## WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start = int(input("Enter start of number : "))
end = int(input("Enter end of number : "))

i = start
print("Numbers that are divisible by 7 and multiple of 5 in the given range:")

while i <= end:
    if i % 7 == 0 and i % 5 == 0:   # condition check
        print(i, end="  ")
    i += 1   # ✅ go to the next number


## using for loop 

# for i in range (start , end+1 ):
#     if (i % 7 == 0 and  i % 5 == 0):
#         print(i)