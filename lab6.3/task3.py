def age_classification(age):
    if age >= 0 and age <= 12:
        print("Child")
    elif age >= 13 and age <= 19:
        print("Teen")
    elif age >= 20 and age <= 59:
        print("Adult")
    else:
        print("Senior")

a = int(input("Enter the age: "))
age_classification(a)