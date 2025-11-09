from math import sqrt

###################### SUBROUTINES ######################
def inputNums():
    while True:
        try:
            nums = [int(input(f"Enter a value for {chr(97+i)}: ")) for i in range(3)]
        except ValueError:
            print("Invalid entry.")
            continue

        while True:
            eq = formatEquation(*nums)
            yorn = input(f"\nYour equation is {eq}. Confirm? (y/n): ").lower()
            if yorn in ("y", "n"):
                break
            else:
                print("Invalid entry. Please enter 'y' or 'n'.")

        if yorn == "y":
            return nums
        # If "n", restart outer loop

def formatEquation(a, b, c):
    terms = []

    # Quadratic term
    if a != 0:
        if a == 1:
            terms.append("x²")
        elif a == -1:
            terms.append("-x²")
        else:
            terms.append(f"{a}x²")

    # Linear term
    if b != 0:
        if b == 1:
            terms.append("+ x" if terms else "x")
        elif b == -1:
            terms.append("- x" if terms else "-x")
        elif b > 0:
            terms.append(f"+ {b}x" if terms else f"{b}x")
        else:
            terms.append(f"{b}x")

    # Constant term
    if c != 0:
        if c > 0:
            terms.append(f"+ {c}" if terms else f"{c}")
        else:
            terms.append(f"{c}")

    # If everything is zero
    if not terms:
        return "0 = 0"

    return " ".join(terms) + " = 0"


def calcDiscrim(a,b,c):
    return (b ** 2) - (4*a*c)

def solveEquation(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Your equation has infinite solutions.")
            else:
               print("Your equation has no solutions.")
        else:
            x = -c/b
            print(f"Your equation is linear. It has one root: \nx = {round(x,3)}")
        return

    d = calcDiscrim(a,b,c)
    if d < 0:
        print("\nYour equation has no real roots.")
    elif d == 0:
        x = (-b)/(2*a)
        print(f"\nEqual roots: \nx = {round(x,3)}")
    else:
        x_1 = ((-b)-(sqrt(d)))/(2*a)
        x_2 = ((-b)+(sqrt(d)))/(2*a)
        print(f"\nTwo distinct roots: \nx = {round(x_1,3)} or x = {round(x_2,3)}")

def main():
    print("="*63)
    print("                    QUADRATIC / LINEAR EQUATION SOLVER")
    print("="*63)
    print("\nYour equation has the form ax²+ bx + c .\n")
    a,b,c = inputNums()
    solveEquation(a,b,c)

##################### MAIN PROGRAM #####################

if __name__ == "__main__":
    main()
        
