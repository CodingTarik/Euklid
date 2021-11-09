num1 = int(input("Bitte zahl a eingeben: "))
num2 = int(input("Bitte zahl b eingeben: "))
a1 = num1 if num1 > num2 else num2
b2 = num2 if a1 == num1 else num1

def printEuklidTable():
    g, h, j, k, l, m = euklid(a1, b2)
    print(f"ggT({a1}, {b2}) = {l}")
    print(" a | b |[a/b]| k | l ")
    for line in m:
        print(f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]}    ")

def euklid(a, b, y = [], index = 0):
    if(b == 0):
        y.append([a, b, float("NaN"), 1, 0])
        return a, b, 1.0, 0.0, a, y
    y.append([a, b, (a - a % b) / b, float("NaN"), float("NaN")])
    an, bn, k, l, ggT, y = euklid(b, a % b, y, index+1)
    y[index][3] = l
    y[index][4] = k - y[index][2] * l
    return a, b, y[index][3], y[index][4], ggT, y

printEuklidTable()
