import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters + string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 1 for alphanumeric or 2 for alphanumeric with special characters.")

    password = ''.join(random.choice(characters) for i in range(length))

    if complexity == 2:
        while not any(c.islower() for c in password) or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
            password = ''.join(random.choice(characters) for i in range(length))

    return password

length = int(input("Enter the desired password length: "))
complexity = int(input("Enter the complexity level (1 for alphanumeric, 2 for alphanumeric with special characters): "))

password = generate_password(length, complexity)
print("Generated password:", password)