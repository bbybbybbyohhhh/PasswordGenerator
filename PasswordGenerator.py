import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    # Define character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters !@#$%^&*()

    # Start with letters as the base character set
    char_pool = letters

    # Add digits and special characters to the pool if selected
    if use_digits:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for i in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Ask if the user wants digits and special characters in the password
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_digits, use_special_chars)
    
    # Output the generated password
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()

