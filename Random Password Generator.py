import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    try:
        length = int(length_input.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        # Characters to use in the password
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        
        
        # Guarantee at least one character from each category
        password = [
            random.choice(lowercase_letters),
            random.choice(uppercase_letters),
            random.choice(digits),
            random.choice(special_characters)
        ]

        # Fill the remaining length with random choices from all categories
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
        password += random.choices(all_characters, k=length - 4)

        # Shuffle the password to mix the characters
        random.shuffle(password)

        # Display the generated password
        result_entry.delete(0, tk.END)
        result_entry.insert(0, ''.join(password))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

