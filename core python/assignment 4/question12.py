## WAP to print Armstrong number within a given range


start = int(input("Enter a start of range:"))
end = int(input("Enter the end of range:"))

print(f'Armstrong number between {start} and {end} are:')

num = start

while num <= end:
    temp = num
    sum_of_powers = 0
    # count number of digit
    n_digit = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n_digit
    temp //= 10

if sum_of_powers == num:
    print(num, end=' ')

num += 1