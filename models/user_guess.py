class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


personal_details = User("Laxmi", "Baruch")


def guess_number() -> str:
    user_input = input("Guess a number: ")
    return user_input



