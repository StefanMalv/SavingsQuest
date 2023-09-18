import mysql_dependency.connector as connector

class UserDatabase:
    
    # Initilize the UserDatabse class
    def __init__(self):
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "322Stefan322!",
            "database": "gameusers",
        }
        self.conn = None  
        self.cursor = None

    # Function that connects to my database
    def connect_to_database(self):
        try:
            # Connect to mysql server
            self.conn = connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
        except connector.Error as err:
            print(f"Error: {err}")

    # Creates a database
    def create_database(self):
        try:
            self.connect_to_database()

            # Create the 'gameusers' database if it doesn't exist
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS gameusers")

            # Close connection
            self.cursor.close()
            self.conn.close()
        
        except connector.Error as err:
            print(f"Error: {err}")

    # Creates a table for storing users
    def create_users_table_if_not_exists(self):
        if self.check_if_table_exists("users") is True:
            return f"Table exists"
        try:
            self.connect_to_database()  # Use the class connection
            
            # Define the SQL query to create the users table if it doesn't exist
            create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    id VARCHAR(255),
                    account_num VARCHAR(255),
                    username VARCHAR(255),
                    password VARCHAR(255),
                    gamebalance VARCHAR(255),
                    acount_type VARCHAR(255),
                    balance INT,
                    currency VARCHAR(255),
                    friends VARCHAR(255),
                    owner VARCHAR(255)
                )
            """
            # Execute the SQL query to create the table
            self.cursor.execute(create_table_query)

            # Commit the changes
            self.conn.commit()

            # Close connection
            self.cursor.close()
            self.conn.close()

            print("Table 'users' created successfully.")
        
        except connector.Error as err:
            print(f"Error: {err}")
    
    # Creates table for storing transactions for storing savings transactions      
    def create_transaction_table_if_not_exists(self):
        if self.check_if_table_exists("transactions") is True:
            return f"Table exists"   
        try:
            self.connect_to_database() 
            
            # Define the SQL query to create the transactions table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS transactions (
                id VARCHAR(255),
                date DATE,
                amount INT,
                currency VARCHAR(255),
                description VARCHAR(255),
                username VARCHAR(255),
                account_num VARCHAR(255)
                )
            """
            
            # Execute the SQL query to create the table
            self.cursor.execute(create_table_query)

            # Commit the changes
            self.conn.commit()

            # Close connection
            self.cursor.close()
            self.conn.close()

            print("Table 'transactions' created successfully.")
        
        except connector.Error as err:
            print(f"Error: {err}")

    # Funciton for inserting users into the database
    def new_user(self, data):
        try:
            self.connect_to_database()
            
            # Define the SQL query to insert user data
            insert_query = """
                INSERT INTO users (id, account_num, username, password, gamebalance, acount_type, balance, currency, friends, owner)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Prepare the data with the correct order
            prep_data = tuple(data)

            # Execute the SQL query to insert the data
            self.cursor.execute(insert_query, prep_data)

            # Commit the changes
            self.conn.commit()
            
            # Close connection
            self.cursor.close()
            self.conn.close()

            print(f"User data inserted successfully.")
        
        except connector.Error as err:
            print(f"Error: {err}")
    
    # Funciton for inserting savings transactions into the database
    def new_transaction(self, transaction):
        try:
            self.connect_to_database()
        
            insert_query = """
                INSERT INTO transactions (id, date, amount, currency, description, username, account_num)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            self.cursor.execute(insert_query, transaction)

            # Commit the changes
            self.conn.commit()
            
            # Close connection
            self.cursor.close()
            self.conn.close()
            
        except connector.Error as err:
            print(f"Error: {err}")

    # Delete a user from the user table
    def delete_data(self, data=None):
            try:
                self.connect_to_database()

                # Check if the user exists
                check_user_query = "SELECT COUNT(*) FROM users WHERE owner = %s"
                self.cursor.execute(check_user_query, (data,))
                user_exists = self.cursor.fetchone()[0]

                if user_exists > 0:
                    # Delete the user if they exist
                    delete_query = "DELETE FROM users WHERE owner = %s"
                    self.cursor.execute(delete_query, (data,))
                    self.conn.commit()
                    print(f"User: {data} was deleted")
                else:
                    print(f"User: {data} not found in the database")

            except connector.Error as err:
                print(f"Error: {err}")

            finally:
                self.cursor.close()
                self.conn.close()
    
    # Deletes all current tables           
    def delete_all_tables(self):
        try:
            self.connect_to_database()
            
            # Define SQL statements to drop each table if it exists
            drop_users_table = "DROP TABLE IF EXISTS users"
            drop_transactions_table = "DROP TABLE IF EXISTS transactions"
            
            # Execute SQL statements to drop tables
            self.cursor.execute(drop_users_table)
            self.cursor.execute(drop_transactions_table)

            # Commit the changes
            self.conn.commit()
            
            print("All tables dropped successfully.")
            
        except connector.Error as err:
            print(f"Error: {err}")

    # Shows all the game users from users table
    def show_gameusers(self):
        try:
            self.connect_to_database() 
            
            select_query = "SELECT * FROM users"
            
            self.cursor.execute(select_query)
            
            rows = self.cursor.fetchall()

            if not rows:
                print("Database is empty")
            else:
                return rows
                    
        except connector.Error as err:
            print(f"Error: {err}")

        finally:
            self.cursor.close()
            self.conn.close()
    
    # Shows all the transactions from the transactions table 
    def show_transactions(self):
        try:
            self.connect_to_database() 
            
            select_query = "SELECT * FROM transactions"
            
            self.cursor.execute(select_query)
            
            rows = self.cursor.fetchall()

            if not rows:
                print("Database is empty")
            else:
                return rows
                    
        except connector.Error as err:
            print(f"Error: {err}")

        finally:
            self.cursor.close()
            self.conn.close()
    
    # Checks if a tables exists        
    def check_if_table_exists(self, table):
        try:
            self.connect_to_database()
            
            check_table_query = f"SHOW TABLES LIKE '{table}'"
            
            self.cursor.execute(check_table_query)
            
            query_rows = self.cursor.fetchall()
            
            if query_rows:
                return True
            else:
                return False

            
        except connector.Error as err:
            print(f"{err}")
        

if __name__ == "__main__":
    pass
    
    
    