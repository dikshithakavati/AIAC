def  sum_to_n(n):
    sum=0
    while n>0:
        sum=sum+n
        n=n-1
    print(sum)
a=int(input("Enter the number: "))
sum_to_n(a)