from userSR import User

class UserRepo:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_to_db(self,user:User):
        print(f"{user.name} is saving to database")