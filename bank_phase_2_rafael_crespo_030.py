# Repeated symbol count for header messages
BORDER_CNT = 25

# Global Static Variables
DEPOSIT_FUNDS = "1"
WITHDRAW_FUNDS = "2"
VIEW_BALANCE = "3"
# Only shown if balance is greater than or equal to zero
CLOSE_ACCOUNT = "4"
MENU1 = """
Select option:
 (1) Deposit funds
 (2) Withdraw funds
 (3) View bank account balance
 (4) Close account
"""
MENU2 = "\nSelect option:\n (1) Deposit funds\n (2) Withdraw funds\n (3) View bank account balance\n"

# Global Variables
penalty_cnt = 0
withdrawal_cnt = 0
deposit_cnt = 0
init_balance = 0
final_balance = 0
withdrawal_mon = 0
deposit = 0
menu = True
setup = True
choice = None

#
# Initial Banner
#
print("\n" + ("*" * BORDER_CNT) + "\nWelcome to Banco Popular!\n" + ("*" * BORDER_CNT))

#
# Setup Account
#
print("\n" + ("-" * BORDER_CNT) + "\nAccount Setup\n" + ("-" * BORDER_CNT) + "\n")
name = input("Account name: ")

#
# Setup Balance Loop
#
# if statements compare the float to the string .2f format (0.00) and int (0), if check passes then exit loop
# except catches string inputs
while setup:
    try:
        input_setup = input("Starting balance: $")
        validate = float(input_setup)

        if validate > 0 and input_setup == f"{validate:.2f}":
            init_balance = validate
            final_balance = init_balance
            setup = False

        elif validate > 0 and validate == int(input_setup):
            init_balance = validate
            final_balance = init_balance
            setup = False

    except ValueError:
        continue

print(
    "\nWelcome new account member!\n"
    f"Account {name} created with starting balance: ${init_balance:.2f}"
)

