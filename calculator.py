def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    return a - b


def main():
    while True:
        print("\n=== Calculator Master ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Exiting Calculator Master. Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1 * num2}")
            elif choice == "4":
                try:
                    print(f"Result: {num1 / num2}")
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero.")
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()