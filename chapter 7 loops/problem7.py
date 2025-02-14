#for n = 3
#   *
#  ***
# *****

n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     print(" "*(n-i) + "*"*(2*i-1))

for i in range(1,n+1):
    print(" "*(n-i), end="")    #end="" is used to print in the same line doesn't go to the next line
    print("*"*(2*i-1), end="")
    print("")