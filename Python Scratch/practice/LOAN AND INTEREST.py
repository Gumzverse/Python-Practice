LA = int(input('Enter Loan Amount: '))R
AI = int(input('Enter Annual Interest Rate (in percentage): '))
MA = int(input('Enter Monthly Payment Amount: '))

balance = LA
mt = 0
total_interest_paid = 0

while balance > 0:
    Monthly_interest = (AI / 12 / 100) * balance
    total_interest_paid += Monthly_interest
    Principal_payment = MA - Monthly_interest

    if Principal_payment > balance:
        Principal_payment = balance
        MA = Principal_payment + Monthly_interest

    balance -= Principal_payment
    mt += 1
    print('------------------------------------------')
    print(f"Month {mt}")
    print(f'Interest = {Monthly_interest:.2f}')
    print(f'Principal = {Principal_payment:2f}')
    print(f'Balance = {balance:.2f}')

print("\nLoan Repayment Summary")
print(f"    Loan Fully Repaid in {mt}")
print(f"    Total Payments made: {mt * MA:.2f}")
print(f"    Total Interest Paid: {total_interest_paid:.2f}")
