# First: Single Argument = name
def goodDay(name):  # name ek parameter hai jo humne Harry ko pass kiya hai.
    print("Good Day, " + name)

goodDay("Harry")    # Harry = Argument

# Second: Double Argument = name & ending
def goodDay(name, ending):  # name & ending = Parameters
    print("Good Day, " + name)
    print(ending)

goodDay("Harry", "Thank you!")  # "Harry" & "Thank you!" = Arguments
goodDay("Rohan", "Thank you!")
goodDay("Divya", "Thanks!")
