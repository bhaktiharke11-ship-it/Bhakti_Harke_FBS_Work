#3 WAP to accept basic salary of n emp . (n should be accepted from user )  if basic salary is below 20000 then 
## da = 10% , ta = 12% and hra = 15% otherwise da = 15% , ta = 18 % and hra = 20 % . based on this calculate 
# the total salary of each emp and also total salary of all emp .


n = int(input("Enter number of employees: "))

grand_total = 0  

for i in range(1, n + 1):
    basic = float(input(f"\nEnter basic salary of employee {i}: "))

    
    if basic < 20000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total_salary = basic + da + ta + hra
    grand_total += total_salary

    print(f"Total salary of employee {i} = {total_salary:}")

print("Grand Total salary of all employees =", grand_total)
