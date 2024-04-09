class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
