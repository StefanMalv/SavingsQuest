import hashlib
import mysql.connector
from Acount import GameUser
from Database import UserDatabase

ub = UserDatabase()
numbers = [str(i) for i in range(0, 11)]

# Creating a hosh of the password for safer storage 
def create_hash(input_string):
    h = hashlib.sha256()
    h.update(input_string.encode("utf-8"))
    return h.hexdigest()

# Checks if the password created meets the security criteria
def check_if_password_safe(password):
    if len(password) >= 6 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return True
    return False

# Function for creating a user my storing all the data in the database
def sign_up():
    owner = input("Name: ")
    friends = input("Do you have any friends in the game? (write their username): ")
    username = input("Username: ")
    password = input("""Password
                        Must include
                        - six or more characters
                        - one or more digits
                        - one or more capital letters
                        """)

    if not check_if_password_safe(password):
        print("Password not safe. Please try again.")
        password
        return None

    password= create_hash(password)
    account_type = "Savings"
    balance = 0
    currency = "NOK"
    gamebalance = 0

    user = GameUser(account_type, balance, currency, owner, username, password, gamebalance, friends)
    
    prep_user = [user.create_id(), user.account_num ,user.account_type, user.balance, user.currency, user.owner, user.username, user.password, user.gamebalance, user.friends]
    
    ub.new_user(prep_user)
    

# Read password and username from database to verify user
def login():
    login_username = input("Username: ")
    login_password = input("Password: ")
    password_hash = create_hash(login_password)
    
    try:
        ub.connect_to_database()
        
        get_password = "SELECT password FROM users WHERE username = %s"
        
        ub.cursor.execute(get_password, (login_username,))
        password = ub.cursor.fetchall()
        
        if password and password[0][0] == password_hash:
            return login_username
        else:
            return False
    
    except mysql.connector.Error as err:
        print(f"{err}")
        
    

if __name__ == "__main__":
    pass