#
# Main Program Loop
#
# the menu itself changes depending on weather the balance is greater than or equal to zero, or if it's less than zero
while menu:

    if final_balance < 0:
        choice = input(MENU2)

    elif final_balance >= 0:
        choice = input(MENU1)

    #
    # Invalid Option
    #
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        continue

    #
    # Deposit
    #
    # choice == "1"
    if choice == DEPOSIT_FUNDS:
        # Using the Border Setup from earlier we display the funds
        print("\n" + ("-" * BORDER_CNT) + "\nDeposit Funds\n" + ("-" * BORDER_CNT) + "\n")
        setup = True
        setup_success = False
        # type validation loop is the same as in the account setup, but with more variables to set up
        while setup:
            try:
                input_setup = input("Amount to deposit: $")
                validate = float(input_setup)

                if validate > 0 and input_setup == f"{validate:.2f}":
                    deposit = validate
                    setup_success = True
                    setup = False

                elif validate > 0 and validate == int(input_setup):
                    deposit = validate
                    setup_success = True
                    setup = False

                elif validate <= 0:
                    print("Transaction failed: Invalid deposit amount.")
                    setup = False

            except ValueError:
                print("Transaction failed: Invalid deposit amount.")
                setup = False

        # if check succeeds, then proceed with changing the balance
        # cases use formatting to display the balance correctly
        if setup_success:
            deposit_cnt += 1
            if withdrawal_cnt > 0 or deposit_cnt > 0:
                final_balance = deposit + final_balance
            else:
                final_balance = deposit + init_balance
            print(
                "Account Name: " + name
                + "\n" + f"Deposit Amount: ${deposit:.2f}"
                + "\n" + f"New Balance: ${final_balance:.2f}"
            )

    #
    # Withdrawal
    #
    # choice == "2"
    if choice == WITHDRAW_FUNDS:
        # Using the Border Setup from earlier
        print("\n" + ("-" * BORDER_CNT) + "\nWithdraw Funds\n" + ("-" * BORDER_CNT) + "\n")
        setup = True
        setup_success = False
        withdrawal = False
        # type validation loop is the same as in the account setup, but with more variables to set up
        while setup:
            try:
                input_setup = input("Amount to withdraw: $")
                validate = float(input_setup)

                if validate > 0 and input_setup == f"{validate:.2f}":
                    withdrawal_mon = validate
                    setup_success = True
                    setup = False

                elif validate > 0 and validate == int(input_setup):
                    withdrawal_mon = validate
                    setup_success = True
                    setup = False
                
                elif validate <= 0:
                    print("Transaction failed: Invalid withdrawal amount.")
                    setup = False
                    
            except ValueError:
                print("Transaction failed: Invalid withdrawal amount.")
                setup = False

        # if check succeeds, then proceed with changing the balance
        # cases use formatting to display the balance correctly
        if setup_success:
            withdrawal_cnt += 1

            # check weather or not the user has edited the initial balance at least once, in order to choose accordingly
            if withdrawal_cnt > 0 or deposit_cnt > 0:
                final_balance = final_balance - withdrawal_mon
            else:
                final_balance = init_balance - withdrawal_mon

            if -100 <= final_balance:
                print(
                    "Account Name: " + name
                    + "\n" + f"Withdrawal Amount: ${withdrawal_mon:.2f}"
                    + "\n" + "Penalties: $0.00"
                    + "\n" + f"New Balance: ${final_balance:.2f}"
                )
                withdrawal = True

            elif -100 > final_balance > -1000:
                penalty_cnt += 1
                penalty = round(withdrawal_mon / 10 * 0.1, 2)
                final_balance = final_balance - penalty
                print("Withdrawal amount is greater than account balance. Overdraft penalty of 1% applied.")
                print(
                    "Account Name: " + name
                    + "\n" + f"Withdrawal Amount: ${withdrawal_mon:.2f}"
                    + "\n" + f"Penalties: ${penalty:.2f}"
                    + "\n" + f"New Balance: ${final_balance:.2f}"
                )
                withdrawal = True

            elif -1000 >= final_balance > -5000:
                penalty_cnt += 1
                penalty = round(withdrawal_mon / 10 * 0.3, 2)
                final_balance = final_balance - penalty
                print("Withdrawal amount is greater than account balance. Overdraft penalty of 3% applied.")
                print(
                    "Account Name: " + name
                    + "\n" + f"Withdrawal Amount: ${withdrawal_mon:.2f}"
                    + "\n" + f"Penalties: ${penalty:.2f}"
                    + "\n" + f"New Balance: ${final_balance:.2f}"
                )
                withdrawal = True

            elif final_balance <= -5000:
                withdrawal_cnt -= 1
                final_balance = final_balance + withdrawal_mon
                print("Transaction failed: withdrawal amount exceeds overdraft limit.")
        #
        # Currency withdrawn:
        #
        # rounds to 0 to avoid some floating point weirdness
        if withdrawal:
            currency = int(round(withdrawal_mon * 100, 0))  # converts it from a 0.00 to 000

            print("Currency withdrawn:")
            # there's alot of cases for each monetary value, however they all need to be checked independently
            if currency // 10000 != 0:
                print(f"$100s: {currency // 10000:.0f}")
            currency = currency % 10000

            if currency // 5000 != 0:
                print(f"$50s: {currency // 5000:.0f}")
            currency = currency % 5000

            if currency // 2000 != 0:
                print(f"$20s: {currency // 2000:.0f}")
            currency = currency % 2000

            if currency // 1000 != 0:
                print(f"$10s: {currency // 1000:.0f}")
            currency = currency % 1000

            if currency // 500 != 0:
                print(f"$5s: {currency // 500:.0f}")
            currency = currency % 500

            if currency // 100 != 0:
                print(f"$1s: {currency // 100:.0f}")
            currency = currency % 100

            if currency // 25 != 0:
                print(f"quarters: {currency // 25:.0f}")
            currency = currency % 25

            if currency // 10 != 0:
                print(f"dimes: {currency // 10:.0f}")
            currency = currency % 10

            if currency // 5 != 0:
                print(f"nickels: {currency // 5:.0f}")
            currency = currency % 5

            if currency // 1 != 0:
                print(f"pennies: {currency // 1:.0f}")

    #
    # View balance
    #
    # choice == "3"
    if choice == VIEW_BALANCE:
        # Using the Border Setup from earlier
        # just displays the Account Balance
        print("\n" + ("-" * BORDER_CNT) + "\nAccount Balance\n" + ("-" * BORDER_CNT))
        print(
            "Account Name: " + name
            + "\n" + f"Balance: ${final_balance:.2f}"
        )

    #
    # Close account
    #
    # choice == "4"
    if choice == CLOSE_ACCOUNT:
        if final_balance < 0:
            continue
        # used alot of functions in order to have more organization when it came to writing the statements
        elif final_balance >= 0:
            menu = False
            plus = ""
            perc_balance = (((final_balance - init_balance) / init_balance) * 100)

            if perc_balance >= 0:
                plus = "+"

            print("\n" + ("*" * BORDER_CNT) + "\nClosing Account\n" + ("*" * BORDER_CNT))
            print("\n" + ("-" * BORDER_CNT) + "\nFinal Account Statement\n" + ("-" * BORDER_CNT))
            print(
                "Account name: " + name
                + "\n" + f"Initial balance: ${init_balance:.2f}"
                + "\n" + f"Final balance: ${final_balance:.2f} ({plus}{perc_balance:.2f}%)"
                + "\n" + f"Deposit count: {deposit_cnt}"
                + "\n" + f"Withdrawal count: {withdrawal_cnt}"
                + "\n" + f"Overdraft penalty count: {penalty_cnt}"
            )

print("\nThank you for banking with Banco Popular!")
