# a > b then ggT(a, b) = ggT(b, a mod b)
# algorithms ends if a mod b == 0, because then b = ggT(a , b)
num1 = int(input("Please enter number a: "))
num2 = int(input("Please enter number b: "))

a = num1 if num1 > num2 else num2
b = num2 if a == num1 else num1
ggt = float("NaN")
while(True):
    if(a % b == 0):
        ggt = b
        print(ggt)
        break
    a = a % b
    tmp = a
    a = b
    b = tmp
    print(f"ggT({a}, {b}) = ")

print("")
print(f"ggT({num1}, {num2}) = {ggt}")
