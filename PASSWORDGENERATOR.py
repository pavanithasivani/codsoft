import random
import string


def generate_password(length):
   
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters


    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Add random characters to meet the desired length
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    # Join the characters to create the final password
    return "".join(password)

# Main function to interact with the user
def main():
    try:
        # Prompt the user to enter the desired length for the password
        password_length = int(input("Enter the desired length for the password: "))

        # Validate the length
        if password_length < 4:
            print("Password length must be at least 4 characters.")
            return

        # Generate and display the password
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
