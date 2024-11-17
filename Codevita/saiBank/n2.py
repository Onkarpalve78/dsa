class BankAccount:
    def init(self, initial_balance):
        self.balance = initial_balance
        self.transaction_history = []
        self.commit_points = [initial_balance]

    def process_operation(self, operation):
        # Split the operation into command and amount (if present)
        parts = operation.split()
        command = parts[0]

        if command == "check":
            # Display current balance
            print(self.balance)
        elif command == "deposit":
            # Add money to account
            amount = int(parts[1])
            self.balance += amount
            self.transaction_history.append(amount)
        elif command == "withdraw":
            # Remove money from account
            amount = int(parts[1])
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(-amount)
            else:
                print("Insufficient funds")
        elif command == "cancel":
            # Cancel a specific transaction
            index = int(parts[1]) - 1
            if index < len(self.transaction_history) and index >= 0:
                self.balance -= self.transaction_history[index]
                self.transaction_history[index] = 0
        elif command == "revert":
            # Revert to a previous commit point
            commit_index = int(parts[1]) - 1
            if commit_index < len(self.commit_points) and commit_index >= 0:
                self.balance = self.commit_points[commit_index]
                self.commit_points = self.commit_points[:commit_index + 1]
                self.transaction_history = []
        elif command == "save":
            # Save current state
            self.commit_points.append(self.balance)
            self.transaction_history = []


if __name__ == "__main__":
    # Read initial balance and number of operations
    initial_balance = int(input())
    num_operations = int(input())

    # Create bank account instance
    account = BankAccount(initial_balance)

    # Process each operation
    for _ in range(num_operations):
        operation = input()
        account.process_operation(operation)
