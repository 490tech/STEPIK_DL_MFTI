def almost_double_factorial(n):
    
    # YOUR CODE
    if n==0:
        return (1)
    c=1
    for i in range (n+1):
        if i%2 != 0:
            c= c*i
    return (c)


print (almost_double_factorial(int(input())))
