# Caesar Cipher Program

# Function to encrypt the message
def encrypt(text, shift):
    # Empty string to store the final encrypted message
    encrypted_text = ""
    
    # Loop through each character in the input text
    for char in text:
        # Only shift alphabetic characters (skip numbers, punctuation, etc.)
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            # We'll handle both cases correctly by using different ASCII ranges
            base = 65 if char.isupper() else 97
            
            # Shift the character and wrap it within A-Z or a-z using modulo
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabet characters are not shifted, just added as-is
            encrypted_text += char
            
    return encrypted_text

# Function to decrypt the message (just the reverse of encryption)
def decrypt(text, shift):
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)

# Main program loop where we get user input and process the message
def main():
    # Ask user if they want to encrypt or decrypt
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    # Get the actual message and shift value from the user
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g., 3): "))

    # Handle user's choice
    if choice == 'E':
        # Encrypt and display the result
        print(f"Encrypted Message: {encrypt(message, shift)}")
    elif choice == 'D':
        # Decrypt and display the result
        print(f"Decrypted Message: {decrypt(message, shift)}")
    else:
        # Handle invalid input (user didn't type E or D)
        print("Invalid choice, please enter 'E' for encryption or 'D' for decryption.")

# Only run the main function if this file is executed directly (not imported)
if __name__ == "__main__":
    main()
