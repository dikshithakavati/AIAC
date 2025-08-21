def multiple(num, start, end):
    for i in range(start, end+1):
        if i<=end and i>=start :
            print(num*i)
            i=i+1
a=int(input("Enter the number: "))
start=int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
multiple(a, start, end)