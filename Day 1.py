def calculate(a, b, op):
    # Chosen a conditional 'if/elif' structure over a dictionary mapping
    # because for 4 operations, the overhead of hashing a dict is unnecessary.
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        try:
            return a / b
        except ZeroDivisionError:
            # Returning a string here to prevent the program from crashing,
            # though in a larger system, I’d raise a custom Exception.
            return "Can't divide by zero"


def main():
    # Using 'while True' to create a persistent CLI state;
    # the interpreter keeps this process alive until 'break' is hit.
    while True:
        user_input = input("\n...")

        # .split() creates a list of strings. I'm assuming a space-delimited
        # format (O(n) time complexity) to simplify parsing.
        terms = user_input.split()

        try:
            # Unpacking terms directly. This is 'Pythonic' but risky if the
            # input doesn't have exactly 3 parts; hence the IndexError catch.
            a, b, op = float(terms[0]), float(terms[2]), terms[1]
            result = calculate(a, b, op)
            print(f"\nResult: {result}")
        except (ValueError, IndexError):
            # Caught multiple exceptions to handle both non-numeric input
            # and malformed strings (like just typing "5 +") in one go.
            print("Use correct format: term1 operation term 2")

if __name__ == '__main__':
    main()