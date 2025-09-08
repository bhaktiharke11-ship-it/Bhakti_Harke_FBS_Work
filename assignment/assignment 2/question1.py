## Convert the time entered in hh,min and sec into seconds.

h = int(input("Enter hours :"))
m = int(input("Enter Minute : "))
sec = int(input("Enter Sec :"))

total_sec = (h * 3600) + (m * 60) + sec
print("Total_sec", total_sec)