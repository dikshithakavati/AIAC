def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n*fact(n-1)
a=int(input())
print("factorial:",fact(a))

