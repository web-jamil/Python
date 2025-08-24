import sys

# --- Caesar Cipher Core Functions ---

def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypts a plaintext string using the Caesar cipher.
    Handles uppercase and lowercase English letters, preserves others.
    """
    encrypted_text = ""
    for char in text:
        if char.isupper():
            # Shift uppercase letters (A=65, B=66, ..., Z=90)
            # (ord(char) - 65) converts 'A' to 0, 'B' to 1, etc.
            # % 26 ensures wrap-around (e.g., (25 + 3) % 26 = 2)
            # + 65 converts back to ASCII for uppercase letters
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters (a=97, b=98, ..., z=122)
            # (ord(char) - 97) converts 'a' to 0, 'b' to 1, etc.
            # % 26 ensures wrap-around
            # + 97 converts back to ASCII for lowercase letters
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave non-alphabetic characters (numbers, symbols, spaces) unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypts a ciphertext string using the Caesar cipher.
    Handles uppercase and lowercase English letters, preserves others.
    """
    decrypted_text = ""
    for char in text:
        if char.isupper():
            # Reverse shift for uppercase letters
            # Using -shift directly handles negative results correctly with Python's % operator
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            # Reverse shift for lowercase letters
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(text: str):
    """
    Attempts to decrypt a Caesar cipher ciphertext by trying all 26 possible shifts.
    Prints each potential decryption.
    """
    print(f"\n--- Brute-forcing '{text}' ---")
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2d}: {decrypted}")

# --- User Interaction Logic ---

def run_caesar_cipher_app():
    """
    Runs the interactive Caesar Cipher application.
    """
    print("Welcome to the Caesar Cipher Tool!")
    print("----------------------------------")

    while True:
        print("\nWhat would you like to do?")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force a message (crack)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift number (an integer, e.g., 3): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number for the shift.")
            encrypted = caesar_encrypt(message, shift)
            print(f"\nYour encrypted message is: {encrypted}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift number (an integer, e.g., 3): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number for the shift.")
            decrypted = caesar_decrypt(message, shift)
            print(f"\nYour decrypted message is: {decrypted}")

        elif choice == '3':
            message = input("Enter the message to brute-force: ")
            brute_force_caesar(message)
            print("\nLook through the possible decryptions above. One of them should be the original message!")

        elif choice == '4':
            print("Exiting Caesar Cipher Tool. Goodbye!")
            sys.exit() # Exit the program gracefully

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Main execution block ---
if __name__ == "__main__":
    run_caesar_cipher_app()