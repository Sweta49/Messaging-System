from user import User
from message import Message
import db_handler as db

# Function for user registration
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    users = db.load_users()
    if username in users:
        print("Username already exists. Please choose a different one.")
        return

    new_user = User(username, password)
    users[username] = {"password": password, "messages": []}
    db.save_users(users)
    print("User registered successfully!")

# Function for user login
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = db.load_users()
    if username not in users or users[username]["password"] != password:
        print("Invalid username or password.")
        return None

    print("Login successful!")
    return username

# Function to send a message
def send_message(sender):
    receiver = input("Enter username of the receiver: ")

    # Load users to check if receiver exists
    users = db.load_users()
    if receiver == sender or receiver not in users:
        print("Invalid receiver.")
        return

    content = input("Enter your message: ")

    # Create a message object
    message = Message(sender, receiver, content)

    # Append message to sender's and receiver's message list
    users[sender]["messages"].append(message.__dict__)
    users[receiver]["messages"].append(message.__dict__)

    # Save updated user data
    db.save_users(users)

    # Append message to global messages
    messages = db.load_messages()
    messages.append(message.__dict__)
    db.save_messages(messages)

    print("Message sent successfully!")


# Function to delete message history
def delete_message_history(sender):
    # Load users to delete sender's messages
    users = db.load_users()
    users[sender]["messages"] = []

    # Save updated user data
    db.save_users(users)

    print("Message history deleted.")


# Function to view message history with a specific user
def view_message_history(sender):
    users = db.load_users()
    messages = users[sender]["messages"]

    if not messages:
        print("No message history.")
        return

    print("Your message history:")
    for msg in messages:
        print(f"To: {msg['receiver']}, Message: {msg['content']}")

# Main function
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Send Message\n4. View Message History\n5. Delete Message History\n6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                while True:
                    print("\n1. Send Message\n2. View Message History\n3. Delete Message History\n4. Logout")
                    user_choice = input("Select an option: ")
                    if user_choice == "1":
                        send_message(username)
                    elif user_choice == "2":
                        view_message_history(username)
                    elif user_choice == "3":
                        delete_message_history(username)
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            print("Please login first.")
        elif choice == "4":
            print("Please login first.")
        elif choice == "5":
            print("Please login first.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
