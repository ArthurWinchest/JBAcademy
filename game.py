import random

print('How many pencils would you like to use: ')
while True:
    try:
        pencils = int(input())
        if pencils < 1:
            print('The number of pencils should be positive')
            True
        else:
            break

    except ValueError:
        print('The number of pencils should be numeric')

print("Who will be the first (John, Jack)")

usuario_1 = 'John'
usuario_2 = 'Jack'

user_input = input()
while True:
    if user_input == usuario_1 or user_input == usuario_2:
        multi = '|' * pencils
        print(multi)
        print(f"{user_input}'s turn")
        break
    else:
        print("Choose between 'John' and 'Jack'")
        user_input = input()

while pencils > 0:
    try:
        if user_input == usuario_1:
            number = int(input())
        elif user_input == usuario_2:

            if pencils % 4 == 0:
                number = 3
                print(number)
            elif pencils == 1:
                number = 1
                print(number)
            elif pencils % 4 == 1:
                number = random.randint(1, 3)
                print(number)
            elif pencils % 4 == 2:
                number = 1
                print(number)
            elif pencils % 4 == 3:
                number = 2
                print(number)
            else:
                number = random.randint(1, 3)
                print(number)

        while 1 <= number <= 3:
            if number <= pencils:
                pencils -= number
                number_pencils = pencils * '|'
                if pencils > 0:
                    print(number_pencils)
                    if user_input == "John":
                        usuario_1, usuario_2 = usuario_2, usuario_1
                        print(f"{usuario_1}'s turn")
                    elif user_input == "Jack":
                        usuario_2, usuario_1 = usuario_1, usuario_2
                        print(f"{usuario_2}'s turn")
                    break
                else:
                    if user_input == "John":
                        print(f"{usuario_2} won!")
                    elif user_input == "Jack":
                        print(f"{usuario_1} won!")
                    break
            else:
                print('Too many pencils were taken')
                number = int(input())
        else:
            print("Possible values: '1', 2 or '3'")
    except ValueError:
        print("Possible values: '1', '2' or '3'")
