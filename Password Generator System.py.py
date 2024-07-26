import random
import string
import secrets

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for better security.")
    
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password has at least one character from each set
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password += [secrets.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

# Example usage
password_length = 16
print(f"Generated password: {generate_password(password_length)}")
