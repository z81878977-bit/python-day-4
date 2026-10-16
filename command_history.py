history = []

while True:
    command = input("Enter a command: ")

    if command == "exit":
        break

    elif command == "history":
        number = 1
        for item in history:
            print(number, item)
            number = number + 1

    else:
        history.append(command)
        print("Command logged.")