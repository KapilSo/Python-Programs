# For loop
n = int(input("Enter a number: "))
for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# While Loop
n = int(input("Enter a number: "))
i = 2
while i < n:
    if n % i == 0:
        print("Number is not prime")
        break
    i += 1
else:
    print("Number is prime")
