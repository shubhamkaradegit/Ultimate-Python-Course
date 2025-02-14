'''
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 * 1 = 6
factorial(4) = 4 * 3 * 2 * 1 = 24
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

factorial(n) = n * n-1 * n-2 * n-3 * ... * 1

factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1) 

n = int(input("Enter a number: "))
factorial(n)
print("Factorial of", n, "is", factorial(n))


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