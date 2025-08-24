import sys

class CaesarCipher:
    """
    A class to perform Caesar cipher encryption and decryption.
    Handles uppercase and lowercase English letters, preserves other characters.
    """
    def __init__(self, shift: int):
        """
        Initializes the CaesarCipher object with a specific shift value.

        Args:
            shift (int): The number of positions to shift characters.
        """
        # Ensure shift is within a valid range (0-25) for consistency,
        # though Python's % handles negative shifts correctly.
        self.shift = shift % 26

    def _transform_char(self, char: str, is_encrypt: bool) -> str:
        """
        Helper method to apply the Caesar cipher shift to a single character.
        """
        if char.isupper():
            start = ord('A')
        elif char.islower():
            start = ord('a')
        else:
            return char # Return non-alphabetic characters unchanged

        current_val = ord(char) - start
        
        if is_encrypt:
            shifted_val = (current_val + self.shift) % 26
        else:
            shifted_val = (current_val - self.shift) % 26
            
        return chr(shifted_val + start)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a given plaintext string using the initialized shift.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted ciphertext.
        """
        return "".join(self._transform_char(char, is_encrypt=True) for char in plaintext)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a given ciphertext string using the initialized shift.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted plaintext.
        """
        return "".join(self._transform_char(char, is_encrypt=False) for char in ciphertext)

# --- Application Logic (User Interaction) ---

def run_caesar_cipher_app_oop():
    """
    Runs the interactive Caesar Cipher application using the OOP approach.
    """
    print("Welcome to the OOP Caesar Cipher Tool!")
    print("--------------------------------------")

    while True:
        print("\nWhat would you like to do?")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force a message (crack)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1' or choice == '2':
            message = input("Enter your message: ")
            while True:
                try:
                    shift_input = int(input("Enter the shift number (an integer, e.g., 3): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number for the shift.")
            
            # Create an instance of the CaesarCipher class with the user's shift
            cipher = CaesarCipher(shift_input) 

            if choice == '1':
                processed_message = cipher.encrypt(message)
                print(f"\nYour encrypted message is: {processed_message}")
            else: # choice == '2'
                processed_message = cipher.decrypt(message)
                print(f"\nYour decrypted message is: {processed_message}")

        elif choice == '3':
            message_to_crack = input("Enter the message to brute-force: ")
            print(f"\n--- Brute-forcing '{message_to_crack}' ---")
            for shift_attempt in range(26):
                # For brute-forcing, we create a new CaesarCipher instance for each possible shift
                cracker = CaesarCipher(shift_attempt)
                decrypted_attempt = cracker.decrypt(message_to_crack)
                print(f"Shift {shift_attempt:2d}: {decrypted_attempt}")
            print("\nLook through the possible decryptions above. One of them should be the original message!")

        elif choice == '4':
            print("Exiting OOP Caesar Cipher Tool. Goodbye!")
            sys.exit() # Exit the program gracefully

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Main execution block ---
if __name__ == "__main__":
    run_caesar_cipher_app_oop()