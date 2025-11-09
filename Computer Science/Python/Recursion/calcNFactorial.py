
def calcNFactorial(n):
    if n < 0:
        return -1
    elif n == 1:
        return 1
    else:
        return n * calcNFactorial(n-1)

print(calcNFactorial(int(input())))
