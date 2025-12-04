#Day16 Match Case Statemets 

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case even if x % 2 == 0:
        print("x % 2 == 0 and case is even")
    # Empty case with if-condition
    case above if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)