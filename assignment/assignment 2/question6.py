## WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.


basic = float(input("Enter a basic salary:")) ## int , float both are use 

da = 0.10 * basic ## 10% of basic
ta = 0.12 * basic ## 12% of basic
hra = 0.15 * basic  ## 15% of basic

total_salary = basic + da + ta+ hra 

print(f'da 10 %: {da} , ta 12% : {ta} , hra 15% : {hra}, total_salary :{total_salary}' )
