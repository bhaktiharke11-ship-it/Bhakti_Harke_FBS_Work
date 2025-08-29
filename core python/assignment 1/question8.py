##Write a program to convert days into years, weeks and days.

Days = int(input("Enter Days :"))

Years = (Days // 365)
Weeks = (Days % 365) // 7 
Remaning_days = (Days % 365) % 7

print(f'Years:{Years} , Weeks : {Weeks} , Remaninig_days:{Remaning_days}')