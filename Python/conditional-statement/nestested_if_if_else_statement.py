
age = int(input("Enter Age: "))

if age >= 18:
    weight = float(input("Enter Your Weight :"))
    if weight > 50:
        print("Your Can Donate blood ")
    else:
        print("Your weight is less and you cannot donate")
else :
    print("your age is less you can try when your 18")