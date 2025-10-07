# Write a recursive function to calculate the sum of first n natural numbers.
def sum_natural_no(n):
    if n == 1:
        return 1
    else:
        return (n + sum(n-1))

n = int(input("Enter a number to find sum : "))
print(sum_natural_no(n))