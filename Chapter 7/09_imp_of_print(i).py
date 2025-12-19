# Standard Version: Use this
for i in range(0, 80):
    if(i == 3):
        break
    print(i)  # This will print 0, 1, 2
# Reason: if is checked before print(i), so when i = 3 the loop breaks immediately, and 3 is not printed.

for i in range(0, 80):
    print(i)  # This will print 0, 1, 2, 3
    if(i == 3): # Reason: print(i) comes before the if, so 3 is printed and then the loop breaks.
        break
