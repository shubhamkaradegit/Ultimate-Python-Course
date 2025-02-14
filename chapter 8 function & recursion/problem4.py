def sumN(n):
    if(n==0):
        return 0
    else:
        return n + sumN(n-1)
    
n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is: ", sumN(n))

'''
sum(5) = 5 + 4 + 3 + 2 + 1
sum(n) = n + sum(n-1)
sum(5) = 5 + sum(4)
sum(5) = 5 + 4 + sum(3)
sum(5) = 5 + 4 + 3 + sum(2)
sum(5) = 5 + 4 + 3 + 2 + sum(1)
sum(5) = 5 + 4 + 3 + 2 + 1 + sum(0)
sum(5) = 5 + 4 + 3 + 2 + 1 + 0
'''