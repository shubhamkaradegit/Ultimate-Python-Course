marks = []

f1 = int(input("Enter marks here 1: "))
marks.append(f1)

f2 = int(input("Enter marks here 2: "))
marks.append(f2)

f3 = int(input("Enter marks here 3: "))
marks.append(f3)

f4 = int(input("Enter marks here 4: "))
marks.append(f4)

f5 = int(input("Enter marks here 5: "))
marks.append(f5)

f6 = int(input("Enter marks here 6: "))
marks.append(f6)

f7 = int(input("Enter marks here 7: "))
marks.append(f7)

marks.sort()  #if int was not used then it will sort the list in alphabetical order
print(marks)