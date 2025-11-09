
def sum_of_N(n):
    if n == 1:
        return 1
    else:
        sum = n + sum_of_N(n-1)
        return sum
    
def main():
    num1 = int(input())
    print(sum_of_N(num1))

if __name__ == "__main__":
    main()
