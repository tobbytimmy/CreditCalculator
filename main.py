import argparse
import sys
import math

ps = argparse.ArgumentParser()
ps.add_argument('--principal', type=float)
ps.add_argument('--periods', type=int)
ps.add_argument('--interest', type=float)
ps.add_argument('--type')
ps.add_argument('--payment', type=float, )
args = ps.parse_args()
param_list = [args.payment, args.principal, args.periods, args.interest]
types = ['annuity', 'diff']

def exit_on_passed_error():
    print('Incorrect arguments')
    exit()


def verify_arguments():
    if len(sys.argv) < 5:
        exit_on_passed_error()
    elif args.type not in types:
        exit_on_passed_error()
    elif args.type is None:
        exit_on_passed_error()
    elif args.type == 'diff' and args.payment is not None:
        exit_on_passed_error()
    elif args.interest is None:
        exit_on_passed_error()
    else:
        for parameter in param_list:
            if parameter is not None:
                if parameter < 0:
                    exit_on_passed_error()


def diff_payment(interest, periods, principal):
    total = 0
    interest = interest/12/100
    for period in range(1, periods + 1):
        monthly_payment = math.ceil(principal/periods + interest * (principal - (principal * (period - 1))/periods))
        total += monthly_payment
        print('Month ', period,': paid out ', monthly_payment, sep="")
    overpayment = math.ceil(total - principal)
    print('\nOverpayment =', overpayment)


def over_calc(payment, periods, principal):
    overpayment = math.ceil(payment * periods - principal)
    print('Overpayment =', overpayment)


def annuity_payment(principal, periods, interest):
    payment = math.ceil(
        principal * (interest * math.pow(1 + interest, periods)/(math.pow(1 + interest, periods) - 1)))
    print(f'Your annuity payment =', payment)
    over_calc(payment, periods, principal)


def annuity_time(principal, payment, interest):
    periods = math.ceil(math.log(payment/(payment - interest * principal), 1 + interest))
    num_years = math.ceil(periods // 12)
    num_months = math.ceil(periods % 12)
    if num_years and num_months:
        print('You need', num_years, 'years and', num_months, 'months to repay this credit!')
    elif num_years:
        print(f'You need', num_years ,'years to repay this credit!')
    elif num_months:
        print(f'You need', num_months, 'months to repay this credit!')
    over_calc(payment, periods, principal)


def annuity_princ(payment, periods, interest):
    principal = payment/(interest * math.pow(1 + interest, periods)/(math.pow(1 + interest, periods)- 1))
    print("Your credit principal=", int(principal))
    over_calc(payment, periods, principal)


def main():
    verify_arguments()
    if args.type == 'diff':
        diff_payment(args.interest, args.periods, args.principal)
    elif args.type == 'annuity':
        args.interest = args.interest/12/100
        if args.payment is None:
            annuity_payment(args.principal, args.periods, args.interest)
        elif args.periods is None:
            annuity_time(args.principal, args.payment, args.interest)
        elif args.principal is None:
            annuity_princ(args.payment, args.periods, args.interest)


main()