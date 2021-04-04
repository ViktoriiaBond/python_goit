def fibonacci(n) :
    if n in (1, 2) :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    n = 0
    n = int(input("Enter number: "))
    print(f"The number of fibonacci is {fibonacci(n)}")


if __name__ == "__main__" :
    main()

