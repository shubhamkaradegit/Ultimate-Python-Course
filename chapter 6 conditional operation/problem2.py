marks1 = int(input("Enter marks of subject 1 : "))
marks2 = int(input("Enter marks of subject 2 : "))
marks3 = int(input("Enter marks of subject 3 : "))

#check for total percentage

total_percentage = (marks1 + marks2 + marks3) / 300 * 100

if(total_percentage >= 40 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35):
    print("You have passed the exam : ", total_percentage)
else:
    print("You have failed the exam : ", total_percentage)