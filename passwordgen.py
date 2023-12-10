import random
import string

def generate_password(length=12):
    """
    Generate a random password of a specified length.

    Args:
        length (int): The length of the password.

    Returns:
        str: The randomly generated password.
    """
    # Ensure the length is at least 4.
    if length < 4:
        print("Error: length should be at least 4")
        return None

    # Generate a random password using the specified character types.
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Include at least one lowercase letter, one uppercase letter, and one digit.
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))

    # For the remaining characters, include randomly selected characters from the specified character types.
    for i in range(length - 3):
        password.append(random.choice(password_characters))

    # Shuffle the password characters to ensure randomness.
    random.shuffle(password)

    # Join the password characters into a single string and return it.
    return ''.join(password)


# Example usage:
password = generate_password(12)
print(f"Generated password: {password}")