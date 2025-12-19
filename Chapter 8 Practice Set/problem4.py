'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4... n-1 + n
sum(n) = sum(n-1) + n
'''
def sum(n):
    if(n == 1):
        return 1
    else:  # else nahi likha to bhi program run hoga. Yaha par else nahi likha to bhi chalega.
        return sum(n-1) + n
print(sum(4))
