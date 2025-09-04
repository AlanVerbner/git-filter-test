class AuthManager:
    def __init__(self):
        self.users = {}
    
    def register(self, username, password):
        self.users[username] = password
        return True
    
    def login(self, username, password):
        return self.users.get(username) == password