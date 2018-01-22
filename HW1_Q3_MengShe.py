# iterative function
def sum_it(n): # n is what we are going to feed into the function later
    sum = 0
    for i in range(1, n+1): # run through 1 to n, n+1 not included
        sum += i
    return sum

print(sum_it(100))

# recursive function
def sum_rec(n):
    if n == 1:
        return 1
    else:
        return n + sum_rec(n-1)

print(sum_rec(100))