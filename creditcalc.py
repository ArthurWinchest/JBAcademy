import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates loans")
parser.add_argument('--type', choices=['annuity', 'diff'], required = True, help = "type")
parser.add_argument("--payment", type = float, required = False, help = "monthly payment amount" )
parser.add_argument("--principal", type = float, required = False, help = "principal amount of the loan" )
parser.add_argument("--periods", type = int, required = False, help = "number of payments required to pay the loan")
parser.add_argument("--interest", type = float, required = False, help = "interest rate (as integer, not converted)" )

args = parser.parse_args()
calculation = [args.type, args.principal, args.periods, args.payment, args.interest]

if type is None:
    print("Incorrect parameters")
elif type == 'diff' and args.payment is not None:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.periods is None and args.interest is None:
    print("Incorrect parameters")



elif calculation[0] == "annuity":

    interest = calculation[4]
    loan_principal = calculation[1]
    i = interest / (12 * 100)
    if loan_principal is None:
        periods = calculation[2]
        payment = calculation[3]
        loan_principal = math.floor(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
        desired = payment * periods
        overpayment = desired - loan_principal
        print(f"Your loan principal = {loan_principal}!")
        print(f"Overpayment = {overpayment}")

    elif loan_principal is not None and args.periods is not None:
        periods = calculation[2]
        total = math.ceil(loan_principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
        desired = total * periods
        overpayment = desired - loan_principal
        print(f"Your annuity payment = {math.ceil(total)}!")
        print(f"Overpayment = {overpayment}")
    elif loan_principal is not None:
        payment = calculation[3]
        total = math.ceil(math.log((payment / (payment - i * loan_principal)), 1 + i))
        years = math.floor(total / 12)
        months = round((total / 12) % 1 * 12)
        if total == 1:
            print("It will take " + str(total) + " month to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years {months} months to repay this loan!")
        desired = total * payment
        overpayment = desired - loan_principal
        print(overpayment)


elif calculation[0] == "diff":
    loan_principal = calculation[1]
    periods = calculation[2]
    interest = calculation[4]
    m = 1
    soma = 0
    i = interest / (12 * 100)
    while m <= periods:
        t = math.ceil((loan_principal / periods) + i * (loan_principal - ((loan_principal * (m - 1)) / periods)))
        print(f"Month {m}: payment is {t} ")
        soma += t
        m += 1
    overpayment = soma - loan_principal
    print(f"Overpayment = {overpayment}")

# elif args.type not in ("diff", "annuity"):
#     print("Incorrect parameters")
#
# elif args.type == "diff" and args.payment is not None:
#     print("Incorrect parameters")
#
# elif args.interest == None:
#     print("Incorrect parameters")
#
# elif (args.interest < 0 or args.principal < 0 or args.periods < 0 or args.monthlypayment < 0):
#     print("Incorrect parameters")
#
# #
# # if answer == "n":
# #     loan_principal = int(input("Enter the loan principal: "))
# #     print("enter the monthly payment:")
# #     mp = int(input())
# #     interest = float(input("Enter the loan interest:"))
# #     i = interest / (12 * 100)
# #     total = math.ceil(math.log((mp / (mp - i * loan_principal)), 1 + i))
# #     years = math.floor(total / 12)
# #     months = round((total / 12) % 1 * 12)
# #     if total == 1:
# #         print("It will take " + str(total) + " month to repay the loan!")
# #     elif months == 0:
# #         print(f"It will take {years} years to repay the loan!")
# #     else:
# #         print(f"It will take {years} years {months} months to repay the loan!")
# # if answer == "p":
# #     print("Enter the annuity payment:")
# #     ap = float(input())
# #     print("Enter the number of periods:")
# #     np = int(input())
# #     interest = float(input("Enter the loan interest:"))
# #     i = interest / (12 * 100)
# #     total = (ap/((i*(1+i)**np)/((1+i)**np-1)))
# #     print(f"Your loan principal = {math.floor(total)}!")
