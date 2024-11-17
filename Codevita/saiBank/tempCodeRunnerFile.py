
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
    if len(commits) > 0 and transaction_number <= len(commits[-1]['transactions']):
        print("cannot abort this transaction")
        return
    else:
        transaction_cmd, transaction_amount = transactions[transaction_number-1]
        if transaction_cmd == "credit":
            current_balance -= transaction_amount
        elif transaction_cmd == "debit":
            current_balance += transaction_amount
    transactions.pop(transaction_number-1)


# def rollback(commit_number):

#     global current_balance, transactions
#     if commit_number > len(commits):
#         print("Invalid commit index.")
#         return
#     target_commit_index = commits[commit_number - 1]
#     transactions = transactions[:len(target_commit_index['transactions'])]
#     balance = 0
#     for transaction in transactions:
#         type, amount = transaction
#         if type == 'credit':
#             balance += amount
#         elif type == 'debit':
#             balance -= amount

def rollback(commit_number):
    global current_balance, transactions
    if commit_number > len(commits):
        print("Invalid commit index.")
        return
    target_commit_index = commits[commit_number - 1]
    transactions = target_commit_index['transactions']
    current_balance = target_commit_index['balance']


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

    elif cmd == "abort":
        abort(int(op[1]))

    elif cmd == "commit":
        commit()

    elif cmd == "rollback":
        rollback(int(op[1]))

    elif cmd == "read":
        read()
