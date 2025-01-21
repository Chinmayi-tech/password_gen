import random
import string

def generate_password(length, include_special_chars=True):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    password = generate_password(length, include_special)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
