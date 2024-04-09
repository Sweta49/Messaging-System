import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)

def load_messages():
    try:
        with open('messages.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_messages(messages):
    with open('messages.json', 'w') as file:
        json.dump(messages, file)
