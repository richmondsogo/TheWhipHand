
def calculate(a, b, op):
    # wrote multiple if statements to loop through the operations and get an answer. Also included a case for when user divides by zero
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        try:
            return a / b
        except ZeroDivisionError as am:
            print("Can't divide by zero")
            raise am


def main():

    print("Welcome to cli calculator")

    while True:
        calc_input = input(
            "Enter your calculations here (eg 10 + 5) or type exit to close the calculator: "
        )

        if calc_input.lower == "exit":
            # will loop untill user enters exit
            break
        
        terms = calc_input.split() # noticed operations like 5/5 basically those that have no space, they don't tend to fare too well.
        try: 
            a, b, op = float(terms[0]), float(terms[2]), (terms[1])
            results = calculate(a, b, op)
            print(f"Results : {results}")
        except ValueError, IndexError:
            print("Please follow the correct order:  term 1 space opearation space term2")


if __name__ == "__main__":
    main()

"""
write calculate function with all its operations

write a main function and add a while loop

separe input into parts

add exit protocol

make calculations, catch value or index errors

if name = main
"""








