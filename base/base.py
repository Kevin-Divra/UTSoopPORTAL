class base:
    def __init__(self, user_nim, name, email, password):
        self.user_nim = user_nim  # Encapsulation: Private attribute
        self.name = name
        self.email = email
        self.user_password = password

    def login(self, nim, password):
        if nim == self.user_nim and password == self.user_password:
            return True
        else:
            return False