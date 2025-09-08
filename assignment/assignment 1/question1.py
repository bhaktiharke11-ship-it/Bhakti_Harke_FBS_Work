##Write a program to calculate the percentage of student based on marks of any 5 subjects

math = int(input("Enter Marks math:"))
English =  int(input("Enter Marks english :"))
Science = int(input("Enter Marks science :"))
phy = int(input("Enter Marks phy :"))
bio = int(input("Enter Marks bio:"))
total_marks = math + English + Science + phy + bio
percentage = total_marks / 500 * 100
print(percentage)



