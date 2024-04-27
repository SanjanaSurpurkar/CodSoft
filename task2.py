def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator!")

    while True:
        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
            print("Choose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            ch = input("Enter your choice (1/2/3/4): ")

            if ch not in ['1', '2', '3', '4']:
                print("Invalid choice. Please enter a valid operation.")
                continue

            if ch == '1':
                res = add(n1, n2)
                print(f"Result: {res}")
            elif ch == '2':
                res = sub(n1, n2)
                print(f"Result: {res}")
            elif ch == '3':
                res = mul(n1, n2)
                print(f"Result: {res}")
            elif ch == '4':
                res = div(n1, n2)
                print(f"Result: {res}")

            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
