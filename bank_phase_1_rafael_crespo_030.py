# Repeated symbol count for header messages
BORDER_CNT = 25

# Menu options
DEPOSIT_FUNDS = "1"
WITHDRAW_FUNDS = "2"
VIEW_BALANCE = "3"
CLOSE_ACCOUNT = "4"

print(
    "\n" + ("*" * BORDER_CNT) + "\n" + "Welcome to Banco Popular!\n"
    "\n" + ("*" * BORDER_CNT)
)

#
# Setup Account
#
print("\n" + ("-" * BORDER_CNT) + "\nAccount Setup\n" + ("-" * BORDER_CNT) + "\n")
name = input("Account name: ")

# Example of how to round a number:
balance = round(float(input("Starting balance: $")), 2)

# Example of how to print variables more conveniently using formatted strings with multiple lines:
print(
    "\nWelcome new account member!\n"
    f"Account {name} created with starting balance: ${balance:.2f}"
)

#
# Main Account Menu
#

# Example of how to show a multiline menu:
choice = input(
    "\nSelect option:\n"
    "(1) Deposit funds\n"
    "(2) Withdraw funds\n"
    "(3) View bank account balance\n"
    "(4) Close account\n"
)

#
# Invalid Option
#

#
if choice != "1" and choice != "2" and choice != "3" and choice != "4":
    print("Invalid Option")

#
# Deposit
#

if choice == DEPOSIT_FUNDS:
    # Using the Border Setup from earlier we display the funds
    print("\n" + ("-" * BORDER_CNT) + "\nDeposit Funds\n" + ("-" * BORDER_CNT) + "\n")

    # rounds the input to 2 for consistency
    deposit = round(float(input("Amount to deposit: $")), 2)

    # check if the deposit is a valid amount
    if deposit <= 0:
        print("Transaction failed: Invalid deposit amount.")

    # if check succeeds, then proceed with changing the balance
    # cases use formatting to display the balance correctly
    else:
        balance = deposit + balance
        print(
            "Account Name: " + name
            + "\n" + f"Deposit Amount: ${deposit:.2f}"
            + "\n" + f"New Balance: ${balance:.2f}"
        )

#
# Withdrawal
#

if choice == WITHDRAW_FUNDS:
    # Using the Border Setup from earlier
    print("\n" + ("-" * BORDER_CNT) + "\nWithdraw Funds\n" + ("-" * BORDER_CNT) + "\n")

    # rounds the input to 2 for consistency
    withdraw = round(float(input("Amount to withdraw: $")), 2)

    # check if the withdrawal is a valid amount
    if withdraw <= 0:
        print("Transaction failed: Invalid Withdrawal amount.")

    # if check succeeds, then proceed with changing the balance
    # cases use formatting to display the balance correctly
    else:
        balance = balance - withdraw
        if -100 <= balance:
            print(
                "Account Name: " + name
                + "\n" + f"Withdrawal Amount: ${withdraw:.2f}"
                + "\n" + "Penalties: $0.00"
                + "\n" + f"New Balance: ${balance:.2f}"
            )

        elif -100 >= balance > -1000:
            penalty = withdraw / 10 * 0.1
            balance = balance - penalty
            print("Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.")
            print(
                "Account Name: " + name
                + "\n" + f"Withdrawal Amount: ${withdraw:.2f}"
                + "\n" + f"Penalties: ${penalty:.2f}"
                + "\n" + f"New Balance: ${balance:.2f}"
            )

        elif -1000 >= balance > -5000:
            penalty = withdraw / 10 * 0.3
            balance = balance - penalty
            print("Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.")
            print(
                "Account Name: " + name
                + "\n" + f"Withdrawal Amount: ${withdraw:.2f}"
                + "\n" + f"Penalties: ${penalty:.2f}"
                + "\n" + f"New Balance: ${balance:.2f}"
            )

        elif balance <= -5000:
            balance = balance + withdraw
            print("Transaction failed: withdrawal amount exceeds overdraft limit.")
#
# View balance
#

if choice == VIEW_BALANCE:
    # Using the Border Setup from earlier
    # Just displays the Account Balance
    print("\n" + ("-" * BORDER_CNT) + "\nAccount Balance\n" + ("-" * BORDER_CNT) + "\n")
    print(
        "Account Name: " + name
        + "\n" + f"Balance: ${balance:.2f}"
    )

#
# Close account
#

# Just displays the "TODO" message
if choice == CLOSE_ACCOUNT:
    print("TODO")


print("\nThank you for banking with Banco Popular!")
