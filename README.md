SavingsQuest is an innovative savings application that transforms the act of saving money into an exciting and rewarding activity! My mission is to make the journey towards financial stability entertaining and enjoyable.

### About SavingsQuest:
SavingsQuest offers a unique and engaging way to encourage saving while immersing you in a captivating gaming experience. Unlike traditional savings methods, SavingsQuest takes a gamified approach, turning every dollar saved into a valuable resource in your in-game adventure.

### Gameplay and Vision:
Imagine a world where your financial decisions directly impact your progress in an epic gaming universe. In SavingsQuest, you embark on a journey reminiscent of popular mobile games like Clash of Clans, but with a twist, you invest in yourself!

### Key Features:
Savings with a Purpose: Every dollar you save in SavingsQuest contributes to your in-game wealth and progress. The more you save, the stronger you become in the game.

### Resourceful Saving: 
Our application lets you accumulate resources, weapons, and assets, all fueled by your real-world savings. These resources are pivotal in your quest for virtual dominance.

### Compete and Collaborate: 
Engage in epic battles and collaborative challenges with fellow savers. Challenge them to see who can save and grow the fastest.

### Unlock Financial Achievements: 
As you reach various savings milestones, you unlock financial achievements that grant you advantages in the game and recognition among fellow adventurers.

### Smart Goal Setting: 
Set savings goals within the game, and when you achieve them, reap in-game rewards that keep you motivated to save.

### Financial Education: 
Along the way, you'll gain valuable financial insights and knowledge that will empower you to make better financial decisions in the real world.

### Requirements:
Before using the Game User Application, ensure you have the following requirements installed:

Python 3.x
mysql server
mysql Connector/Python (Install using pip install mysql-connector-python)
hashlib (Available in Python standard library)
Setup

### Run the Application:
I had some trouble packaging the MySQL dependency and the openai package. The only alternative I came up with was for you to manually
install the package before running it. So before you run the program, please run:

pip install mysql-connector-python
and
pip install openai

Afterward, you can run the main function in main.py


### Usage
### Sign Up:
To create a new account, select option 1 from the main menu.
Enter your name, friends in the game, a username, and a secure password.
Passwords must meet specific criteria to ensure security.
Once the account is successfully created, you'll receive a confirmation message.

### Login:
Registered users can log in with their username and password.
Select option 2 from the main menu.
Enter your username and password.
If the login is successful, you'll be logged into your account.
Save Money:

Logged-in users can save virtual money to their accounts.
Select option 3 from the main menu.
Enter the amount you want to save.
The application calculates virtual game money earned based on the amount saved.
The transaction is stored in the database.
Set Savings Goal:

Users can set savings goals to earn in-game rewards.
Select option 4 from the main menu.
Enter your savings goal amount.
The application tracks your progress toward the goal and notifies you when you've reached it.

### Personal Finance Assistant (Chat GPT)
Ask your persoanl finance assistant anything finance related. This will help the users make better finantional decissions when saving.
The API only allows a certin amount of questions so after a couple of questions the model will not provide an answer.

### Log Out:
To log out and protect your account, select option 5 from the main menu.

