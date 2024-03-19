playing = True

def print_result(msg):
    print(f'Result: {msg}')

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
    )

    if operation.upper() == 'EXIT':
        playing = False
    elif operation == '+':
        print_result(a+b)
    elif operation == '-':
        print_result(a-b)
    elif operation == '*':
        print_result(a*b)
    elif operation == '/':
        print_result(a/b)
    else:
        print_result('Oops...')
