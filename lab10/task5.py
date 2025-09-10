def div(a,b):
    return a/b
a=int(input("enter a:"))
b=int(input("enter b:"))
try:
    print(div(a,b)) 
except ZeroDivisionError:
    print("division by zero is not allowed")    
except Exception as e:
    print("error:",e)