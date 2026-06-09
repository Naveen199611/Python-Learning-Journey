import random
import string

print("---- Welcome to Python Password Generator -----")

def password_generator(length):
    if length < 4:
        return "Password length must be at least 4 characters"

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    chars = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)


length = int(input("Enter Password Length: "))

final_password = password_generator(length)

# Store generated password in a file
with open("Passwords.txt", "a") as file:
    file.write(final_password + "\n")

print(f"Generated Password: {final_password}")