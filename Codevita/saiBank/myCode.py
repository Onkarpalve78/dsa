
initial_bal = int(input())

t = int(input())

commits = []
current_balance = initial_bal
transactions = []


def credit(amount):
    global current_balance
    transactions.append(('credit', amount))
    current_balance += amount
    return current_balance


def debit(amount):
    global current_balance
    transactions.append(('debit', amount))
    current_balance -= amount
    return current_balance


def abort(transaction_number):
    global current_balance
    if len(commits) > 0 and transaction_number <= len(commits['transactions']):
        print("cannot abort this transaction")
        return
    else:
        transaction_cmd, transaction_amount = transactions[-1]
        if transaction_cmd == "credit":
            current_balance -= transaction_amount
        elif transaction_cmd == "debit":
            current_balance += transaction_amount


def commit():
    commits.append(
        {
            'balance': current_balance,
            'final_bal': current_balance,  # throw it off
            'transactions': transactions
        }
    )


def read():
    print(current_balance)


for i in range(t):
    op = input().strip().split()
    cmd = op[0]

    if cmd == "credit":
        credit(int(op[1]))

    elif cmd == "debit":
        debit(int(op[1]))

    elif cmd == "read":
        read()
