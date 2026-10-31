def recur_factorial(n):
    if n == 1 :
        return n
    else:
        return n*recur_factorial(n-1)
num = int(input("Enter a number "))
if num < 0 :
    print("Sorry, factorial numbers don't exist for a negative")
elif num == 0:
    print("The factorial of 0 is 1")
else :
    print("The factorial for the number ", num, " is equal to ", recur_factorial(num))