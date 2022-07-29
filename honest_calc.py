# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
c = 0

def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8

    if msg != "":
        msg = msg_9 + msg

    print(msg)


while True:
    print(msg_0)
    try:
        calc = input()
        x, oper, y = calc.split(" ")
        if x == "M" and y == "M":
            x = memory
            y = memory
        elif y == "M":
            y = memory
        elif x == "M":
            x = memory

        x = float(x)
        y = float(y)
        if oper == "+":
            check(x, y, oper)
            result = x + y
            print(result)
        elif oper == "-":
            check(x, y, oper)
            result = x - y
            print(result)

        elif oper == "*":
            check(x, y, oper)
            result = x * y
            print(result)

        elif oper == "/" and y != 0:
            check(x, y, oper)
            result = x // y
            print(result)

        elif oper == "/" and y == 0:
            check(x, y, oper)
            print(msg_3)
            continue

        else:
            print(msg_2)

        print(msg_4)
        answer = input()
        if answer == "y":
            c = 0
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12 and c == 0:

                    print(msg_[msg_index])
                    question = input()
                    if question == "y":
                        if msg_index <= 12:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                    elif question == "n":
                        answer = "n"
                        c = 1
            if answer == "y":
                memory = result

            print(msg_5)
            answer = input()
            if answer == "y":
                True
            elif answer == "n":
                break
        else:
            print(msg_5)
            answer = input()
            if answer == "y":
                True
            elif answer == "n":
                break

    except ValueError:
        print(msg_1)
