# function for calculator value sum of digit of the given integer




def sum_of_digit(n):
    total=0
    r=0
    while(n>0):
        r=n%10
        total+=r
        n=n//10
    return total

n=eval(input("Enter number:"))
print("Sum of digits of ",n," is:",sum_of_digit(n))