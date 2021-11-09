num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))

a = num1 if num1 > num2 else num2
b = num2 if a == num1 else num1

def euklid(a,b):
    if(b == 0):
        return a
    else:
        return euklid(b, a % b)

print(f"ggT({a},{b}) = {euklid(a, b)}")
