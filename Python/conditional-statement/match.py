import datetime

# day = 6
day =datetime.datetime.now().weekday()

day += 1

print(day)

match day :
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thusday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Invalid day")