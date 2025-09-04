class AuthManager:
    def __init__(self):
        self.users = {}
    
    def register(self, username, password):
        if len(password) < 8:
            raise ValueError("Password too short")
        if not any(c.isupper() for c in password):
            raise ValueError("Password needs uppercase letter")
        self.users[username] = password
        return True
    
    def login(self, username, password):
        return self.users.get(username) == password
    
    def logout(self, username):
        return True
    
    def list_users(self):
        return list(self.users.keys())