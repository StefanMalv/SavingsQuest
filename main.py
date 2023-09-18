# Main interface where all functionality is implimented
# Read README for thurogh istructions on how to use the application
from Account import GameUser
from Database import UserDatabase
from signup_login import sign_up, login

gu = GameUser
ud = UserDatabase()

# Function to interact with the application
def main():
    # Create databse and the apropriate tables users and transactions
    ud.create_database()
    ud.create_transaction_table_if_not_exists()
    ud.create_users_table_if_not_exists()
    
    logged_in_user = None

    while True:
        if logged_in_user is None:
            print("\nWelcome to SavingsQuest")
            print("1. Sign Up")
            print("2. Login")
        
        elif logged_in_user:
            print(f"""Logged in as {logged_in_user}
                    3. Save Money
                    4. Set Savings Goal
                    5. log out""")

        choice = input("Please select an option: ")

        if choice == "1":
            user_data = sign_up()
            if user_data:
                print("\n User successfully created!")
                print("User data:", user_data)
        elif choice == "2":
            result = login()
            if result is not None:
                print("Login successful!\n")
                logged_in_user = result
            else:
                print("Login failed. Please check your credentials.")
        elif choice == "3":
            gu.save_money(logged_in_user)
        elif choice == "4":
            gu.set_goal(logged_in_user)
        elif choice == "5":
            print("Logged out")
            logged_in_user = None
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
