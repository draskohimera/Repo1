import random

def generate_password(length=12):
    """Generate a random password of a specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def check_password_strength(password):
    """Check the strength of a password."""
    score = 0
    if any(char.isdigit() for char in password):
        score += 2
    if any(char.isupper() for char in password):
        score += 2
    if any(char.islower() for char in password):
        score += 2
    if any(char in "!@#$%^&*()_+" for char in password):
        score += 3
    if len(password) >= 8:
        score += 2
    return score

def main():
    """Main function."""
    print("Welcome to the Password Generator and Strength Checker!")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
    strength = check_password_strength(password)
    print(f"Password Strength Score: {strength}")

if __name__ == "__main__":
    main()