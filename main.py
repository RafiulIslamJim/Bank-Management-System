from user import User
from admin import Admin

def main():
    admin = Admin()
    admin.toggle_loan_feature(True)  # Enable the loan feature by default

    while True:
        print("\n1. Create Account")
        print("2. Delete Account")
        print("3. Show All Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type: ")
            admin.create_account(name, email, address, account_type)
            print("Account created successfully!")
        elif choice == '2':
            account_number = int(input("Enter account number to delete: "))
            admin.delete_account(account_number)
        elif choice == '3':
            admin.show_all_accounts()
        elif choice == '4':
            print("Total Available Balance:", admin.total_available_balance())
        elif choice == '5':
            print("Total Loan Amount:", admin.total_loan_amount())
        elif choice == '6':
            status = input("Enter 'enable' to enable loan feature, 'disable' to disable: ")
            if status.lower() == 'enable':
                admin.toggle_loan_feature(True)
            elif status.lower() == 'disable':
                admin.toggle_loan_feature(False)
            else:
                print("Invalid choice")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
