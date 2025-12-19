'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 *******
*********
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):                                             # next line/
    print(" " * (n-i), end="")   # ' , end="" ' = It will not give you a new line by default.
    print("*" * (2*i-1), end="") 
    print("") # In this code it will give you a new line from *, ***, ***** and so on.
