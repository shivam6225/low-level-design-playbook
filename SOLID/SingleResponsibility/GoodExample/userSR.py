class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def get_user_info(self):
        print(f"This user is {self.name} and my age is {self.age}")

    def is_adult(self):
        return self.age >= 18


