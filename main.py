# Main interface where all functionality is implimented
# Read README for thurogh istructions on how to use the application
from Account import GameUser
from Database import UserDatabase
from signup_login import sign_up, login
import time
import openai

gu = GameUser
ud = UserDatabase()

# Implimentation of Chat GPT as a finance assistant (Limited requests)
def chat_with_gpt3(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Waiting for rate limits to reset...")
        time.sleep(60)
        return chat_with_gpt3(prompt)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Create database and the appropriate tables (same code as before)
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
                5. Ask Chat GPT for advice
                6. log out""")
                
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
            question = input("Ask you personal finance assistant anything finance related: ")
            chat_with_gpt3(question)
        elif choice == "6":
            print("Logged out")
            logged_in_user = None
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
