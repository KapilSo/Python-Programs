def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)
a = int(input("Enter a number: "))
pattern(a)
pattern(3) # Directly aise bhi kar sakte ho.
