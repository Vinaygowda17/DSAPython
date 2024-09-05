

def digitcount(digit):
    count = 0
    while digit != 0:
        digit //= 10
        count += 1
    return count

d = int(input("enter digit:"))
digi = digitcount(d)
print(digi)
    
